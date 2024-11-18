from credmark.cmf.engine.web3.batch import Payload, Web3Batch
from credmark.cmf.engine.web3.batch_multicall import Web3BatchMulticall
from credmark.cmf.engine.web3.batch_rpc import Web3BatchRpc
from credmark.cmf.engine.web3.helper import MulticallResult


class Web3BatchFallback(Web3Batch):
    def __init__(
        self,
    ):
        self._multicall = None
        self._rpc = None

    def batch_size(self):
        return self.multicall.batch_size()

    @property
    def multicall(self) -> Web3BatchMulticall:
        """
        A :class:`~credmark.cmf.engine.web3.web3_multicall.Web3Multicall` instance which can be
        used to batch query web3 using multicall.
        """
        if self._multicall is None:
            self._multicall = Web3BatchMulticall()
        return self._multicall

    @property
    def rpc(self) -> Web3BatchRpc:
        """
        A :class:`~credmark.cmf.engine.web3.web3_multicall.Web3Multicall` instance which can be
        used to batch query web3 using multicall.
        """
        if self._rpc is None:
            self._rpc = Web3BatchRpc()
        return self._rpc

    def _process_payloads(self, payloads: list[Payload]) -> list[MulticallResult]:
        try:
            return self.multicall._process_payloads(payloads)  # pylint: disable=protected-access
        except Exception:
            return self.rpc._chunk_process_payloads(payloads)  # pylint: disable=protected-access
