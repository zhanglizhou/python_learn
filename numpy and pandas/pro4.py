import numpy as np 
A = np.arange(3,15).reshape(3,4)

print(A[2,1])
print(A[2][1])

print(A[2,:])
print(A[2])

print(A[1,1:2])
print(A[:,1]) #1col



for row in A:
	print(row)


for item in A.flat:#寻找值,默认是按照行
	print(item)