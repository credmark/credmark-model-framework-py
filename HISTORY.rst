.. :changelog:

History
-------

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
* feat: add as_ and join to ledger model query

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
* Improve local cache with Sqllitedict (#152), allow multiple readonly base cache (#153) and type annotation (#154)
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
* Creation of Token/Contract/Accoint DTO with string (#143)

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
* Serialize datetimes and numpy and pandas datastructures to json
* Pandas types conversion helpers
* Improve types and typehints
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

* 0.8.13 [2022-05-03]
Contract ledger queries

0.0.1 [2022-02-25]
* First public release
