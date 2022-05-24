# pylint: disable=locally-disabled, unused-import, unused-variable
import importlib
import sys
import inspect
from typing import List
from datetime import datetime, date, timezone, timedelta
import IPython

import os
import logging
import yaml

from web3.exceptions import ABIFunctionNotFound
from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.model_api import ModelApi

from credmark.cmf.model import Model
from credmark.cmf.model.context import RunModelMethod
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from credmark.cmf.model.print import print_manifest_description
from credmark.cmf.types import (
    Address,
    Account, Contract, Token,
    Accounts, Contracts, Tokens,
    Portfolio, Position,
    Price, PriceList,
    BlockNumber,
    NativeToken,
    NativePosition,
    TokenPosition,
    ContractLedger,
)

from credmark.dto import DTO, DTOField, EmptyInput, IterableListGenericDTO, PrivateAttr

from credmark.cmf.types.ledger import (BlockTable, ContractTable,
                                       LogTable,
                                       ReceiptTable, TokenTable,
                                       TokenTransferTable, TraceTable,
                                       TransactionTable)


@Model.describe(slug='composer',
                version='1.0',
                display_name='composer',
                description='Credmark Model REPL')
class Composer(Model):
    def run(self, _) -> dict:
        return {1: 1}


from credmark.model.utils.dask_utils import DaskUtils

  @property
   def cluster(self):
        if self._cluster is None:
            cluster = Cluster(cluster=self._cluster_str,
                              web3_http_provider=self._web3_registry.provider_url(
                                  self.chain_id),
                              block_number=self.block_number,
                              model_paths=[] if self._model_paths is None else self._model_paths,
                              open_browser=False)
            self._cluster = cluster
        return self._cluster

    parser_run.add_argument('--cluster', dest='cluster_str', type=str, default='sequence', required=False,
                            help=('enable cluster with configuration: '
                                  '"sequence", '
                                  'n-process: "localhost:n" or '
                                  'dask cluster, "tcp://localhost:8786"'))

    def run_pipe(self, pipe: Pipe, outputs: List[str]):
        return pipe.run(self.cluster, outputs)

from .engine.pipe import Task, ModelTask, Pipe
