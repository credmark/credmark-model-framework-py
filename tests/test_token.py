# pylint:disable=line-too-long

import unittest

import credmark.cmf.model
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.model.errors import ModelBaseError, ModelRunError
from credmark.cmf.types import Account, Address, Contract, Network, Portfolio, Position, Token
from credmark.cmf.types.data.fungible_token_data import FUNGIBLE_TOKEN_DATA_BY_ADDRESS, FUNGIBLE_TOKEN_DATA_BY_SYMBOL
from credmark.cmf.types.token_erc20 import NativeToken
from credmark.dto import DTO
from credmark.dto.transform import transform_data_for_dto


class TCA(DTO):
    token1: Token
    token2: Token
    token3: Token
    token4: Token
    contract1: Contract
    contract2: Contract
    account1: Account
    account2: Account


class TestToken(ModelTestCase):
    def test_portfolio(self):
        p1 = Portfolio(positions=[Position(amount=1, asset=Token("AAVE"))])
        p2 = Portfolio.merge(p1, p1)
        self.assertTrue(p2.positions[0].amount == 2.0)
        self.assertTrue(p1.positions[0].amount == 1.0)

        p3 = Portfolio(positions=[Position(amount=2, asset=Token("CMK")),
                       Position(amount=4, asset=Token("LINK"))])
        p4 = Portfolio.merge(p3, p1)
        self.assertTrue(p1.positions[0].amount == 1.0)
        self.assertTrue(len(p4.positions) == 3)
        self.assertTrue(sum([p.amount for p in p4.positions]) == 7)

    def test_native(self):
        nt = NativeToken()

        self.assertTrue(nt == Token(
            address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeee'))
        self.assertTrue(nt == Token(symbol='ETH'))
        self.assertTrue(nt == Token(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeee'))
        self.assertTrue(nt == Token('ETH'))

        self.assertTrue(nt == NativeToken(
            address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeee'))
        self.assertTrue(nt == NativeToken(symbol='ETH'))
        self.assertTrue(nt == NativeToken(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeee'))
        self.assertTrue(nt == NativeToken('ETH'))

        with self.assertRaises(ModelRunError):
            NativeToken(address=Token('AAVE').address)

        with self.assertRaises(ModelRunError):
            NativeToken(symbol='AAVE')

        with self.assertRaises(ModelRunError):
            NativeToken('AAVE')

        with self.assertRaises(ModelRunError):
            NativeToken(Token('AAVE').address)

        self.assertTrue(nt != Token(address=Token('AAVE').address))
        self.assertTrue(nt != Token(symbol='AAVE'))
        self.assertTrue(nt != Token('AAVE'))
        self.assertTrue(nt != Token(Token('AAVE').address))

    def test_creation(self):
        a1 = Account(address='0xad529dabbd6201545ce9aac300b868f2443382b9')
        a2 = Account('0xad529dabbd6201545ce9aac300b868f2443382b9')
        a3 = Account({'address': '0xad529dabbd6201545ce9aac300b868f2443382b9'})
        self.assertTrue(a1.address == a2.address)
        self.assertTrue(a1.address == a3.address)

        c1 = Contract(address='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
        c2 = Contract('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
        c3 = Contract(
            {'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'})
        self.assertTrue(c1.address == c2.address)
        self.assertTrue(c1.address == c3.address)

        t1 = Token(symbol='CMK')
        t2 = Token('CMK')
        t3 = Token({'symbol': 'CMK'})
        self.assertTrue(t1.address == t2.address)
        self.assertTrue(t1.address == t3.address)

        t1 = Token(address='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
        t2 = Token('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
        t3 = Token({'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'})
        self.assertTrue(t1.address == t2.address)
        self.assertTrue(t1.address == t3.address)

        tca = transform_data_for_dto(
            {'token1': '0xad529dabbd6201545ce9aac300b868f2443382b9',
             'token2': {'address': '0xad529dabbd6201545ce9aac300b868f2443382b9'},
             'token3': 'CMK',
             'token4': {'symbol': 'CMK'},
             'contract1': '0xad529dabbd6201545ce9aac300b868f2443382b9',
             'contract2': {'address': '0xad529dabbd6201545ce9aac300b868f2443382b9'},
             'account1': '0xad529dabbd6201545ce9aac300b868f2443382b9',
             'account2': {'address': '0xad529dabbd6201545ce9aac300b868f2443382b9'}
             }, TCA, '', '')

        self.assertTrue(tca.token1.address ==  # type: ignore
                        tca.token2.address)  # type: ignore
        self.assertTrue(tca.token3.address ==  # type: ignore
                        tca.token4.address)  # type: ignore
        self.assertTrue(tca.contract1.address ==  # type: ignore
                        tca.contract2.address)  # type: ignore
        self.assertTrue(tca.account1.address ==  # type: ignore
                        tca.account2.address)  # type: ignore

    def test_scan_token_for_all_chains(self):
        with self.assertRaises(ModelBaseError):
            Token()

        with self.assertRaises(ModelBaseError):
            Token(symbol="INVALID_SYMBOL")

        for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items():
            chain_has_native_token = False
            symbols_set = set()
            addresses_set = set()
            names_set = set()

            for token_symbol, token_meta in chain_tokens.items():
                if 'is_native_token' in token_meta and token_meta['is_native_token']:
                    if chain_has_native_token:
                        raise Exception(
                            f'There are >1 native token on {chain_id=}')

                    chain_has_native_token = True

                try:
                    try:
                        self.assertEqual(token_symbol, token_meta['symbol'])
                    except AssertionError:
                        passed = False
                        if chain_id == Network.Mainnet:
                            passed = token_symbol in ['UST (Wormhole)',
                                                      'wLUNA',
                                                      'LUNA (Wormhole)',
                                                      'GreenMetaverseToken']
                        elif chain_id == Network.ArbitrumOne:
                            passed = token_symbol in ['USDC.e']

                        if not passed:
                            print(f'{chain_id=}', token_symbol, token_meta['symbol'])
                            raise

                    self.assertTrue('symbol' in token_meta)
                    self.assertTrue('decimals' in token_meta)
                    self.assertTrue('name' in token_meta)
                    self.assertTrue('address' in token_meta)
                    try:
                        self.assertTrue(token_meta['address'] == Address(
                            token_meta['address']))
                    except AssertionError:
                        print(('Diff', token_meta['address'], Address(
                            token_meta['address'])))
                        raise

                    try:
                        self.assertTrue(
                            token_meta['symbol'] not in symbols_set)
                    except AssertionError:
                        passed = False
                        if chain_id == Network.Mainnet:
                            passed = token_meta['symbol'] in [
                                'UST', 'GMT', 'LUNA']
                        elif chain_id == Network.ArbitrumOne:
                            passed = token_symbol in ['USDC']

                        if not passed:
                            print(f'{chain_id=}', token_meta['symbol'], symbols_set)
                            raise

                    try:
                        self.assertTrue(token_meta['name'] not in names_set)
                    except AssertionError:
                        passed = False
                        if chain_id == Network.Mainnet:
                            passed = token_meta['name'] in ['UST']
                        elif chain_id == Network.Avalanche:
                            passed = token_meta['address'] in [
                                '0x152b9d0fdc40c096757f570a51e494bd4b943e50',
                                '0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664',
                                '0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab']
                        elif chain_id == Network.BSC:
                            passed = token_meta['name'] in ['Catcoin', 'Carbon', 'GameFi', 'SafeMoon', 'SafeMars']

                        if not passed:
                            print(f'{chain_id=}',
                                  token_meta['name'], names_set)
                            raise

                    self.assertTrue(token_meta['address'] not in addresses_set)
                    addresses_set.add(token_meta['address'])
                    names_set.add(token_meta['name'])
                    symbols_set.add(token_meta['symbol'])
                except:
                    print(token_meta)
                    raise

            if not chain_has_native_token:
                if chain_id in [Network.Mainnet,  Network.BSC, Network.Polygon, Network.ArbitrumOne]:
                    raise Exception(f'There is no native token on {chain_id}')

        for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_ADDRESS.items():
            chain_has_native_token = False
            symbols_set = set()
            addresses_set = set()
            names_set = set()
            for token_address, token_meta in chain_tokens.items():
                if 'is_native_token' in token_meta and token_meta['is_native_token']:
                    if chain_has_native_token:
                        raise Exception(
                            f'There are >1 native token on {chain_id=}')

                    chain_has_native_token = True
                try:
                    self.assertEqual(token_address, token_meta['address'])
                    self.assertTrue('symbol' in token_meta)
                    self.assertTrue('decimals' in token_meta)
                    self.assertTrue('name' in token_meta)
                    self.assertTrue('address' in token_meta)
                    self.assertTrue(token_meta['address'] == Address(
                        token_meta['address']))

                    try:
                        self.assertTrue(
                            token_meta['symbol'] not in symbols_set)
                    except AssertionError:
                        passed = False
                        if chain_id == Network.Mainnet:
                            passed = token_meta['symbol'] in [
                                'GMT', 'UST', 'LUNA']
                        elif chain_id == Network.ArbitrumOne:
                            passed = token_meta['symbol'] in ['USDC']

                        if not passed:
                            print(f'{chain_id=}', token_meta['symbol'], symbols_set)
                            raise

                    try:
                        self.assertTrue(token_meta['name'] not in names_set)
                    except AssertionError:
                        passed = False
                        if chain_id == Network.Avalanche:
                            passed = token_meta['address'] in [
                                '0x152b9d0fdc40c096757f570a51e494bd4b943e50',
                                '0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664',
                                '0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab']
                        elif chain_id == Network.BSC:
                            passed = token_meta['name'] in ['Catcoin', 'Carbon', 'GameFi', 'SafeMoon', 'SafeMars']

                        if not passed:
                            print(f'{chain_id=}', token_meta['name'], names_set)
                            raise

                    self.assertTrue(token_meta['address'] not in addresses_set)
                    addresses_set.add(token_meta['address'])
                    names_set.add(token_meta['name'])
                    symbols_set.add(token_meta['symbol'])
                except:
                    print(token_meta)
                    raise

            if not chain_has_native_token:
                raise Exception('There is no native token on {chain_id}')

    def test_token_on_mainnet(self):
        token = Token(symbol="CMK")
        print(f'Testing on {token.instance.w3.eth.default_block}')

        self.assertEqual(token.symbol, "CMK")
        self.assertEqual(token.address,
                         "0x68CFb82Eacb9f198d508B514d898a403c449533E")
        self.assertEqual(token.decimals, 18)
        self.assertEqual(token.total_supply, 100_000_000 * 10**18)

        for native_token in (
            NativeToken(),
            NativeToken(symbol='ETH'),
            NativeToken(
                symbol='ETH', address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            NativeToken(
                symbol='ETH', address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeee'),
            NativeToken(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeee'),
            NativeToken(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            Token(symbol="ETH", address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeeeeee'),
            Token(symbol="ETH"),
            Token(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeeeeee')
        ):
            self.assertEqual(native_token.symbol, "ETH")
            self.assertEqual(native_token.name, "Ethereum")
            self.assertEqual(native_token.decimals, 18)

    def test_token_on_chains(self):
        context = credmark.cmf.model.ModelContext.current_context()
        for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items():
            if chain_id in [Network.BSC, Network.Polygon, Network.Mainnet]:
                block_number = 29727653 if chain_id == Network.BSC else None
                with context.fork(chain_id=chain_id, block_number=block_number) as cc:
                    print(f'Test tokens on chain: {chain_id} @ {cc.block_number}')
                    for token_n, (token_symbol, token_meta) in enumerate(chain_tokens.items()):
                        if chain_id == Network.Mainnet:
                            token = Token(token_symbol)
                        else:
                            token = Token(token_symbol).as_erc20(set_loaded=True)
                        self.assertEqual(token.symbol, token_meta['symbol'])
                        self.assertEqual(token.name, token_meta['name'])
                        self.assertEqual(token.address, token_meta['address'])
                        self.assertEqual(token.decimals, token_meta['decimals'])
                        print(f'{token_n+1}/{len(chain_tokens)}: {token_symbol} {token_meta["address"]}', flush=True)


if __name__ == '__main__':
    unittest.main()
