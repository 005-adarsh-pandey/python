import pandas as pd

# Read the CSV file
df = pd.read_csv('new_file.csv')

# Sum the values in the second column
total_sum = df.iloc[:, 1].sum()

# Print the total sum
print(total_sum)
   