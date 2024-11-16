import pandas as pd
titanic = pd.read_csv('titanic.csv')

print(titanic[["Age", "Fare"]].median()) # Calculate the median Age and Fare
print(titanic[["Age", "Fare"]].describe()) # Calculate the mean Age and Fare

print(titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"]
    }
))

print(titanic[["Age", "Sex"]].groupby("Sex").mean()) # Calculate the mean Age
print(titanic.groupby("Sex").mean(numeric_only=True)) # Calculate the mean value for each numeric column
print(titanic.groupby(["Sex", "Passenger Class"])["Fare"].mean()) # Calculate the mean Fare for each combination of Sex and Pclass
print(titanic["Passenger Class"].value_counts()) # Count the number of passengers in each Pclass


# ---------- Sorting Data ----------
print("\n---------- Sorting Data ----------")
print(titanic.sort_values(by="Passenger Class")) # Sort the DataFrame by the "Passenger Class" column
print(titanic.sort_values(by="Passenger Class", ascending=False)) # Sort the DataFrame by the "Passenger Class" column in descending order
