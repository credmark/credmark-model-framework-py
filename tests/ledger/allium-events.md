# Allium events

```sql
SELECT address, topic0, name, interface
	FROM common.event_signatures_per_contract
	where (address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2' or address = '0x514910771af9ca656af840dff83e8264ecf986ca')
	and name = 'Transfer'
	and chain = 'ethereum'
	limit 10;

/*
'{"name": "Approval", "type": "event", "inputs": [{"name": "src", "type": "address", "indexed": true}, {"name": "guy", "type": "address", "indexed": true}, {"name": "wad", "type": "uint256", "indexed": false}], "anonymous": false}'
'{"name": "Transfer", "type": "event", "inputs": [{"name": "src", "type": "address", "indexed": true}, {"name": "dst", "type": "address", "indexed": true}, {"name": "wad", "type": "uint256", "indexed": false}], "anonymous": false}'
*/

SELECT decoded->>'src' as src,
	decoded->>'dst' as dst,
	decoded->>'wad' as wad,
	transaction_hash, log_index, contract_address, block_number, block_timestamp, name, signature
FROM savor_fearless_nurse.ethereum_events
where block_number = 17860029
and contract_address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
and name = 'Transfer';
```
