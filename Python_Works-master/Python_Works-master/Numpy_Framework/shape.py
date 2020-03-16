import numpy as np

# 3 e 3 lük bir array tanımlandı
array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array)

#array tek boyutlu bir array haline getirildi
array2 = array.ravel()
print(array2)

array3 = np.array([[1,2], [3,4], [5,6]])
print(array3)
print()

#arrayı 1 ye 3 lük bir hale getirerek başka bir arraya aktarıldı. ilk array hala aynı
array4 = array3.reshape(2,3)
print(array4)
print()

print(array3)
print()

#arrayı 2 ye 3 lük bir hale getirerek aynı arrraye aktarıldı. ilk array değiştirildi.
array3.resize(2,3)
print(array3)
