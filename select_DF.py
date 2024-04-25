# how to import an existing file

import pandas as pd
import_sqlite3

# import file, because it is tab delimited you need second argument because comma delimited is the default
data = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")
print(data)

# to get rid of unnecessary first column, go back to panda_practice.py file and add index=False
# when saving the csv file
