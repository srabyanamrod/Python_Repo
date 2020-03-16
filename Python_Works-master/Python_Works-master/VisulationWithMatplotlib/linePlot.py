import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("iris.csv")
df1 = df.drop("Id",axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa",alpha=0.5)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="blue", label="versicolor",alpha=0.5)
plt.plot(virginica.Id, virginica.PetalLengthCm, color="black", label="virginica",alpha=0.5)
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid = True,linestyle=":")
plt.show()
