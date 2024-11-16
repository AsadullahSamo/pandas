# ---------------------- Data Cleaning ----------------------
# dropna() - drops rows with missing values and returns a new DataFrame (doesn't change the original DataFrame)
# fillna() - fills rows with missing values with a specified value (i.e., 0, mean, median, etc.)
# replace() - replaces a specified value with another value (i.e., replace all 0 with 1)
# interpolate() - fills missing values with a value according to a specified method (i.e., linear, quadratic, etc.)
# using inplace=True will modify the original DataFrame in dropna(), fillna(), and interpolate() methods.


import pandas as pd
data = pd.read_csv('data.csv')
# print(data.to_string()) # Print the entire DataFrame (if it is too large)

missing_removed = data.dropna()
print(missing_removed.to_string())

filled = data.fillna(130) # Fill missing values with 130
# calories_mean = data["Calories"].mean() # Calculate the mean of the "Calories" column (Same for median, mode, etc.)
# calories_filled = data['Calories'].fillna(calories_mean) # Fill missing values in the "Calories" column with the mean
# print(calories_mean)
print(filled.to_string())


# --------------- Cleaning of Wrong Data ---------------
# Wrong data can be replaced with a new value, or the entire row can be removed.

# Replace wrong data:
data.loc[7, 'Duration'] = 45 # Replace the "Duration" column at row 7 with 45
print(data.to_string())

# Remove rows with wrong data:
data.dropna(subset=['Duration'], inplace=True) # Remove rows with missing "Duration" values

for x in data.index:
  if data.loc[x, "Maxpulse"] > 120:
    data.loc[x, "Maxpulse"] = 45 # Replace all values in the "Maxpulse" column that are higher than 120 with 45

print(data.to_string())


for x in data.index:
  if data.loc[x, 'Duration'] > 180:
    data.drop(x, inplace = True) # Remove all rows where the "Duration" is higher than 180

print(data.to_string())


# --------------- Removing duplicates -------------------------
data.drop_duplicates(inplace = True) # Remove all duplicates
print(data.to_string())

# ---------------- Storing the cleaned data -------------------
cleaned_data = data.to_csv('cleaned_data.csv') # Save the cleaned data to a new CSV file
print(cleaned_data) # None
