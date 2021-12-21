import pandas as pd
import numpy as np

# replicate the 'Employee' table and store it in excel, next read it
employee = pd.read_excel('Employee.xlsx').set_index('id')
#employee.manager_id = employee.manager_id.astype(object)

#question a

# get their manager's salary and store in a list
m_salary = []
for x in employee.manager_id:
    if pd.isnull(x):
        m_salary.append(np.nan)
    else:
        m_salary.append(employee.loc[x, 'Salary'])

# concat the manager's salary to the employee dataframe for comparison
employee['manager_salary'] = m_salary

# get the name of employee whose salary is greater than their managers'
print(employee.query('Salary > manager_salary')['Name'].values)


#question b

#get the ones who's not managing anyone
no_managing = set(employee.index) - set(employee.manager_id)

#get the mean of their salaries
print(employee.loc[list(no_managing), 'Salary'].mean())
