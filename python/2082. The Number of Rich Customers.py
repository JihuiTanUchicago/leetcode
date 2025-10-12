import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    p = store.groupby(['customer_id','bill_id']).sum()
    p = p.groupby(level='customer_id').max()
    return pd.DataFrame(
        {
            "rich_count": [len(p[p['amount'] > 500])]
        }
    )