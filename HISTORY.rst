.. :changelog:

History
-------

0.8.26 [2022-06-30]
* Added checking of latest version tag in github (#125)
* Add client property support for model-api (#127)
* Creation of Currency DTO with string or kwargs (#129)
* Fix depth when calling api model run
* Updated max depth to 25

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
