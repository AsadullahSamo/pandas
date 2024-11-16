import pandas as pd
titanic = pd.read_csv('titanic.csv')
# print(titanic.to_string()) # Print the entire DataFrame (if it is too large)

print(titanic[["Age", "Sex"]]) # Print the Age and Sex columns
above_35 = titanic[titanic["Age"] > 35]
print(above_35[["Age", "Passenger Class"]])

cabin_2_or_3 = titanic[titanic["Passenger Class"].isin([2, 3])]
print(cabin_2_or_3[["Passenger Class", "Fare"]])

age_not_null = titanic[titanic["Age"].notna()]
print(age_not_null.shape) # (714, 12) Shows that there are 714 rows with non-null values in the "Age" column

adult_names = titanic.loc[titanic["Age"] > 35, "Name"] # Get the names of passengers older than 35 (The part before the comma is the rows you want, and the part after the comma is the columns you want to select.)
print(adult_names)

# titanic.rename(columns = {"Pclass": "Passenger Class"}, inplace=True) # Rename the "Pclass" column to "Passenger Class"
# titanic.to_csv('titanic.csv', index=False)
