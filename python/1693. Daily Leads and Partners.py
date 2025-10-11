import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id':'nunique',
        'partner_id':'nunique'
    }).reset_index()

    df = df.rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners'
    })

    return df