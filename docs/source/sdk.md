# Credmark SDK (Python)

A client library for accessing Credmark Gateway

## Installation

Install using pip:

```bash
pip install credmark
```

## Usage

First, create an instance of `Credmark` client. In order to access the API, you will need an API key. Information about getting a key is available in our [API setup guide](https://docs.credmark.com/api-how-to-guide/).

```python
from credmark import Credmark

client = Credmark(api_key="<Your API Key>")
```

Alternatively you can also set the API key in the OS environment and the client will automatically pick from it.

```bash
export CREDMARK_API_KEY=<Your API Key>
```

```python
from credmark import Credmark

client = Credmark() # It reads the api key from CREDMARK_API_KEY env var
```

Now call your endpoint by tag and use your models:

```python
metadata = client.token_api.get_token_metadata(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")

print(metadata)
# TokenMetadataResponse(chain_id=1, block_number=17044112, block_timestamp=1681459199, token_address='0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9', name='Aave Token', symbol='AAVE', decimals=18)
```

Or do the same thing with an async version:

```python
import asyncio

async def get_metadata():
    metadata = await client.token_api.get_token_metadata_async(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")
    print(metadata)
    # TokenMetadataResponse(chain_id=1, block_number=17044112, block_timestamp=1681459199, token_address='0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9', name='Aave Token', symbol='AAVE', decimals=18)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_metadata())
loop.close()
```

## Examples

### 1. DeFi API - Run models

Get all Uniswap V3 pools for USDC on Ethereum Mainnet:

```python
from credmark.models import RunModelDto

result = client.defi_api.run_model(
    json_body=RunModelDto(
        chain_id=1, 
        block_number="latest", 
        slug="uniswap-v3.get-pools", 
        input={"symbol": "USDC"}
    ),
)

print(result.chain_id, result.block_number)
# 1 17563869
print(result.slug, result.version)
# uniswap-v3.get-pools 0.1
print(result.output)
# {'contracts': [{'address': '0x5777d92f208679db4b9778590fa3cab3ac9e2168'}, {'address': '0x6c6bc977e13df9b0de53b251522280bb72383700'}, {'address': '0xa63b490aa077f541c9d64bfc1cc0db2a752157b5'}, {'address': '0x6958686b6348c3d6d5f2dca3106a5c09c156873a'}, {'address': '0x3416cf6c708da44db2624d63ea0aaef7113527c6'}, {'address': '0x7858e59e0c01ea06df3af3d20ac7b0003275d4bf'}, {'address': '0xee4cf3b78a74affa38c6a926282bcd8b5952818d'}, {'address': '0xbb256c2f1b677e27118b0345fd2b3894d2e6d487'}]}
```

### 2. Portfolio API

Get all positions, i.e. tokens and balances for a wallet

```python
result = client.portfolio_api.get_positions(1, ["0x5291fBB0ee9F51225f0928Ff6a83108c86327636"])

print(result.chain_id, result.block_number)
# 1 17567721
print(result.positions)
# [Position(token_address='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', balance=2.169356), Position(token_address='0xdac17f958d2ee523a2206206994597c13d831ec7', balance=479.354369)]
```

### 3. Token API

Get price of AAVE token (0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9)

```python
result = client.token_api.get_token_price(1, "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9")

print(result.chain_id, result.block_number)
# 1 17567740
print(result.price, result.src, result.quote_address)
# 64.599481 cex 0x0000000000000000000000000000000000000348
# 0x0000000000000000000000000000000000000348 => USD address
```

## Handling Errors

Each method can raise:

- errors.CredmarkError: If the server returns a non 2xx status code.
- httpx.TimeoutException: If the request takes longer than Client.timeout.

```python
from httpx import TimeoutException
from credmark.errors import CredmarkError

try:
    metadata = client.token_api.get_token_metadata(1, "WRONG TOKEN ADDRESS")
except CredmarkError as e:
    print(e.status_code)
    # 400
    print(e.parsed)
    # TokenErrorResponse(status_code=400, error='Bad Request', message=['Invalid token address'])
    print(str(e.content, "UTF-8"))
    # {"statusCode":400,"message":["Invalid token address"],"error":"Bad Request"}
except TimeoutException:
    print('timeout occurred')
```

## Available APIs

- [Token API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/TokenAPI.md)
- [Portfolio API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/PortfolioApi.md)
- [DeFi API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/DeFiAPI.md)
- [Utilities API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/UtilitiesAPI.md)

## Things to know

1. Every path/method combo has four functions:
    1. default: Blocking request that returns parsed data (if successful) or `None`
    2. `async`: Like default but async instead of blocking

2. All path/query params, and bodies become method arguments.

## Advanced Usage

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken", 
    verify_ssl=False
)
```

There are more settings on the generated `Credmark` class which let you control more runtime behavior, check out the docstring on that class for more info.