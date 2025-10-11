import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    results = employees.groupby(['emp_id', 'event_day'], as_index=False)['total_time'].sum().rename(columns={'event_day':'day'})
    return results