import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['immediate'] = delivery['order_date'] == delivery['customer_pref_delivery_date']
    return pd.DataFrame({
        'immediate_percentage': [round(delivery['immediate'].sum() / len(delivery['immediate']) * 100, 2)]
    })