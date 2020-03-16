import pandas as pd


dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }

dataFrame = pd.DataFrame(dictionary)

print(dataFrame["Name"])
print()
print(dataFrame.Age)
print()

dataFrame["New_Column"] = [-1,-2,-3,-4,-5]
print(dataFrame)
print()
print(dataFrame.loc[0:2,"Name":"Age"])
print()
print(dataFrame.loc[0:2,["Name","New_Column"]])
