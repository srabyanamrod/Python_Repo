import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv")

df1 = df.drop("Id",axis=1)
df1.plot()
plt.show()