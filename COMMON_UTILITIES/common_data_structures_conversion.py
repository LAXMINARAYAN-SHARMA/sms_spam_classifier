# === DATA STRUCTURE CONVERSIONS ===
# Converting between data structures

# List to Series
list_data = [1, 2, 3, 4]
series_data = pd.Series(list_data)
print(series_data)

# Series to List
series_to_list = series_data.tolist()
print(series_to_list)

# Dictionary to DataFrame
dict_data = {'A': [1, 2], 'B': [3, 4]}
df_from_dict = pd.DataFrame(dict_data)
print(df_from_dict)

# DataFrame to Dictionary
df_to_dict = df_from_dict.to_dict()
print(df_to_dict)

# DataFrame to List of Tuples
df_to_tuples = df_from_dict.to_records(index=False).tolist()
print(df_to_tuples)

# List of Tuples to DataFrame
tuples_list = [(1, 'a'), (2, 'b')]
df_from_tuples = pd.DataFrame(tuples_list, columns=['Num', 'Char'])
print(df_from_tuples)

# CSV to DataFrame
csv_data = """A,B,C
1,2,3
4,5,6"""
from io import StringIO
csv_df = pd.read_csv(StringIO(csv_data))
print(csv_df)

# DataFrame to CSV
print(csv_df.to_csv(index=False))

# DataFrame to JSON
print(csv_df.to_json())
