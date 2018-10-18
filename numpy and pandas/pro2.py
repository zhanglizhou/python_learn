import numpy as np 
a = np.array([[1,1],
			  [0,1]])
b = np.arange(4).reshape((2,2))

#三种乘法，后面两个一样的作用
c = a*b
c_dot = np.dot(a,b)
c_dot2 = a.dot(b)

#print(c)
#[[0,1
# [0,3]]
#print(c_dot)
#[[2,4
#  [2,3]]
#print(c_dot2)



a1 = np.random.random((2,4))
print(a1)
print(np.sum(a1, axis=1))
print(np.max(a1, axis=0))