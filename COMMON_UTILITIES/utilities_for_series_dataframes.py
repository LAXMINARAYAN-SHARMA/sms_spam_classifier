# Import Pandas
import pandas as pd

# === SERIES ===
s = pd.Series([1, 2, 3, 4, 5])

# Apply a function to each element
print(s.apply(lambda x: x**2))  # Square each element

# Map values using a function or a dictionary
print(s.map(lambda x: x + 10))  # Add 10 to each element
mapping = {1: 'one', 2: 'two'}
print(s.map(mapping))          # Replace values using a dictionary

# Statistical summaries
print(s.sum())                 # Sum of all elements
print(s.mean())                # Mean of the elements
print(s.std())                 # Standard deviation
print(s.value_counts())        # Count occurrences of unique values

# Boolean filtering
print(s[s > 2])                # Filter elements greater than 2

# Replace values
print(s.replace({3: 99, 5: 100}))  # Replace specific values

# === DATAFRAME ===
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': ['a', 'b', 'c', 'd']
})

# Apply a function column-wise or row-wise
print(df.apply(lambda x: x.sum(), axis=0))  # Column-wise sum
print(df.apply(lambda x: x.sum(), axis=1))  # Row-wise sum

# Apply element-wise operations
print(df['A'].apply(lambda x: x**2))       # Square each element in column 'A'

# Map values in a single column
mapping = {1: 'one', 2: 'two'}
print(df['A'].map(mapping))               # Replace values in column 'A'

# Apply with multiple columns
print(df.applymap(lambda x: str(x) if isinstance(x, int) else x.upper()))  
# Apply to every element in the DataFrame

# Filtering rows based on conditions
print(df[df['A'] > 2])                   # Rows where column 'A' > 2
print(df[(df['A'] > 1) & (df['B'] < 40)])  # Multiple conditions

# Grouping and aggregation
print(df.groupby('A').sum())             # Group by column 'A' and sum
print(df.groupby('A').agg({'B': 'mean', 'C': 'count'}))  # Custom aggregation

# Sorting
print(df.sort_values(by='B', ascending=False))  # Sort by column 'B'

# Column and row operations
df['D'] = df['A'] + df['B']                # Create a new column
print(df.drop('C', axis=1))                # Drop a column
print(df.drop(0, axis=0))                  # Drop a row

# Handling missing data
df.loc[2, 'B'] = None                     # Set a value to NaN
print(df.fillna(0))                       # Fill missing values
print(df.dropna())                        # Drop rows with NaN values

# Statistical summaries
print(df.describe())                      # Summary statistics
print(df['A'].cumsum())                   # Cumulative sum

# Pivot Tables
pivot = df.pivot_table(values='B', index='A', aggfunc='sum')
print(pivot)

# === COMMON UTILITIES ===
# Lambda Functions
df['E'] = df['A'].apply(lambda x: x*2)

# Map vs Apply
print(df['A'].map(lambda x: x+1))
print(df.apply(lambda x: x.sum(), axis=0))  # Sum of each column

# Applymap
print(df.applymap(lambda x: x*2 if isinstance(x, int) else x))

# Groupby with Aggregations
print(df.groupby('A').agg({'B': 'sum', 'C': 'count'}))

# Missing Value Handling
print(df.fillna(0))
print(df.dropna(axis=0))

# merging two dataframes
df1.merge(df2,on=)