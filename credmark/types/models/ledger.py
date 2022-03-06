from typing import List
from credmark.types.dto import DTO, DTOField, IterableListDto


class LedgerModelOutput(IterableListDto):
    data: List[dict] = DTOField([], description='A list of dicts which are the rows of data')
    iterator = "data"
