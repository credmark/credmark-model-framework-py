## 1. Query Events.Transfer

```python
input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
with input.ledger.events.Transfer as ts:
        df = ts.select(aggregates=[(ts.EVT_FROM, 'evt_from'),
                                   (ts.EVT_TO, 'evt_to'),
                                   (ts.BLOCK_NUMBER, 'block_number'),
                                   (ts.TXN_HASH, 'hash')],
                        order_by=ts.BLOCK_NUMBER,
                        where=ts.EVT_FROM.eq(Address.null()),
                        limit=10).to_dataframe()
```

```typescript
EventData {
  alias: null,
  columns: [],
  joins: null,
  aggregates: [
    { expression: 'evt_from', asName: 'evt_from' },
    { expression: 'evt_to', asName: 'evt_to' },
    { expression: 'block_number', asName: 'block_number' },
    { expression: 'transaction_hash', asName: 'hash' }
  ],
  where: "evt_from = '0x0000000000000000000000000000000000000000'",
  groupBy: null,
  having: null,
  orderBy: 'block_number',
  limit: '10',
  offset: null,
  originator: 'console',
  eventName: 'Transfer',
  contractAddress: '0xed5af388653567af2f388e6224dc7c4b3241c544',
  l2_columns: [ 'evt_from', 'evt_to', 'evt_tokenId' ]
}
```

```sql
SELECT evt_from AS "evt_from",evt_to AS "evt_to",block_number AS "block_number",transaction_hash AS "hash" FROM (SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,transaction_hash AS transaction_hash,signature AS signature,decoded::json->'data'->>'from' AS evt_from,decoded::json->'data'->>'to' AS evt_to,decoded::json->'data'->>'tokenId' AS evt_tokenId FROM raw_ethereum.decoded.events WHERE block_number <= 17242439 AND ( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) as event_table WHERE block_number <= 17242439 AND ( evt_from = '0x0000000000000000000000000000000000000000' ) ORDER BY block_number LIMIT 10
```

## 2. Query Events.Transfer with .as_()

```python
input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
with input.ledger.events.Transfer.as_('ts') as ts:
    df = ts.select(columns=[ts.EVT_FROM],
                    order_by=ts.BLOCK_NUMBER,
                    where=ts.EVT_FROM.eq(Address.null()),
                    limit=10).to_dataframe()
```

```typescript
EventData {
  alias: 'ts',
  columns: [],
  joins: null,
  aggregates: [
    { expression: 'ts.evt_from', asName: 'evt_from' },
    { expression: 'ts.evt_to', asName: 'evt_to' },
    { expression: 'ts.block_number', asName: 'block_number' },
    { expression: 'ts.transaction_hash', asName: 'hash' }
  ],
  where: "ts.evt_from = '0x0000000000000000000000000000000000000000'",
  groupBy: null,
  having: null,
  orderBy: 'ts.block_number',
  limit: '10',
  offset: null,
  originator: 'console',
  eventName: 'Transfer',
  contractAddress: '0xed5af388653567af2f388e6224dc7c4b3241c544',
  l2_columns: [ 'ts.evt_from', 'ts.evt_to', 'ts.evt_tokenId' ]
}
```

```sql
SELECT ts.evt_from AS "evt_from",ts.evt_to AS "evt_to",ts.block_number AS "block_number",ts.transaction_hash AS "hash" FROM (SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,transaction_hash AS transaction_hash,signature AS signature,decoded::json->'data'->>'from' AS evt_from,decoded::json->'data'->>'to' AS evt_to,decoded::json->'data'->>'tokenId' AS evt_tokenId FROM raw_ethereum.decoded.events WHERE block_number <= 17242439 AND ( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) ts WHERE  ts.block_number <= 17242439 AND ( ts.evt_from = '0x0000000000000000000000000000000000000000' ) ORDER BY ts.block_number LIMIT 10
```

- with more columns

```python
input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
with input.ledger.events.Transfer.as_('ts') as ts:
    df = ts.select(aggregates=[(ts.EVT_FROM, 'evt_from'),
                                (ts.EVT_TO, 'evt_to'),
                                (f'{ts.BLOCK_NUMBER}+10', 'block_number'),
                                (ts.TXN_HASH, 'hash')],
                    order_by=ts.BLOCK_NUMBER,
                    where=ts.EVT_FROM.eq(Address.null()),
                    limit=10).to_dataframe()
```

## 3. event.Transfer with Transaction

```python
input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
with input.ledger.events.Transfer.as_('ts') as ts:
    with self.context.ledger.Transaction.as_('tx') as tx:
        df = ts.select(aggregates=[(tx.VALUE, 'value'),
                                    (ts.EVT_FROM, 'evt_from'),
                                    (ts.EVT_TO, 'evt_to'),
                                    (ts.BLOCK_NUMBER, 'block_number'),
                                    (ts.TXN_HASH, 'hash')],
                        order_by=ts.BLOCK_NUMBER,
                        where=ts.EVT_FROM.eq(Address.null()).and_(tx.TO_ADDRESS.eq(input.address)),
                        joins=[(JoinType.LEFT_OUTER, tx, tx.HASH.eq(ts.TXN_HASH))],
                        limit=5000).to_dataframe()
```

```sql
SELECT tx.value AS "value",ts.evt_from AS "evt_from",ts.evt_to AS "evt_to",ts.block_number AS "block_number",ts.transaction_hash AS "hash" FROM (SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,transaction_hash AS transaction_hash,signature AS signature,decoded::json->'data'->>'vt_from' AS ts.evt_from,decoded::json->'data'->>'vt_to' AS ts.evt_to,decoded::json->'data'->>'vt_tokenId' AS ts.evt_tokenId FROM raw_ethereum.decoded.events WHERE block_number <= 17242378 AND ( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) as event_table ts LEFT OUTER JOIN raw_ethereum.public.transactions tx ON tx.hash = ts.transaction_hash WHERE  ts.block_number <= 17242378 AND ( ts.evt_from = '0x0000000000000000000000000000000000000000' and tx.to_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY ts.block_number LIMIT 5000;
```

alt

```python
input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
with self.context.ledger.Transaction.as_('tx') as tx:
    with input.ledger.events.Transfer.as_('ts') as ts:
        df = tx.select(aggregates=[(tx.VALUE, 'value'),
                                    (ts.EVT_FROM, 'evt_from'),
                                    (ts.EVT_TO, 'evt_to'),
                                    (ts.BLOCK_NUMBER, 'block_number'),
                                    (ts.TXN_HASH, 'hash')],
                        order_by=ts.BLOCK_NUMBER,
                        where=ts.EVT_FROM.eq(Address.null()).and_(tx.TO_ADDRESS.eq(input.address)),
                        joins=[(JoinType.RIGHT_OUTER, ts, ts.TXN_HASH.eq(ts.TXN_HASH))],
                        limit=5000).to_dataframe()
```

Join with self

```python
with self.context.ledger.Transaction.as_('tx') as tx:
    with input.ledger.events.Transfer.as_('ts') as ts:
        df = tx.select(aggregates=[(tx.VALUE, 'value'),
                                    (ts.EVT_FROM, 'evt_from'),
                                    (ts.EVT_TO, 'evt_to'),
                                    (ts.BLOCK_NUMBER, 'block_number'),
                                    (ts.TXN_HASH, 'hash')],
                        order_by=ts.BLOCK_NUMBER,
                        where=ts.EVT_FROM.eq(Address.null()).and_(tx.TO_ADDRESS.eq(input.address)),
                        joins=[(ts, ts.TXN_HASH.eq(ts.TXN_HASH))],
                        limit=5000).to_dataframe()
```

```sql
SELECT tx.value AS "value",ts.evt_from AS "evt_from",ts.evt_to AS "evt_to",ts.block_number AS "block_number",ts.transaction_hash AS "hash" FROM (
	SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,
	transaction_hash AS transaction_hash,signature AS signature,
	decoded::json->'data'->>'vt_from' AS evt_from,
	decoded::json->'data'->>'vt_to' AS evt_to,
	decoded::json->'data'->>'vt_tokenId' AS evt_tokenId
	FROM raw_ethereum.decoded.events WHERE block_number <= 17238143 AND
	( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) as event_table
	JOIN raw_ethereum.public.transactions tx ON tx.hash = ts.transaction_hash
	WHERE ts.block_number <= 17238143 AND ( ts.evt_from = '0x0000000000000000000000000000000000000000' )
ORDER BY ts.block_number LIMIT 5000 OFFSET 0
```

raw_ethereum.decoded.events => decoded.events

Single event table lookup

```sql
SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,
	transaction_hash AS transaction_hash,signature AS signature,
	decoded::json->'data'->>'from' AS evt_from,
	decoded::json->'data'->>'to' AS evt_to,
	decoded::json->'data'->>'tokenId' AS evt_tokenId
	FROM decoded.events WHERE block_number <= 17238143 AND
	( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number;
```

```sql
SELECT ts.evt_from AS "evt_from",ts.evt_to AS "evt_to",ts.block_number AS "block_number",ts.transaction_hash AS "hash" FROM
(SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,
	transaction_hash AS transaction_hash,signature AS signature,
	decoded::json->'data'->>'from' AS evt_from,
	decoded::json->'data'->>'to' AS evt_to,
	decoded::json->'data'->>'tokenId' AS evt_tokenId
	FROM decoded.events WHERE block_number <= 17238143 AND
	( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) as ts
WHERE ts.block_number <= 17238143 AND ( ts.evt_from = '0x0000000000000000000000000000000000000000' );
```

Final

```sql
SELECT tx.value AS "value",ts.evt_from AS "evt_from",ts.evt_to AS "evt_to",ts.block_number AS "block_number",ts.transaction_hash AS "hash" FROM
(
	SELECT block_number AS block_number,block_timestamp AS block_timestamp,log_index AS log_index,contract_address AS contract_address,
	transaction_hash AS transaction_hash,signature AS signature,
	decoded::json->'data'->>'from' AS evt_from,
	decoded::json->'data'->>'to' AS evt_to,
	decoded::json->'data'->>'tokenId' AS evt_tokenId
	FROM decoded.events WHERE block_number <= 17238143 AND
	( name = 'Transfer' and contract_address = '0xed5af388653567af2f388e6224dc7c4b3241c544' ) ORDER BY block_number) as ts
	LEFT JOIN public.transactions tx ON tx.hash = ts.transaction_hash
	WHERE
	ts.block_number <= 17238143 and ( ts.evt_from = '0x0000000000000000000000000000000000000000' ) and
    -- Missing the following clause, or replace it with another clause (tx.block_number <= 17238143) would make the query run very slow
    -- This suggests the HASH index alone is very slow
	tx.to_address = '0xed5af388653567af2f388e6224dc7c4b3241c544'
ORDER BY ts.block_number
```