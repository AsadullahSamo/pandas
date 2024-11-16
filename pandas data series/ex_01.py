import pandas as pd
series1 = pd.Series(["Red", "Green", "Orange", "Pink", "Yellow", "White"])
print(series1)

sr2 = series1.map(lambda x: len(x))