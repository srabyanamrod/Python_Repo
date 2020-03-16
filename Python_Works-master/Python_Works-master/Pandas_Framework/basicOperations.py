import pandas as pd

dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }
dataFrame = pd.DataFrame(dictionary)

print(dataFrame.columns)
print()
print(dataFrame.info())
print()
print(dataFrame.dtypes)
print()
print(dataFrame.describe())
