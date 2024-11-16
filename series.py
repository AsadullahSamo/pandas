# ------------------------ Series ------------------------
# A series is like a column in a spreadsheet, where each value is associated
# It is one-dimensional array-like object containing an array of data.

import pandas as pd
myvar = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
print(myvar)
print(myvar['c'])

# --------------- Create a Series from a Dictionary ---------------
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"]) # Only takes the specified keys
print(myvar)

# --------------- DataFrames ---------------
# DataFrames is a two-dimensional array with labeled axes (rows and columns).
# It is like a table in a SQL database or an Excel spreadsheet.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(myvar)
print(myvar.loc["day2"]) # Accessing row 02

print("--------- Load files in DataFrame ---------")
# --------------- Load Files into a DataFrame ---------------
# If your data sets are stored in a file, Pandas can load them into a DataFrame.
# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('data.csv')
print(df)
print(df.to_string()) # Print the entire DataFrame (if it is too large)
print(df.loc[5]) # Accessing row 5
print(df.head(2)) # Print the first 2 rows (df.tail(2) for the last 2 rows)
print(df.info()) # Print information about the data


print("--------- Loading JSON files ---------")
# --------------- Loading JSON files into a DataFrame ---------------
# Load a JSON file into a DataFrame:
df = pd.read_json('data.json')
print(df)
print(df['name']) # Accessing the 'name' column
print(df['age'].max())
print(df.describe()) # Print statistics of the data