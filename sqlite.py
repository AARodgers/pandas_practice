import sqlite3

# Create the database, inside  () is name of database
connection =  sqlite3.connect("gta.db")
# when you create a db you need to create an cursor object, it is in charge of
# all communication with db, if you execute a command, you do it on the cursor object
cursor = connection.cursor()

# to create a table
# cursor.execute("create table table_name (column1 data_type, column2 data_type, column3)")
# tell it what kind of data:
# string=text, float=real, int=integer, binary=blob

# create table from info below
cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
  (1997, "Grand Theft Auto", "state of New Guernsey"),
  (1999, "Grand Theft Auto 2", "Anywhere, USA"),
  (2001, "Grand Theft Auto III", "Liberty City"),
  (2002, "Grand Theft Auto: Vice City", "Vice City"),
  (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
  (2008, "Grand Theft Auto IV", "Liberty City"),
  (2013, "Grand Theft Auto V", "Los Santos"),
]

# 2nd step to creating the table, it has to be below data for it to exist
# cursor.executment("insert into table_name values (column1, column2, column3), data_variable")
cursor.executemany("insert into gta values (?, ?, ?)", release_list)

# print database rows
# for row in cursor.execute("select * from db_name")
for row in cursor.execute("select * from gta"):
  print(row)

# print specific rows
# print all releases within liberty city
# city=:c means the column of city id represent by the dictionary key of c
# where "c": has the value of Liberty City
# print("*******************************")
# cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
# gta_search = cursor.fetchall()
# print(gta_search)

# Create another table of fictional city and real city
# cursor.execute("create table cities (gta_city text, real_city text)")
# # only doing 1 row for demonstration so don't need the many part
# cursor.execute("insert into cities values(?, ?)", ("Liberty City", "New York"))
# cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
# cities_search  = cursor.fetchall()
# print(cities_search)

# manipulate database data (replace all Liberty City's with New York)
# make dynamic, "New York" is in zero row and column 1 or cities_search[0][1]
# Liberty City = cities_search[0][0]
# print("**********************")
# for i in gta_search:
#   adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
# print(adjusted)

connection.close()

#third step to creating db, run file

# to run file, either press run button or in terminal
# navigate to right directory
# type: python3 file_name: python3 sqlite.py
# should see a new file named: database_name.db
