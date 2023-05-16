```sql
set tokenaddress = (lower('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'));

set univ2_controller = '0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f';
set sushi_controller = '0xc0aee478e3658e2610c5f7a4a2e1777ce9e4f2ac';


SELECT block_number AS "block_number",to_char(evt_pair) AS "evt_pair" FROM (SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,transaction_hash AS transaction_hash,signature AS signature,get_path(decoded, 'data:token0') AS evt_token0,get_path(decoded, 'data:token1') AS evt_token1,get_path(decoded, 'data:pair') AS evt_pair,get_path(decoded, 'data:_0') AS evt__0 FROM ETHEREUM.decoded.events WHERE block_number <= 15884623 AND ( name = 'PairCreated' and contract_address = $univ2_controller ) ORDER BY block_number) WHERE block_number <= 15884623 AND ( (evt_token0 = $tokenaddress and evt_token1 = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48') or (evt_token0 = $tokenaddress and evt_token1 = '0x6b175474e89094c44da98b954eedeac495271d0f') or (evt_token0 = $tokenaddress and evt_token1 = '0xdac17f958d2ee523a2206206994597c13d831ec7') or (evt_token0 = $tokenaddress and evt_token1 = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2') or
(evt_token0 = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' and evt_token1 = $tokenaddress) or (evt_token0 = '0x6b175474e89094c44da98b954eedeac495271d0f' and evt_token1 = $tokenaddress) or (evt_token0 = '0xdac17f958d2ee523a2206206994597c13d831ec7' and evt_token1 = $tokenaddress) or (evt_token0 = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2' and evt_token1 = $tokenaddress) ) ORDER BY block_number LIMIT 5000 OFFSET 0;


set burnsig = 'Burn(address,uint256,uint256,address)';
set mintsig = 'Mint(address,uint256,uint256)';
set swapsig = 'Swap(address,uint256,uint256,uint256,uint256,address)';
set paircreatedsig = 'PairCreated(address,address,address,uint256)';



// sum() over (partition by contract_address order by block_number asc) as liquidity0,
select
    contract_address,
    block_number,
    token0,
    token1,
    sum(token0amount) as token0amount_block,
    sum(token1amount) as token1amount_block,
    sum(token0amount_block) over (partition by contract_address order by block_number asc) as liquidity0,
    sum(token1amount_block) over (partition by contract_address order by block_number asc) as liquidity1
from (
    select
        contract_address,
        block_number,
        token0,
        token1,
        iff(
        signature=$mintsig,
        decoded:data:amount0,
        iff(
            signature = $burnsig,
            decoded:data:amount0 * -1,
            decoded:data:amount0In - decoded:data:amount0Out
            )
        ) as token0amount,
        iff(
            signature=$mintsig,
            decoded:data:amount1,
            iff(
                signature = $burnsig,
                decoded:data:amount1 * -1,
                decoded:data:amount1In - decoded:data:amount1Out
                )
        ) as token1amount
    from (
        select distinct events.*, pair, token0, token1 from ethereum.decoded.events events
        inner join (
            -- GET THE POOLS FOR THE TOKEN
            select
                decoded:data:pair as pair,
                decoded:data:token0 as token0,
                decoded:data:token1 as token1
            from ethereum.decoded.events
                where signature = $paircreatedsig
                and (
                    decoded:data:token0 = $tokenaddress
                    or decoded:data:token1 = $tokenaddress
                ) and
                contract_address = $univ2_controller
        ) pairs on events.contract_address = pairs.pair
        where events.signature in($burnsig, $mintsig, $swapsig)
    )
)
where block_number <= 11076354
group by contract_address, block_number, token0, token1
order by block_number asc;
```