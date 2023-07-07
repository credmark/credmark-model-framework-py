# pylint:disable=too-many-locals, too-many-arguments, invalid-name


import asyncio
import math
from typing import Optional, Sequence, Union, cast

from web3 import AsyncWeb3, Web3
from web3._utils.events import get_event_data
from web3._utils.filters import construct_event_filter_params
from web3.contract.base_contract import BaseContractEvent
from web3.types import ABIEvent, FilterParams
from web3.utils.abi import get_abi_input_names

# from web3._utils.abi import get_constructor_abi, merge_args_and_kwargs
# from web3._utils.contracts import encode_abi


async def fetch_events_async(async_web3: AsyncWeb3,
                             event_filter_params: FilterParams,
                             from_block: int,
                             to_block: int,
                             num_of_chunk: int = 10):
    """
    events = asyncio.run(fetch_events_async(async_web3, event_filter_params,
                         from_block, to_block, num_of_chunk))  # type: ignore
    """
    size_per_chunk = (to_block - from_block + 1) // num_of_chunk
    if size_per_chunk > 0:
        tasks = []
        for i in range(num_of_chunk):
            _from_block = from_block + i * size_per_chunk
            if i == num_of_chunk - 1:
                _to_block = to_block
            else:
                _to_block = _from_block + size_per_chunk - 1
            event_filter = event_filter_params.copy()
            event_filter['fromBlock'] = _from_block
            event_filter['toBlock'] = _to_block
            tasks.append(async_web3.eth.get_logs(event_filter))
    else:
        event_filter = event_filter_params.copy()
        event_filter['fromBlock'] = from_block
        event_filter['toBlock'] = to_block
        tasks = [async_web3.eth.get_logs(event_filter)]
    events = []
    for result in asyncio.as_completed(tasks):
        evts = await result
        events.extend(evts)
    return events


# pylint: disable=too-many-branches
def fetch_events(
        event: BaseContractEvent,
        argument_filters=None,
        from_block=None,
        to_block=None,
        address=None,
        topics=None,
        contract_address=None,
        argument_names: Optional[Sequence[str]] = None,
        by_range: Optional[int] = None,
        async_web3: Optional[AsyncWeb3] = None,
        async_worker: int = 10):
    """Get events using eth_getLogs API.

    This is a stateless method, as opposite to createFilter and works with
    stateless nodes like QuickNode and Infura.

    :param event: Event instance from your contract.events
    :param argument_filters:
    :param from_block: Start block. Use 0 for all history/
    :param to_block: Fetch events until this contract
    :param address:
    :param topics:
    :return:
    """

    if from_block is None:
        raise TypeError(
            "Missing mandatory keyword argument to getLogs: from_Block")

    w3: Union[Web3, AsyncWeb3] = event.w3
    if isinstance(w3, AsyncWeb3):
        raise TypeError(
            "Contract was initiailized with async_web3. fetch_events only support web3."
        )
    if to_block is None:
        to_block = w3.eth.block_number

    # TODO: existing code reports error with multiple events with same name, different input
    # abi = event._get_event_abi()  # pylint:disable=protected-access

    # TODO: Use manual filtering now: below code is adapted from web3
    # from web3._utils.contracts import find_matching_event_abi
    event_abis = [abi for abi in event.contract_abi
                  if 'name' in abi and
                  abi['name'] == event.event_name and
                  (argument_names is None or
                   set(get_abi_input_names(abi)) == set(argument_names))]
    if len(event_abis) > 1:
        raise ValueError(
            'Multiple events found with same name and argument names')
    event_abi = cast(ABIEvent, event_abis[0])

    abi_codec = w3.codec

    # Set up any indexed event filters if needed
    argument_filters = {} if argument_filters is None else argument_filters
    _filters = {**argument_filters}

    _data_filter_set, event_filter_params = construct_event_filter_params(
        event_abi,
        abi_codec,
        contract_address=event.address if contract_address is None else contract_address,
        argument_filters=_filters,
        fromBlock=from_block,
        toBlock=to_block,
        address=address,
        topics=topics,
    )

    if async_web3 is not None:
        events = asyncio.run(fetch_events_async(async_web3, event_filter_params,
                                                from_block, to_block, async_worker))  # type: ignore
        events = sorted(events, key=lambda x: (x.blockNumber, x.logIndex))
        for entry in events:
            data = {**get_event_data(abi_codec, event_abi, entry)}
            args = data['args']
            yield {**data, **args}  # type: ignore
    else:
        if by_range is None:
            # Call node over JSON-RPC API
            events = w3.eth.get_logs(event_filter_params)

            # Convert raw binary event data to easily manipulable Python objects
            for entry in events:
                data = {**get_event_data(abi_codec, event_abi, entry)}
                args = data['args']
                yield {**data, **args}  # type: ignore
        else:
            n_range_upper = int(math.ceil((int(to_block) - int(from_block) + 1) / by_range))

            for n_range in range(n_range_upper):
                _from_block = from_block + n_range * by_range
                if n_range == n_range_upper - 1:
                    _to_block = to_block
                else:
                    _to_block = _from_block + by_range - 1

                event_filter_params |= {'fromBlock': _from_block, 'toBlock': _to_block}

                # Call node over JSON-RPC API
                events = w3.eth.get_logs(event_filter_params)

                # Convert raw binary event data to easily manipulable Python objects
                for entry in events:
                    data = {**get_event_data(abi_codec, event_abi, entry)}
                    args = data['args']
                    yield {**data, **args}  # type: ignore
