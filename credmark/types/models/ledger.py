from typing import List
from credmark.types import DTO, DTOField


class LedgerModelOutput(DTO):
    data: List[dict] = DTOField([], description='A list of dicts which are the rows of data')
