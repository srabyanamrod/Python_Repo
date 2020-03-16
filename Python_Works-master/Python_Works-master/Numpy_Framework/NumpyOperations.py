import numpy as np

#2,3 boyutunda iki dizi tanımlandı
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[1,2,3], [4,5,6]])

print(a*b)

b1 = b.T
x = a.dot(b1)
print(x)

#numpy kütüphanesinden 0 ile 1 arasında sayılardan oluşan 5 e 5 lik bir matris oluşturuldu.
random = np.random.random((5,5))
print(random)
print("")

#matristeki sutunları toplamaya yarar.
print(random.sum(axis=0))

print("")
#matristeki satırları toplamaya yarar.
print(random.sum(axis=1))

#matrisin karesini alma
print(np.square(random)) # random**2
print()

#matrisin karekökünü alma
print(np.sqrt(random))

