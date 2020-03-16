import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("iris.csv")
df1 = df.drop("Id",axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

#her üründen kaç tane olduğunu gösteren grafiği getirir
plt.hist(setosa.SepalLengthCm, bins=25)
plt.xlabel("SepalLengthCm")
plt.ylabel("frekans")
plt.show()
