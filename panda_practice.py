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
                 "weight": [54, 100, 1]}
data = pd.DataFrame(titled_columns)
#print(data)

# Select weight column
weight_column = data["weight"]
#print(weight_column)

# Get Batman's weight
batman_weight = data["weight"][1]
#print(batman_weight)

# Get Batman's row of info
batman_info = data.iloc[1]
# if you want to get the weight from the row data
batman_info = data.iloc[1]["weight"]
print(batman_info)
