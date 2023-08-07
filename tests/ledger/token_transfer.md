ERC20 transfer from logs

```sql
select
count(distinct block_number, log_index, transaction_index, address, data, topics),
max(block_number)
from ethereum.core.logs
where
address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
and STARTSWITH(topics,'0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef,')
-- and block_number <= 11055450
limit 1;
```


```sql
with double_entry_book as (
    -- debits
    select to_address as address, value as value, block_timestamp
    from ethereum.traces
    where to_address is not null
    and status = 1
    and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
    union all
    -- credits
    select from_address as address, -value as value, block_timestamp
    from ethereum.traces
    where from_address is not null
    and status = 1
    and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
    union all
    -- transaction fees debits
    select miner as address, sum(cast(gas as numeric) * cast(gas_price as numeric)) as value, block_timestamp
    from ethereum.transactions as transactions
    join ethereum.blocks as blocks on blocks.number = transactions.block_number
    group by blocks.miner, block_timestamp
    union all
    -- transaction fees credits
    select from_address as address, -(cast(gas as numeric) * cast(gas_price as numeric)) as value, block_timestamp
    from ethereum.transactions
),
balances_by_address as (
    select address, sum(value) as balance
    from double_entry_book
    group by address
),
balances_total AS (
  SELECT SUM(value) AS total_balance
  FROM double_entry_book
),
balances_by_address_top_million AS (
  SELECT address, balance
  FROM balances_by_address
  ORDER BY balance DESC, address
  LIMIT 1000000 OFFSET 0
),
cumm_balances_by_address_top_million AS (
  SELECT address, balance, SUM(balance) OVER(ORDER BY balance DESC, address ASC) AS cumm_balance
  FROM balances_by_address_top_million
)
SELECT address, balance, cumm_balance, (cumm_balance / total_balance) AS perc_total
FROM cumm_balances_by_address_top_million
INNER JOIN balances_total ON TRUE
where address = lower('0x109B3C39d675A2FF16354E116d080B94d238a7c9')
ORDER BY perc_total ASC
;
```