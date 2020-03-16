import numpy as np # importing numpy framework

#creating a list from numpy framework
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#printing list's shape
print(array.shape)

#list's reshaping
a = array.reshape(3, 5)
print("Spahe: ", a.shape)

print("Dimension: ", a.ndim)
print("Size: ", array.size)
print(type(a))

#0 lardan oluşan 2,3 boyutlu bir dizi oluşturuluyor
zeros = np.zeros((2,3))
print(zeros)
zeros[0,0] = 5
print(zeros)

#1 lerden oluşan 3, 5 boyutlu bir dizi oluşturuluyor
ones = np.ones((3,5))
print(ones)

#3,5 lik boş bir dizi oluşturuluyor
empty = np.empty((3,5))
print(empty)

#10 dan 50 ye kadar olan sayıları 5 er 5 er arttırarak bir listeye aktar
arange = np.arange(10,50,5)
print(arange)