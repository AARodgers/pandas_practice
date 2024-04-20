# To create an environment with constant versions of dependancies:
# conda create --name pandas101 python=3.9 pandas=1.2.4 numpy=1.20.1 ipykernel=5.3.4
# probably need to update all version numbers

# To activate environment:
#conda activate pandas101

import pandas as pd
import numpy as np

# create a Series object using a scalar
# Series object: a one dimensional array with axis labels
# Series(): constructed using data that is of array-like, Iterable, dictionary, or scalar value.
pd.Series(6.3)

# create a Series object using a list
pd.Series([0,1,2,3,4,5])

# create a Series object using an ndarray
# ndarray: an array object representing a multi-dimensional homogenous array of fixed-size items

# Create a numpy array
data = np.array([10, 20, 30, 40, 50])

# Create a pandas Series from the numpy array
series = pd.Series(data)

# Print the Series
print(series)

# create a Series using a dictionary
series = pd.Series({"name": "PyDataPDX", "city": "Portland", "state": "Oregon"})
print(series)

# access the "name" index of 'series'
series["name"]

# create a DataFrame using a list of Series objects
# each series object is created using a dictionary with the same keys which become the Index
# of the DataFrame columns
# The names of the Series objects become the index for the DataFrame rows.
# DataFrame: 2-dimensional, size-mutable, and potentially heterogeneous tabular data
a = pd.Series({ "A": 1, "B": 2, "C": 3}, name="Order")
b = pd.Series({"A": True, "B": False, "C": False}, name="?Vowel")
c = pd.Series({"A": "Apple", "B": "Banana", "C": "Cantaloupe"}, name="Example of Fruit")
df =pd.DataFrame([a,b,c])
df

# To change rows to columns and columns to row
df.T

# Create a dataframe from a dictionary of dictionaries
# Keys of the final dictionary become the column index
a = { "A": 1, "B": 2, "C": 3}
b = {"A": True, "B": False, "C": False}
c = {"A": "Apple", "B": "Banana", "C": "Cantaloupe"}
df = pd.DataFrame({ "Order": a, "?Vowel": b, "Example of fruit": c})
df

# access a column by passing a column name to the DataFrame with square brackets
# only columns can be accessed this way and rows will give you an error
df["Order"]

# access rows using the .loc method and passing in a row label
df.loc["A"]

# you can also access rows using .iloc and passing in a row integer location
df.iloc[0]

# to access all rows for only two columns ( Order and Vowel ), pass a colon as the row
# index and a list with the column names to the loc method
df.loc[:, ["Order", "?Vowel"]]

# to access only rows B and C for columns Order and Example of fruit, pass B:C as the
# row index and a list of the column names as the column index to the loc method
df.loc["B":"C", ["Order", "Example of fruit"]]

# also can get rows by passing a boolean array to df between square brackets
# it will return rows with the index corresponding to the index of True values in the
# boolean
# Here the 0th index is True and indexes 1 and 2 are False, so it returns a df with only the first row
df[[True, False, False]]

# get rows where ?Vowel=True
df[df["?Vowel"]]

# get rows where ?Vowel=False ( using the ~ , the logical NOT operator)
df[~df["?Vowel"]]

# get rows where ?Vowel=False using the numpy package
df[np.logical_not(df["?Vowel"])]

# ndarrays: multi-dimensional or n-dimensional array can be constructed using a single
# integer, array like object or list
# create an ndarray from a nested list
a = [[1, 2, 3], [4, 5, 6]]
arr = np.array(a)
a


