.. :changelog:

History
-------

0.8.148 [2024-08-28]
* fix: unscale by token decimals

0.8.147 [2024-08-28]
* fix: add raw_amount column to token balance

0.8.146 [2024-08-12]
* fix: enable ledger db for more chains

0.8.145 [2024-06-18]
* fix: bump up pydantic for python 3.12.4
* fix: token transfer table columns

0.8.144 [2024-06-11]
* migrate: ledger columns to new model runner

0.8.143 [2024-03-14]
* feat: analytics mode in query input
* feat: multiple fallback functions for web3 batch

0.8.142 [2024-03-12]
* feat: include requester in context
* feat: computed value in position
* feat: PortfolioBuilder

0.8.141 [2024-02-03]
* feat: block number from date
* fix: model api http error logs

0.8.140 [2024-01-29]
* fix: ledger table return type
* fix: docs generation
* fix: line length linter settings

0.8.139 [2024-01-16]
* fix: custom ABI loading for proxy contracts

0.8.138 [2023-12-28]
* fix: event contract ledger for proxy contracts

0.8.137 [2023-12-27]
* fix: support for python 3.12

0.8.136 [2023-11-15]
* feat: add support to ERC20 ABI for symbols of bytes32 type

0.8.135 [2023-11-07]
* fix: disable polygon ledger

0.8.134 [2023-10-16]
* fix: abi loading

0.8.133 [2023-10-04]
* refactor: enhance multicall with fallback to rpc batch
* fix: unwrap and type hinting in multicall methods

0.8.132 [2023-08-24]
* feat: multicall: add unwrap() and run_sequence() to run multicall before its deployment

0.8.131 [2023-08-22]
* feat: multicall

0.8.130 [2023-08-10]
* fix: remove is_just from Maybe

0.8.129 [2023-08-01]
* fix: cache web3 chain_id

0.8.128 [2023-07-28]
* feat: check incremental model result for valid block range in [from_block, context.block_number]
* fix: handle change in error code from runner api

0.8.127 [2023-07-27]
* fix: contract instance type
* fix: balance_of_scaled

0.8.126 [2023-07-22]
* fix: proxy address in contract events / functions

0.8.125 [2023-07-13, 2023-07-22]
* fix: multi-chain token metadata
* feat: add raw_abi for ABI events and functions
* fix: type cast from linting

0.8.124 [2023-07-10]
* docs: update immutableModel and IncrementalModel
* tokens: fix ETH and BTC loading in Polygon
* query: ETL for self-destruct contracts

0.8.123 [2023-07-07]
* upgrade to Python 3.11 and web3-py 6.5.0

0.8.122 [2023-07-06]
* fix: support for from_block_number in credmark-dev

0.8.121 [2023-07-06]
* fix: add native tokens to arb/polygon
* feat: add disable_cache
* chore: bump grpcio from 1.43.0 to 1.53.0

0.8.120 [2023-07-04]
* feat: cache policy
* feat: incremental model
* feat: immutable model
* cleanup: removed lookup cache result

0.8.119 [2023-06-21]
* cleanup: portfolio and position DTOs

0.8.118 [2023-06-19]
* feat: enable ledger for polygon

0.8.117 [2023-06-15]
* chore: update token list

0.8.116 [2023-06-11]
* feat: support polygon ledger
* feat: add .has_dex_price() to network

0.8.115 [2023-06-03]
* fix: disable BSC ledger

0.8.114 [2023-06-02]
* feat: add support for async web3 in fetch_events

0.8.113 [2023-05-29]
* feat: support for dry run and test model selection in test_all_models function
* feat: updated token data for BSC and Polygon networks
* chore: clean up cache object

0.8.112 [2023-05-26]
* feat: enable ledger for BSC

0.8.111 [2023-05-26]
* feat: add skip to test-all
* feat: add BSC tokens to fungible token data (BTCB and WBNB, etc.)
* fix: update Contract instance when chain_id changes
* fix: correct name of USD Coin in Polygon token data
* fix: update Token cache to include chain_id

0.8.110 [2023-05-25]
* fix: remove context enter remnants
* fix: fail on fork to block > context.block_number

0.8.109 [2023-05-25]
* feat: replace context enter with fork context
* fix: network enum enhancements
* fix: allow BlockNumber to be > context.block_number

0.8.108 [2023-05-22]
* fix: improve test-all and test cases

0.8.107 [2023-05-21]
* feat: add web3 async

0.8.106 [2023-05-18]
* feat: test-all improvements

0.8.105 [2023-05-16]
* chore: ruff-ed

0.8.104 [2023-05-15]
* fix: move get_dt() and get_block() to BlockNumber object
* feat: enrich command-line for create, help and test-all

0.8.103 [2023-05-12]
* feat: support of contract ledger join
* feat: add as_integer() for ColumnField

0.8.102 [2023-05-08]
* feat: enrich context.models object with list() and get_result()
* feat: enable context.enter() for Contract and Token web3 calls
* chore: turn off test_ledger.py for now

0.8.101 [2023-05-04]
* feat: enable multi chain in token

0.8.100 [2023-05-01]
* fix: exclude group by columns if already in aggregates
* opt: remove sqlitedict (added from 0.8.33)

0.8.99 [2023-04-28]
* chore: lint with ruff

0.8.98 [2023-04-26]
* feat: add input to call stack

0.8.97 [2023-04-25]
* fix: network to str

0.8.96 [2023-04-25]
* fix: ipython context

0.8.95 [2023-04-25]
* feat: add network dict

.8.95 [2023-04-25]
* feat: add network dict

0.8.94 [2023-04-25]
* feat: add originator to ledger model input

0.8.93 [2023-04-22]
* feat: add context.ledger.describe()

0.8.92 [2023-04-22]
* feat: add context.ledger.tables() and context.ledger.table()

0.8.91 [2023-04-22]
* fix: table join

0.8.90 [2023-04-21]
* fix: contract lookup error handling

0.8.89 [2023-04-21]
* feat: expose original_input in context

0.8.88 [2023-04-20]
* fix: by range event fetching

0.8.87 [2023-04-20]
* lint: clean up for ledger

0.8.86 [2023-04-19]
* refactor: redundant block sampling

0.8.85 [2023-04-18]
* chore: make ipython loader robust to environment variables

0.8.84 [2023-04-17]
* chore: split token list to separate file per chainId
* chore: support new DB
* chore: new create_context
* feat: fetch_events with by_range

0.8.83 [2023-04-04]
* feat: added public nodes
* feat: added public api key

0.8.82 [2023-03-27]
* fix: fix ipython under non-Ethereum networks

0.8.81 [2023-03-18]
* fix: fetch_event for multiple events with same name

0.8.80 [2023-03-14]
* fix web3 for avalanche

0.8.79 [2023-03-14]
* add arbitrum one token data
* add optimism token data
* add avalanche token data
* add fantom token data
* fix polygon and bsc native token data

0.8.78 [2023-03-12]
* support ERC1967Proxy

0.8.77 [2023-03-02]
* change `force` to `set_loaded` for `set_abi()` and `as_erc20()`
* support arbitrum one and optimism

0.8.76 [2023-03-01]
* add network for Optimism, Arbitrum One

0.8.75 [2023-02-27]
* add staging gateway address

0.8.74 [2023-02-26]
* make as_erc20() quicker with force=True. Direct injection of ERC20 ABI.

0.8.73 [2023-02-03]
* fix ledger model setup
* fix typos in code and doc

0.8.72 [2023-01-24]
* fix console goto_block issue

0.8.71 [2023-01-10]
* enable event argument_filters

0.8.70 [2022-12-23]
* refactor: column field helper methods in ledger
* feat: disable/override cache in context
* fix: context safe to use in concurrent code

0.8.69 [2022-12-21]
* feat: add set to json encode

0.8.68 [2022-12-20]
* fix: add missing columns in ledger tables

0.8.67 [2022-12-19]
* fix: refine console startup error message

0.8.66 [2022-12-15]
* fix: fetch error from cache

0.8.65 [2022-12-12]
* feat: improve ipython setup

0.8.64 [2022-12-05]
* fix: set use_local_model by default in ipython

0.8.63 [2022-12-05]
* feat: add dto PositionWithPrice and PortfolioWithPrice

0.8.62 [2022-12-05]
* fix: add list of non-deterministic models to cache
* feat: get latest block for non-mainnet chains
* feat: records can add fix_int_columns to convert to int from string

0.8.61 [2022-12-01]
* feat: support POA network in web3

0.8.60 [2022-11-30]
* feat: add polygon network

0.8.59 [2022-11-29]
* feat: provide override to fetch events for proxy contracts

0.8.58 [2022-11-24]
* feat: add examples to DTO

0.8.57 [2022-11-24]
* feat: add merge to Portfolio
* feat: json encoder for numpy types
* feat: use encoder for all model api request

0.8.56 [2022-11-18]
* feat: as_erc20 to Token

0.8.55 [2022-11-16]
* feat: portfolio/position DTO update

0.8.54 [2022-11-12]
* more fix: support more proxies and tokens

0.8.53 [2022-11-9]
* more fix: support more proxies and tokens
* fix: columns can be [] or None in ledger query

0.8.52 [2022-11-8]
* fix: support more proxies and tokens

0.8.51 [2022-10-29]
* fix: native token initialization in token

0.8.50 [2022-10-21]
* feat: fix contract ledger model
* feat: create_cmf() with template
* feat: add IDLE and INDEX tokens

0.8.49 [2022-10-21]
* feat: add `as_` and `join`` to ledger model query

0.8.48 [2022-10-09]
* fix: price model used in portfolio/position

0.8.47 [2022-10-03]
* fix: decoded table names "unnamed variable" to _0, _1, ...

0.8.46 [2022-09-28]
* fix: pandas starts use uint64

0.8.45 [2022-09-15]
* fix: token list: symbol and name.
* feat: add ne() to ColumnField

0.8.44 [2022-09-15]
* feat: added list of ERC-20 tokens

0.8.43 [2022-09-14]
* chore: extend model api timeout to 1800 seconds

0.8.42 [2022-09-11]
* feat: support CErc20Delegator proxy

0.8.41 [2022-09-11]
* feat: new Records type to hold list of tuples and list of field names.

0.8.40 [2022-09-09]
* various fixes
- chore: fix type in Contract
- fix: override abi missing when set_abi()
- chore: update on error to raise...from
- feat: add PriceWithQuote

0.8.39 [2022-09-06]
* feat: upgrade to new database setup (L2)
- remove table TokenBalance
- rename Event/Functions table column names (breaking)
- Event/Function-specific columns are prefixed with `EVT_` or `FN_`
* chore: Some ColumnField methods to have `str_lower` as a bool to quote and lower case the string

0.8.38 [2022-09-01]
* chore: fix cache storage the same for both local and remote

0.8.37 [2022-09-01]
* chore: store dependencies in cache

0.8.36 [2022-08-31]
* context.reload_model(do_clear:bool): add option for clear cache for reload_model
* cache.clear(do_clear:bool): add clear for cache
* EIP-897 proxy implementation


0.8.35 [2022-08-25]
* cache.get() returns key, context.models() takes all DTO and kwargs, improve console, set cache to autocommit (#156)

0.8.34 [2022-08-23]
* Cache is changed to an instance variable for EngineModelContext (#155)

0.8.33 [2022-08-14]
* Improve local cache with Sqlitedict (#152), allow multiple readonly base cache (#153) and type annotation (#154)
* Create function for ipython extension (#152)

0.8.32 [2022-08-10]
* Make models call available to Account/Contract/Token (#150)
* Add api model cache (#151)

0.8.31 [2022-08-08]
* Various Fix (#149)
- Reset local_model_list during initialization.
- Address can be initialized with int and hex str with less than 40+2 length (2 from '0x')
- Fix for proxy address lookup for returning less 40 long address
- Decouple with context from utilities
- Fix address lookup
- Add helper to ColumnField
- Ledger model update: force all VARIANT column to char type for contract ledger query
- Ledger model update: add bigint_cols to load those columns as character and later convert to Int64/int
- Expand args in event_log in contract.fetch_events()
- Add wrapper to Token
- Add local model cache

0.8.30 [2022-07-25]
* re-org imports (#145)
* enhancement and fix (#148)
- Some (ADT) enhancement
- Use json_dump for input/output serialization
- ipython extension: use local_ns
- add fetch_events() to contract object
- enable local run mode for run_model()
- sort imports


0.8.29 [2022-07-18]
* Add ipython extension (#141)
* Add network identifier, re-organized DTO imports, enrich Maybe (#142)
* Creation of Token/Contract/Account DTO with string (#143)

0.8.28 [2022-07-12]
* Ledger utility update (#92)

0.8.27 [2022-07-12]
* Fix for parallel testing when stdout/stderr are not available (#136)
* Add ADT types of Maybe/Some (#137, #138)

0.8.26 [2022-06-30]
* Added checking of latest version tag in github (#125)
* Add client property support for model-api (#127)
* Creation of Currency DTO with string or kwargs (#129, #132)
* Fix depth when calling api model run (#134)
* Updated max depth to 25 (#134)

0.8.25 [2022-06-26]
* Added support for using no local models (#108)
* add set_abi to contract (#109) and balance_of/balance_of_scaled to Token/NativeToken (#110)
* Price DTO update (#111)
* Add EUROC token symbol (#112)
* Historical utility enhancement (#113)
* Add block_number to contract.meta (#114) and optimized loading / error handling / proxy loading (#115, #116, and #118)
* Doc fix for removal of smartquotes (#117)
* Add --output argument to run subcommand (#119)
* Added category and subcategory to model metadata (#120)

0.8.24 [2022-06-14]
* Updated version support to use versioneer.

0.8.23 [2022-06-13]
* Jupyter notebook support
* Currency as interface for FiatCurrency and Token
* DTOs for compose models and local compose models
* Contract ABI class
* Primitive DTO types: IntDTO, FloatDTO, StrDTO
* Support for credmark-dev use-local-models flag "-" for no locals
* Increase API run request timeout

0.8.22 [2022-05-26]
* Support for web3 websocket urls
* Contract ledger event txn hash field name fix

0.8.21 [2022-05-23]
* Serialize datetime and numpy and pandas data structures to json
* Pandas types conversion helpers
* Improve types and type hints
* Fix to load token ERC20 properties in Token.info() method

0.8.20 [2022-05-14]
* Changed manifest displayName field casing
* Added get_value to Portfolio and Position DTOs

0.8.19 [2022-05-13]
* credmark-dev create command

0.8.18 [2022-05-13]
* Model console improvements
* Added return_type arg to context.models model run

0.8.17 [2022-05-12]
* Model console

0.8.16 [2022-05-10]
* Model mock generation

0.8.15 [2022-05-09]
* chainId and blockNumber in model run results

0.8.14 [2022-05-09]
* Unit testing support

0.8.13 [2022-05-03]
* Contract ledger queries

0.0.1 [2022-02-25]
* First public release
