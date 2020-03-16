import pandas as pd

dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }

dataFrame = pd.DataFrame(dictionary)

filtre = dataFrame.Age > 15
print(filtre)
print()
filtre2 = dataFrame.Name == 'Murat'
print(filtre2)
print()

filtreData = dataFrame[filtre]
print(filtreData)
print()

print(dataFrame[filtre & filtre2])
