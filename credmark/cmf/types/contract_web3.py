# from web3._utils.abi import get_constructor_abi, merge_args_and_kwargs
from web3._utils.events import get_event_data
from web3._utils.filters import construct_event_filter_params

# from web3._utils.contracts import encode_abi


def fetch_events(
        event,
        argument_filters=None,
        from_block=None,
        to_block=None,
        address=None,
        topics=None):
    """Get events using eth_getLogs API.

    This is a stateless method, as opposite to createFilter and works with
    stateless nodes like QuikNode and Infura.

    :param event: Event instance from your contract.events
    :param argument_filters:
    :param from_block: Start block. Use 0 for all history/
    :param to_block: Fetch events until this contract
    :param address:
    :param topics:
    :return:
    """

    if from_block is None:
        raise TypeError("Missing mandatory keyword argument to getLogs: from_Block")

    abi = event._get_event_abi()  # pylint:disable=protected-access
    abi_codec = event.web3.codec

    # Set up any indexed event filters if needed
    argument_filters = {}
    _filters = dict(**argument_filters)

    _data_filter_set, event_filter_params = construct_event_filter_params(
        abi,
        abi_codec,
        contract_address=event.address,
        argument_filters=_filters,
        fromBlock=from_block,
        toBlock=to_block,
        address=address,
        topics=topics,
    )

    # Call node over JSON-RPC API
    logs = event.web3.eth.getLogs(event_filter_params)

    # Convert raw binary event data to easily manipulable Python objects
    for entry in logs:
        data = {**get_event_data(abi_codec, abi, entry)}
        args = data['args']
        yield {**data, **args}  # type: ignore
