# 1. To check if there are any columns with ALL NaN or no values

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [None, None, None],
    'C': [4, 5, 6]
})

# Check if any column has all NaN values
empty_columns = df.isnull().all()

# Display columns that are completely empty
print(empty_columns[empty_columns == True].index.tolist())

# 2. You can use the count() method to count non-NA cells and then compare this to zero.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [None, None, None],
    'C': [4, 5, 6]
})

# Check if any column has no non-NA values
empty_columns = df.count() == 0

# Display columns that are completely empty
print(empty_columns[empty_columns].index.tolist())


# 3. You can use dropna() with the how='all' parameter to filter out columns with all
# NaN values, and then compare the shape of the DataFrame before and after this operation.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [None, None, None],
    'C': [4, 5, 6]
})

# Columns before dropping NaNs
columns_before = df.columns

# Drop columns with all NaNs
df_dropped = df.dropna(axis=1, how='all')

# Columns after dropping NaNs
columns_after = df_dropped.columns

# Columns that were entirely NaNs
empty_columns = list(set(columns_before) - set(columns_after))

print(empty_columns)


# ### This method checks if there are any NaN values in the entire DataFrame.

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, None, 3],
    'C': [4, 5, 6]
})

# Check if any cell has NaN values
has_nan = df.isnull().values.any()

print("Any NaN values in DataFrame:", has_nan)


# This method counts the total number of NaN values in the DataFrame.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, None, 3],
    'C': [4, 5, 6]
})

# Count total number of NaN values
total_nan = df.isnull().sum().sum()

print("Total NaN values in DataFrame:", total_nan)


# This method checks if there are any NaN values in each column.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, None, 3],
    'C': [4, 5, 6]
})

# Check for NaN values in each column
nan_in_columns = df.isnull().any()

print("NaN values in each column:")
print(nan_in_columns)


# This method identifies the specific cells that contain NaN values.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, None, 3],
    'C': [4, 5, 6]
})

# Find specific locations of NaN values
nan_locations = df.isnull()

print("Locations of NaN values:")
print(nan_locations)

# This method filters the DataFrame to show only rows that contain NaN values.

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, None, 3],
    'C': [4, 5, 6]
})

# Display rows with any NaN values
rows_with_nan = df[df.isnull().any(axis=1)]

print("Rows with any NaN values:")
print(rows_with_nan)


# Error
# If get: error AttributeError: 'numpy.bool_' object has no attribute 'isnull'
# Means you can't call that on a numpy object so you have comment numpy and rerun

# Make sure you're applying isnull() to DataFrames or Series, not boolean values. Here’s a corrected version of the code:

# Check if there are any NaN values in the DataFrame
has_nan = df.isnull().values.any()

print("Any NaN values in DataFrame:", has_nan)

# Do it using pandas not numpy

import pandas as pd

# Extract a single value and check if it's NaN
value = df.loc[0, 'column']
is_nan = pd.isnull(value)

print("Is the value NaN:", is_nan)

# Checking for NaN in each column

# Check for NaN values in each column
nan_in_columns = df.isnull().any()

print("NaN values in each column:")
print(nan_in_columns)


# Display rows with NaN values

# Display rows with any NaN values
rows_with_nan = df[df.isnull().any(axis=1)]

print("Rows with any NaN values:")
print(rows_with_nan)

# To change data types for columns
# Use astype for changing to common types like int, float, or str.
# Use pd.to_datetime for converting to datetime.
# Use astype('category') for converting to categorical types.

import pandas as pd

# Sample DataFrame
data = {
    'A': ['1', '2', '3'],
    'B': ['4.0', '5.1', '6.2'],
    'C': [7, 8, 9],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Category': ['A', 'B', 'A']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print(df.dtypes)

# Changing data types
df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
df['C'] = df['C'].astype(str)
df['Date'] = pd.to_datetime(df['Date'])
df['Category'] = df['Category'].astype('category')

print("\nDataFrame after changing data types:")
print(df)
print(df.dtypes)


# Create new df by writing out which columns

import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Create a new DataFrame with selected columns
new_df = df[['A', 'C']]

print("\nNew DataFrame with columns 'A' and 'C':")
print(new_df)

# Create a new DataFrame with selected columns using loc
new_df = df.loc[:, ['A', 'C']]

print("\nNew DataFrame with columns 'A' and 'C' using loc:")
print(new_df)

# Create a new DataFrame with selected columns using iloc
new_df = df.iloc[:, [0, 2]]  # Select columns at positions 0 and 2

print("\nNew DataFrame with columns at positions 0 and 2 using iloc:")
print(new_df)

# List of columns to select
columns_to_select = ['A', 'C']

# Create a new DataFrame with selected columns
new_df = df[columns_to_select]

print("\nNew DataFrame with selected columns from a list:")
print(new_df)

#### CHANGING THE NAME OF A COLUMN

# Using rename method
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Rename column 'A' to 'Alpha'
df.rename(columns={'A': 'Alpha'}, inplace=True)

print("\nDataFrame after renaming column 'A' to 'Alpha':")
print(df)

# Change name of columns using column attribute
# Change the name of column 'B' to 'Beta'
df.columns = ['Alpha', 'Beta', 'C']  # Renaming columns directly

print("\nDataFrame after renaming column 'B' to 'Beta' using columns attribute:")
print(df)


# To get rid of br in WordClouds

#The presence of 'br' in your word cloud likely results from unfiltered HTML tags or line breaks in your text data. The <br> tag is commonly used in HTML to indicate a line break. If your text source contains HTML content, these tags might get included in the word cloud.

#To remove such artifacts, you need to preprocess your text data to strip out HTML tags and other unwanted characters. Here's a step-by-step guide on how to do this:
