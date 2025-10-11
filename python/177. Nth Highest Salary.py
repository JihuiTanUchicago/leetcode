import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    filtered = employee.drop_duplicates(subset='salary', keep='first').sort_values('salary', ascending=False)
    if len(filtered) < N or N <= 0:
        result = None
    else:
        result = filtered.iloc[N-1]['salary']
    return pd.DataFrame(
        {
            f"getNthHighestSalary({N})": [result]
        }
    )