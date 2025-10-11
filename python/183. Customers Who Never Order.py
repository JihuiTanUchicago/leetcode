import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    masks = ~customers['id'].isin(orders['customerId'])
    return customers.loc[masks, ['name']].rename(columns={'name':'Customers'})

    