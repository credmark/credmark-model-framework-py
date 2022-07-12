from typing import List, Union
from credmark.cmf.model.errors import ModelDataError
from credmark.cmf.types.token import Tokens, Token
from credmark.cmf.types.contract import Contract
from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr
from credmark.cmf.types.portfolio import Portfolio


class Pool(Contract):
    """
    A pool is a contract that consolidates assets on behalf of many accounts to perform
    a financial function.
    """

    tokens: Tokens = DTOField(description="The tokens that are supported by the pool.")
    portfolio: Portfolio = DTOField(description="The positions of the pool")

    def __init__(self, **data):
        if len(data.get("tokens")) != len(data.get("balances")):
            raise ModelDataError(
                message="Pool balances and Pool tokens must be the same size array.")
        super().__init__(**data)


class SwapPool(Pool):
    """
    Swap Pools are pools that represent an liquidity pool enabling Swaps between tokens.
    These are commonly the building blocks of DEXes, such as Uniswap and Curve Finance.

    Note: The token reserves may not be custodied by the pool contract itself, representing
    virtual custody.
    """


class ConstantProductSwapPool(SwapPool):
    """
    SymmetricSwapPools are Swap Pools that follow an x*y=k based swap algoritm.
    """

    def __init__(self, **data):
        if len(data.get("tokens")) != 2:
            raise ModelDataError(
                message="There must be 2 tokens and 2 balances in a FlatAMMSwapPool")
        super().__init__(**data)

    @property
    def swap_spot_price(self, base: Union[Token, None] = None):
        quote = self.tokens[1]
        if base is None:
            base = self.tokens[0]
        if base == self.tokens[1]:
            quote = self.tokens[0]
        base_liquidity = None
        quote_liquidity = None
        for position in self.portfolio:
            if position.asset == base:
                base_liquidity = position.amount
            if position.asset == quote:
                quote_liquidity = position.amount
        if base_liquidity is None:
            raise ModelDataError("Token " + base.symbol + " not found in Pool.")
        if quote_liquidity is None:
            raise ModelDataError("Token " + quote.symbol + " not found in Pool.")
        if quote_liquidity == 0 or base_liquidity == 0:
            raise ModelDataError("No Liquidity in Pool " + self.address)
        return base_liquidity / quote_liquidity


class TokenizedConstantProductSwapPool(SwapPool):

    lp_token: Union[Token, None] = DTOField(default=None,
                                            description="The Liquidity Provider "
                                            "Token for this pool.")


class Pools(IterableListGenericDTO[Pool]):
    pools: List[Pool] = DTOField(
        default=[], description="An iterable list of Pool Objects")
    _iterator: str = PrivateAttr('pools')


class SwapPools(IterableListGenericDTO[SwapPool]):
    pools: List[Pool] = DTOField(
        default=[], description="An iterable list of SwapPool Objects")
    _iterator: str = PrivateAttr('pools')


class ConstantProductSwapPools(IterableListGenericDTO[ConstantProductSwapPool]):
    pools: List[Pool] = DTOField(
        default=[], description="An iterable list of FlatAmmPairedSwapPool Objects")
    _iterator: str = PrivateAttr('pools')
