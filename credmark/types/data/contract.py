from ..dto import DTO, DTOField
from .address import AddressStr

from typing import Optional


class ContractMeta(DTO):
    contractName: str
    protocol: str
    product: str
    chainId: int
    constructorArgs: str  # ":Hash[]",
    deploymentTx: str  # ":Hash"


class Contract(DTO):
    address: AddressStr = DTOField(0.0, description='address')
    abi: str = DTOField(0.0, description='abi')
    meta: ContractMeta = DTOField(description='meta')
