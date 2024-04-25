# how to import an existing file
import pandas as pd
import sqlite3

# import file, because it is tab delimited you need second argument because comma delimited is the default
data = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")

# pd.read_sql("select * from table_name_in_db", connection_variable_or_the_db_itself)
gta_data = pd.read_sql("select * from gta", connection)

print(gta_data)

# to get rid of unnecessary first column, go back to panda_practice.py file and add index=False
# when saving the csv file
