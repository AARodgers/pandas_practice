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
titled_column = {"name": column}
data = pd.DataFrame(titled_column)
print(data)
