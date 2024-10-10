import pandas as pd
import pandas as pd

data={
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Judy'],
    'salary': [75000, 62000, 80000, 54000, 72000, 59000, 85000, 67000, 58000, 90000],
    'age': [28, 34, 29, 40, 26, 38, 31, 30, 45, 27]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Reset the index to have a cleaner DataFrame
df.to_csv('data/dataset.csv',index=False)

