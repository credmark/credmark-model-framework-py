from typing import cast

from eth_typing import ChecksumAddress
from web3.contract.contract import Contract
from web3.exceptions import ContractLogicError

import credmark.cmf.model
from credmark.cmf.engine.web3.batch import Payload, Web3Batch
from credmark.cmf.engine.web3.helper import MULTICALL_V3_ABI, MULTICALL_V3_BYTECODE, MulticallResult
from credmark.cmf.model.errors import ModelEngineError
from credmark.cmf.types.network import Network, NetworkDict

# https://github.com/mds1/multicall#deployments
MULTICALL_CONTRACTS = NetworkDict(
    lambda: "0xcA11bde05977b3631167028862bE2a173976CA11",
    {
        Network.Mainnet: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.Optimism: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.BSC: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.Polygon: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.Fantom: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.ArbitrumOne: "0xcA11bde05977b3631167028862bE2a173976CA11",
        Network.Avalanche: "0xcA11bde05977b3631167028862bE2a173976CA11",
    },
)

MULTICALL_DEPLOYMENT = NetworkDict(
    lambda: None,
    {
        Network.Mainnet: 14353601,
        Network.Optimism: 4286263,
        Network.BSC: 15921452,
        Network.Polygon: 25770160,
        Network.Fantom: 33001987,
        Network.Base: 11907934,
        Network.ArbitrumOne: 7654707,
        Network.Avalanche: 11907934,
        Network.Linea: 42,
        Network.Sepolia: 751532,
    },
)


class Web3BatchMulticall(Web3Batch):
    _contract: Contract | None = None

    def batch_size(self) -> int:
        return 100

    @property
    def contract(self) -> Contract:
        context = credmark.cmf.model.ModelContext.current_context()
        if self._contract is not None:
            if (
                self._contract.w3.eth.chain_id != context.chain_id
                or self._contract.w3.eth.default_block != context.block_number
            ):
                self._contract = None

        if self._contract is None:
            deployment = MULTICALL_DEPLOYMENT.get(context.network)
            if deployment is None or int(context.block_number) < deployment:
                raise ModelEngineError("Multicall contract not available")

            address = cast(ChecksumAddress, MULTICALL_CONTRACTS.get(context.network))
            self._contract = context.web3.eth.contract(
                address=context.web3.to_checksum_address(address),
                abi=MULTICALL_V3_ABI,
                bytecode=MULTICALL_V3_BYTECODE,
            )

        return self._contract

    def _process_payloads(self, payloads: list[Payload]) -> list[MulticallResult]:
        aggregate_parameter = [
            {"target": payload["to"], "callData": payload["data"]} for payload in payloads
        ]
        try:
            result = self.contract.functions.tryAggregate(False, aggregate_parameter).call()
            return [MulticallResult(success, data) for success, data in result]
        except (ContractLogicError, OverflowError, ValueError) as err:
            raise ModelEngineError("Multicall function failed") from err
