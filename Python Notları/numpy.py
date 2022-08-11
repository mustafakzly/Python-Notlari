import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy arrays
#tek boyutlu liste
np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(py_list))
print(type(np_array))
#çok boyutlu liste
py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) #boyutlandırma matris
print(py_multi)
print(np_multi)
print(np_multi.ndim) # boyut olarak bakma 2 boyutlu sonuç çıkarır
print(np_array.ndim)
print(np_array.shape)
print(np_multi.shape)