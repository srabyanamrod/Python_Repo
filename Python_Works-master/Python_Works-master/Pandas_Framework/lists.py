import pandas as pd

dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }

dataFrame = pd.DataFrame(dictionary)

#ortalama yaşı verir
age_mean = dataFrame.Age.mean()
print(age_mean)

dataFrame["MaasSeviyesi"] = ["düsük" if age_mean > each  else "yuksek" for each in dataFrame.Age]
print(dataFrame)
print()

dataFrame.columns = [each.upper() for each in dataFrame.columns]
print(dataFrame)

dataFrame.columns = [each.split()[0] + "_" + each.split[1] if(len(each.split()) > 1) else each for each in dataFrame.columns]
print(dataFrame)
