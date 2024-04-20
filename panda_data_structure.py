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
# will be like a matrix with the arrays stacked

# the shape attribute of an ndarray returns a tuple w/ the # of rows and columns
# returns (2, 3), the 2 is for axis = 0 (vertical/rows) and the 3 is for axis = 1 (horizontal/columns)
arr.shape

# get maximum value from array
# default returns maximum from flattened array, meaning as if all values were in one row
arr.max()
#returns 6

# to get maximum value along axis=0, will compare values along axis=0 for each column
# to determine the maximum
arr.max(axis=0)
# returns array([4, 5, 6])
# array looks like:
# [1, 2, 3]
# [4, 5, 6], it compares, 1 and 4, 2 and 5, 3 and 6 and then returns the higher value of each comparison

# to get maximum along axis=1
arr.max(axis=1)
# returns array([3, 6])
# in the first row along axis=1, the max is 3
# in the second row along axis=1, the max is 6

# to get minimum value of flattened ndarray
arr.min()
# returns 1, the overall minimum

# to get minima along axis=0
arr.min(axis=0)
#returns array([1, 2, 3])
# work same as max

# mean of flattened ndarray
arr.mean()

# mean along axis=0
arr.mean(axis=0)
# returns array([2.5, 3.5, 4.5])
# average of 1 and 4, 2 and 5, 3 and 6

# mean along axis=1
arr.mean(axis=1)
# returns array([2., 5.])
# average of first row(x) and average of second row(y)

# operations between array and scalar ( the scalar is broadcasted to each element of array
arr = np.array([1, 2, 3])
b = 2
arr * b
# returns array([2, 4, 6])

# exopnentiation btwn array and scalar
a = [[1, 2, 3], [4, 5, 6]]
arr = np.array(a)
arr ** 2
# returns
# array([[ 1,  4,  9],
#       [16, 25, 36]])

# Broadcasting only works if btwn two arrays if they have either equal trailing axes
# or one of the trailing axis is 1
# trailing axes = counting the axis from the end of the shape, the y value in (x, y)
# create a 2 x 2 array
arr2 = np.array([[1, 2], [1,2]])
arr2.shape
# returns (2, 2)
arr2
# returns array([[1, 2],
#                [1, 2]])

# view other array size
arr.shape
# returns (2, 3)

# error: add two arrays with incomplatible trailing dimensions
# will get error because of broadcasting rules
arr2 + arr

# create a 1 x 3 array ( will be compatible with the (2, 3) array, the last dimension is
# equal and the first dimension is 1
arr2 = np.array([[1, 2, 3]])
arr2.shape
#returns (1, 3)

# add 2 arrays with compatible trailing dimensions, top row gets added to top row
arr + arr2
# returns
# array([[2, 4, 6],
#       [5, 7, 9]])
# arr =
#       ([[1, 2, 3],
#       [4, 5, 6]])
# arr.shape = (2, 3) # 2 rows, 3 columns
# arr2.shape = (1, 3) #
# arr2 = array([[1, 2, 3]])

# sometime you need to create an ndarray with a predetermined shape that you will update with values
# np.zeros() : creates an ndarray of a given shape filled with zeros, the shape is given as a tuple
# create a 4 x 4 ndarray of zeros
np.zeros((4, 4))
# returns
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

# create a 4 x 4 ndarray of zero-like values, with data type boolean
np.zeros((4, 4), dtype=bool)

# array([[False, False, False, False],
#        [False, False, False, False],
#        [False, False, False, False],
#        [False, False, False, False]])

#  create a 4 x 4 ndarray of ones
np.ones((4, 4))
# returns
# array([[1., 1., 1., 1.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.]])

#create a 4 x 4 ndarray of one-like value
np.ones((4, 4), dtype=bool)
# returns
# array([[ True,  True,  True,  True],
#        [ True,  True,  True,  True],
#        [ True,  True,  True,  True],
#        [ True,  True,  True,  True]])


