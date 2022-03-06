
import credmark.model
from .contract import Contract, Address
from .token_data import TOKEN_DATA, MIN_ERC20_ABI
from typing import List, Union
from ..dto import IterableListDto
from ..models.core import CoreModels


class Token(Contract):
    symbol: Union[str, None]
    decimals: Union[int, None]
    address: Union[Address, None]

    def __init__(self, **data):

        if 'symbol' not in data or \
            'decimals' not in data or \
            'address' not in data or \
                'name' not in data:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ValueError(f'No current context to look up missing token data {data}')

            chain_id = context.chain_id
            td = []
            if 'address' in data:
                td = [t for t in TOKEN_DATA[str(chain_id)] if t['address'] == data['address']]
            elif 'symbol' in data:
                td = [t for t in TOKEN_DATA[str(chain_id)] if t['symbol'] == data['symbol']]
            elif 'name' in data:
                td = [t for t in TOKEN_DATA[str(chain_id)] if t['name'] == data['name']]

            if len(td) == 1:
                td = td[0]
                data['symbol'] = td['symbol']
                data['address'] = td['address']
                data['name'] = td.get('name', None)
                data['decimals'] = td.get('decimals', None)
                data['protocol'] = td.get('protocol', None)

            # TODO: un-hardcode this

            if 'abi' not in data:
                data['abi'] = MIN_ERC20_ABI

            if data.get('decimals', None) is None:
                try:
                    data['decimals'] = context.web3.eth.contract(
                        address=Address(str(data.get('address'))).checksum,
                        abi=MIN_ERC20_ABI).functions.decimals().call()
                except Exception:
                    pass

            if data.get('symbol', None) is None:
                try:
                    data['symbol'] = context.web3.eth.contract(
                        address=Address(str(data.get('address'))).checksum,
                        abi=MIN_ERC20_ABI).functions.symbol().call()
                except Exception:
                    pass

            if data.get('name', None) is None:
                try:
                    data['name'] = context.web3.eth.contract(
                        address=Address(str(data.get('address'))).checksum,
                        abi=MIN_ERC20_ABI).functions.name().call()
                except Exception:
                    pass

        super().__init__(**data)

    @property
    def price_usd(self):
        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ValueError(f'No current context to get price of token {self.symbol}')
        return context.run_model(CoreModels.token_price, self).get('price_usd')


class Tokens(IterableListDto):
    tokens: List[Token]
    iterator = 'tokens'
