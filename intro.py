import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
    'year': [2020, 2019, 2018]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

