from abc import ABC, abstractmethod
from typing import Any, Iterator, Literal, NotRequired, Sequence, TypedDict, TypeVar, cast, overload

from eth_abi.exceptions import DecodingError
from eth_typing import ChecksumAddress, HexStr
from web3._utils.abi import map_abi_data
from web3._utils.normalizers import BASE_RETURN_NORMALIZERS
from web3.contract.contract import ContractFunction
from web3.exceptions import BadFunctionCallOutput
from web3.types import ABIFunctionParams, TxParams, Wei

import credmark.cmf.model
from credmark.cmf.engine.web3.helper import MulticallDecodedResult, MulticallResult
from credmark.cmf.model.errors import ModelEngineError

T = TypeVar("T")
U = TypeVar("U", bound=tuple)


Payload = TypedDict('Payload', {
    'data': bytes | HexStr | None,
    'output_type': Sequence[str],
    'to': ChecksumAddress,
    'fn_name': str | None,
    'from': NotRequired[ChecksumAddress]
})


class Web3Batch(ABC):
    def _divide_chunks(self,
                       big_list: Sequence[T],
                       chunk_size: int) -> Iterator[Sequence[T]]:
        for i in range(0, len(big_list), chunk_size):
            yield big_list[i:i + chunk_size]

    def _build_payload(self,
                       contract_functions: Sequence[ContractFunction],
                       *,
                       from_address: ChecksumAddress | None = None):
        payloads: list[Payload] = []
        params: TxParams = {"gas": Wei(0), "gasPrice": Wei(0)}
        for contract_function in contract_functions:
            if not contract_function.address:
                raise ValueError(
                    f"Missing address for batch_call in `{contract_function.fn_name}`"
                )

            data = contract_function.build_transaction(params).get("data")
            outputs: Sequence[ABIFunctionParams] = (
                contract_function.abi["outputs"] if "outputs" in contract_function.abi else [])
            output_types = [output["type"] if "type" in output else "" for output in outputs]
            payload: Payload = {
                "to": contract_function.address,
                "data": data,
                "output_type": output_types,
                "fn_name": contract_function.fn_name,  # For debugging purposes
            }
            if from_address:
                payload["from"] = from_address
            payloads.append(payload)

        return payloads

    def _build_payload_same_function(self,
                                     contract_function: ContractFunction,
                                     contract_addresses: Sequence[ChecksumAddress],
                                     *,
                                     from_address: ChecksumAddress | None = None):
        params: TxParams = {"gas": Wei(0), "gasPrice": Wei(0)}
        data = contract_function.build_transaction(params).get("data")
        outputs: Sequence[ABIFunctionParams] = (contract_function.abi["outputs"]
                                                if "outputs" in contract_function.abi else [])
        output_types = [output["type"] if "type" in output else "" for output in outputs]
        fn_name = contract_function.fn_name

        payloads: list[Payload] = []
        for contract_address in contract_addresses:
            payload: Payload = {
                "to": contract_address,
                "data": data,
                "output_type": output_types,
                "fn_name": fn_name,  # For debugging purposes
            }
            if from_address:
                payload["from"] = from_address
            payloads.append(payload)

        return payloads

    def _decode_data(self,
                     fn_name: str | None,
                     output_types: Sequence[str],
                     return_data: bytes):
        w3 = credmark.cmf.model.ModelContext.current_context().web3
        try:
            output_data = w3.codec.decode(output_types, return_data)
        except DecodingError as e:
            msg = (
                f"Could not decode contract function call to {fn_name} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
            )

            raise BadFunctionCallOutput(msg) from e
        # Workaround for https://github.com/ethereum/eth-abi/issues/142
        except OverflowError as e:
            msg = (
                f"Could not decode contract function call to {fn_name} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
            )

            raise BadFunctionCallOutput(msg) from e

        normalized_data = map_abi_data(
            BASE_RETURN_NORMALIZERS, output_types, output_data)

        if len(normalized_data) == 1:
            return normalized_data[0]
        else:
            return normalized_data

    def _decode_results(self,
                        payloads: list[Payload],
                        encoded_results: list[MulticallResult],
                        *,
                        require_success: bool = False,
                        ):
        results: list[MulticallDecodedResult] = []
        for payload, multicall_result in zip(payloads, encoded_results):
            success = multicall_result.success
            encoded_data = multicall_result.return_data
            # If fallback function is defined, require_success will
            # be enforced when calling fallback function
            if require_success and (not success or encoded_data == b""):
                # `b''` values are decoding errors/missing contracts/missing functions
                raise ModelEngineError("Multicall function failed")

            try:
                data = self._decode_data(payload['fn_name'],
                                         payload['output_type'],
                                         encoded_data) \
                    if multicall_result.success else encoded_data
            except BadFunctionCallOutput:
                success = False
                data = multicall_result.return_data
            results.append(MulticallDecodedResult(
                success,
                data,
            ))

        return results

    @abstractmethod
    def _process_payloads(self, payloads: list[Payload]) -> list[MulticallResult]:
        ...

    @overload
    def call(
            self,
            contract_functions: Sequence[ContractFunction],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            unwrap: Literal[True],
            unwrap_default: Any = None,
            return_type: type[U] = tuple[Any, ...]) -> U:
        ...

    @overload
    def call(
            self,
            contract_functions: Sequence[ContractFunction],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            unwrap: Literal[False] = ...,) -> tuple[MulticallDecodedResult[Any], ...]:
        ...

    def call(
            self,
            contract_functions: Sequence[ContractFunction],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            unwrap: bool = False,
            unwrap_default: Any = None,
            return_type: type[U] = tuple[Any]) -> U:  # pylint: disable=unused-argument
        results: list[MulticallDecodedResult] = []
        for chunk in self._divide_chunks(contract_functions, batch_size):
            payloads = self._build_payload(chunk)
            encoded_results = self._process_payloads(payloads)
            results.extend(self._decode_results(payloads,
                                                encoded_results,
                                                require_success=require_success))

        if unwrap:
            # pylint disable=consider-using-generator
            return cast(U, tuple(result.unwrap(unwrap_default) for result in results))

        return cast(U, tuple(results))

    @overload
    def call_same_function(
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_functions: Sequence[ContractFunction] | None = None,
            unwrap: Literal[True]) -> list[Any]:
        ...

    @overload
    def call_same_function(
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_functions: Sequence[ContractFunction] | None = None,
            unwrap: Literal[False]) -> list[MulticallDecodedResult[Any]]:
        ...

    # pylint: disable=too-many-arguments
    @overload
    def call_same_function(
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_functions: Sequence[ContractFunction] | None = None,
            unwrap: Literal[True],
            unwrap_default: T = None,
            return_type: type[T] | Any = Any) -> list[T]:
        ...

    @overload
    def call_same_function(
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_functions: Sequence[ContractFunction] | None = None,
            unwrap: Literal[False] = ...,
            return_type: type[T] | Any = Any) -> list[MulticallDecodedResult[T]]:
        ...

    # pylint: disable=too-many-arguments
    def call_same_function(  # pylint: disable=too-many-locals
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_functions: Sequence[ContractFunction] | None = None,
            unwrap: bool = False,
            unwrap_default: Any = None,
            return_type: type[T] | Any = Any) -> list[T | None] | list[MulticallDecodedResult[T]]:  # pylint: disable=unused-argument
        results: list[MulticallDecodedResult[T]] = []
        for chunk in self._divide_chunks(contract_addresses, batch_size):
            payloads = self._build_payload_same_function(contract_function, chunk)
            encoded_results = self._process_payloads(payloads)
            results.extend(self._decode_results(
                payloads,
                encoded_results,
                require_success=require_success and not fallback_functions))

        failed = [(idx, contract_addresses[idx])
                  for idx, decoded_result in enumerate(results) if not decoded_result.success]

        if failed and fallback_functions:
            fallback_results = self.call_same_function(
                fallback_functions[0],
                [address for (_, address) in failed],
                require_success=require_success,
                batch_size=batch_size,
                fallback_functions=fallback_functions[1:])

            for idx, fallback_result in enumerate(fallback_results):
                results[failed[idx][0]] = fallback_result

        if unwrap:
            return [result.unwrap(unwrap_default) for result in results]

        return results
