import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', how='right')[['name_y', 'name_x', 'salary']]
    merged.rename(columns={
        'name_y': 'Department',
        'name_x': 'Employee',
        'salary': 'Salary'
    }, inplace=True)

    highest_by_department = merged.groupby('Department')['Salary'].transform(max)
    return merged[merged['Salary'] == highest_by_department]