import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = sales_person.merge(orders, on='sales_id', how='left')
    df = df.merge(company, on='com_id', how='left', suffixes=("_person", "_company"))
    p = df.groupby('name_person')['name_company'].apply(lambda x: not x.isin(['RED']).any()).reset_index()
    return p[p['name_company']][['name_person']].rename(columns={'name_person': 'name'})