from typing import Any

from eth_typing import URI

from hexbytes import HexBytes
from web3._utils.request import get_response_from_post_request
from credmark.cmf.engine.web3.helper import MulticallResult
import credmark.cmf.model
from credmark.cmf.model.errors import ModelEngineError
from credmark.cmf.engine.web3.batch import Payload, Web3Batch


class Web3BatchRpc(Web3Batch):
    def _process_payloads(self, payloads: list[Payload]) -> list[MulticallResult]:
        if not payloads:
            return []

        context = credmark.cmf.model.ModelContext.current_context()
        block = hex(int(context.block_number))
        queries: list[dict[str, Any]] = []
        for i, payload in enumerate(payloads):
            assert "data" in payload, "`data` not present"
            assert "to" in payload, "`to` not present"
            assert "output_type" in payload, "`output-type` not present"

            query_params = {"to": payload["to"], "data": payload["data"]}  # Balance of
            if "from" in payload:
                query_params["from"] = payload["from"]

            queries.append(
                {
                    "jsonrpc": "2.0",
                    "method": "eth_call",
                    "params": [
                        query_params,
                        block,
                    ],
                    "id": i,
                }
            )

        provider_url = context._web3_registry.provider_url_for_chain_id(  # pylint: disable=protected-access
            context.chain_id)
        response = get_response_from_post_request(URI(provider_url), json=queries)
        if not response.ok:
            raise ModelEngineError(
                f"Error connecting to {provider_url}: {response.text}"
            )

        results = response.json()

        if isinstance(results, dict) and "error" in results:
            raise ValueError(f"Batch request error: {results}")

        return_values: list[MulticallResult] = []
        errors = []
        for payload, result in zip(
            payloads, sorted(results, key=lambda x: x["id"])
        ):
            if "error" in result:
                fn_name = payload.get("fn_name", HexBytes(payload["data"] or "").hex())
                errors.append(f'`{fn_name}`: {result["error"]}')
                return_values.append(MulticallResult(False, b""))
            else:
                return_values.append(MulticallResult(True, HexBytes(result["result"])))

        return return_values
