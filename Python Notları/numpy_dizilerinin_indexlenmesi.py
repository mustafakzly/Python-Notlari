import numpy as np

numberss = np.array([0,5,10,15,20,25,50,75])
result = numberss[5]
result = numberss[-1]
result = numberss[0:3]
result = numberss[:3]
result = numberss[3:]
result = numberss[::]
result = numberss[::-1]

numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers[0]
result = numbers[2]
result = numbers[0,2]
result = numbers[2,2]
result = numbers[:,2]
result = numbers[:,0]
result = numbers[:,0:2]
result = numbers[-1,:]
result = numbers[:2,:2]
#print(result)

arr1 = np.arange(0,10)
#arr2 = arr1 #referance
arr2 = arr1.copy()
arr2[0] = 20

print(arr1)
print(arr2)
