1. Function

````python
with Token('USDC').ledger.functions.Mint as q:
	df1 = q.select(
aggregates=[(f'sum({q.FN__AMOUNT.as_numeric()} / 1e6)', 'sum')],
where=q.BLOCK_NUMBER.between_(16772727, 16779843)).to_dataframe()

with Token('USDC').ledger.functions.Burn as q:
	df2 = q.select(
aggregates=[(f'sum({q.FN__AMOUNT.as_numeric()} / 1e6)', 'sum')],
where=q.BLOCK_NUMBER.between_(16772727, 16779843)).to_dataframe()

print(float(df1.sum()[0]) - float(df2.sum()[0]))
# -257914457.15999997

2. Events

1 row from below query

```python
with Token('USDC').ledger.events.Approval as q:
    df1 = q.select(q.columns, where=q.BLOCK_NUMBER.between_(16772727, 16779843)).to_dataframe()
````
