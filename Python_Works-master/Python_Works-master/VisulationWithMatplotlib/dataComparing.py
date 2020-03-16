import pandas as pd

df = pd.read_csv("iris.csv")

print(df.Species.unique())

setosa = df[df.Species == "Iris-setosa"]
print(setosa)
iris_versicolor = df[df.Species == "Iris-versicolor"]
print(iris_versicolor)

print(setosa.describe())
print(iris_versicolor.describe())