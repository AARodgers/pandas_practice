# terminal: pip install pandas

#load pandas into file
import pandas as pd

#List of names
column = ["Mariya", "Batman", "Spongebob"]
#print(column)

# Make list into a dataframe
#data = pd.DataFrame(column)
#print(data)

# Add a name to the column
#titled_column = {"name": column}
# Add height column in meters and weight column in kg to dataframe
titled_columns = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                 "weigh": [54, 100, 1]}
data = pd.DataFrame(titled_columns)
print(data)
