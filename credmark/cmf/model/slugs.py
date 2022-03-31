
class CoreModels:
    """
    Slugs of core Credmark models that are used by some
    cmf type classes and utils in the framework.
    """

    token_price = 'token.price'
    """
    Get price for a token
    """
    contract_metadata = 'contract.metadata'
    """
    Lookup a contract by metadata
    """

    latest_block_number = 'rpc.get-latest-blocknumber'
    """
    Get latest block number
    """

    rpc_block_range_time_start_end_interval = 'rpc.get-block-range-time-start-end-interval'
    """
    Get a range of blocks by start and end time and interval
    """
    rpc_block_range_time_window_interval = 'rpc.get-block-range-time-window-interval'
    """
    Get a range of blocks by time window and interval
    """
    rpc_block_range_block_start_end_interval = 'rpc.get-block-range-block-start-end-interval'
    """
    Get a range of blocks by start and end block number and interval
    """
    rpc_block_range_block_window_interval = 'rpc.get-block-range-block-window-interval'
    """
    Get a range of blocks by block number window and interval
    """
