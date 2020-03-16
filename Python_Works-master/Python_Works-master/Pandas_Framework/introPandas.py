import pandas as pd

dictionary = {"Name":["Murat","Sema","Mehmet","Elif","Yusuf"],
              "Age":[21,19,18,12,5]
              }

dataFrame = pd.DataFrame(dictionary)
print(dataFrame)
print()

#baştan ilk 3 kaydı getirir
head = dataFrame.head(3)
print(head)
print()

#sonra ilk 3 kaydı getirir
tail = dataFrame.tail(3)
print(tail)