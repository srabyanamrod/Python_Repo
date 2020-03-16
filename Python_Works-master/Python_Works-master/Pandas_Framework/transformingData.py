import pandas as pd

dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }

dataFrame = pd.DataFrame(dictionary)

def multiply(age):
    return age * 2

dataFrame["Age*2"] = dataFrame.Age.apply(multiply)
print(dataFrame)
