import pandas as pd
import pandas as pd

employees = {
    "employee_1": {"name": "Alice", "salary": 75000, "age": 28},
    "employee_2": {"name": "Bob", "salary": 62000, "age": 34},
    "employee_3": {"name": "Charlie", "salary": 80000, "age": 29},
    "employee_4": {"name": "David", "salary": 54000, "age": 40},
    "employee_5": {"name": "Eva", "salary": 72000, "age": 26},
    "employee_6": {"name": "Frank", "salary": 59000, "age": 38},
    "employee_7": {"name": "Grace", "salary": 85000, "age": 31},
    "employee_8": {"name": "Hannah", "salary": 67000, "age": 30},
    "employee_9": {"name": "Ian", "salary": 58000, "age": 45},
    "employee_10": {"name": "Judy", "salary": 90000, "age": 27},
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(employees, orient='index')

# Reset the index to have a cleaner DataFrame
df.reset_index(drop=True, inplace=True)

df.to_csv('')
