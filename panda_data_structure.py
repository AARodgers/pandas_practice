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


