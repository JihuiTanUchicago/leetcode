import pandas as pd

def salary_level(x):
    if x < 20000:
        return "Low Salary"
    elif 20000 <= x <= 50000:
        return "Average Salary"
    else:
        return "High Salary"

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['salary_level'] = accounts['income'].apply(salary_level)
    salary_levels = ['High Salary', 'Low Salary', 'Average Salary']
    p = accounts.groupby('salary_level')['income'].size()
    p = p.reindex(salary_levels, fill_value=0).to_frame().reset_index()
    p = p.rename(columns={
        'salary_level': 'category',
        'income': 'accounts_count'
    })
    return p

