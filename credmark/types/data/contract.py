from typing import (
    List
)
from .address import AddressStr
from .json import JsonDict, JsonStr, JsonList
from ..dto import DTO, Json

#  Contracts(contracts=contract_q_results['contracts'])
#  Contract(contract_q_results['contracts'][0])
#  json.dumps(contract_q_results['contracts'][0]['abi'])
# JsonDict


class Contract2(DTO):
    name: str
    address: AddressStr
    deploy_tx_hash: str  # hexstr
    constructor_args: str  # hexstr
    abi_hash: str  # hexstr
    abi: JsonStr  # json


class Contract(DTO):
    name: str
    address: str
    deploy_tx_hash: str  # hexstr
    constructor_args: str  # hexstr
    abi_hash: str  # hexstr
    abi: JsonList  # json


class Contracts(DTO):
    contracts: List[Contract]
