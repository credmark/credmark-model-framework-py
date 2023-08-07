```sql
SELECT trace_type, to_address as address, block_number
FROM TRACES
WHERE block_number between 16000000 and 16010000
and trace_type = 'suicide';
```

```sql
select address, count(block_number) as usage from
(
/*
disable for now
SELECT 'create' as source, to_address as address, block_number
FROM TRACES
WHERE block_number between 16000000 and 16010000
and trace_type = 'create'
union
*/
SELECT /* 'call' as source, */ to_address as address, block_number
FROM TRACES
WHERE block_number between 16000000 and 16010000
and trace_type = 'call'
except
SELECT /* 'suicide' as source, */ to_address as address, block_number
FROM TRACES
WHERE block_number between 16000000 and 16010000
and trace_type = 'suicide'
) as list_of_address
where address != '0x0000000000000000000000000000000000000000'
group by address
having count(block_number) > 1
order by address, usage desc
```