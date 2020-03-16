import numpy as np

array = np.array([1,2,3,4,5,6,7])

print(array[0:4])  # Output = [1 2 3 4]
print(array)

#Arrayı ters çevirir
reverse_array = array[::-1]
print(reverse_array)    # Output = [7 6 5 4 3 2 1]

array1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(array1[:,1])# Output =   [2 7]
print(array1[1,1:4])# Output =  [7 8 9]

print(array1[-1,:])   # Output = [ 6  7  8  9 10]

print(array1[:,-1])   # Output =   [ 5 10]
