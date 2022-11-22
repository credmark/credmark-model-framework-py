
from .contract import Contract


class NonFungibleToken(Contract):
    """
    Non-fungible token.

    `This class is not yet implemented`
    """

    def __init__(self, **data):
        super().__init__(**data)
        raise NotImplementedError()

    @property
    def ledger(self) -> None:
        return None
