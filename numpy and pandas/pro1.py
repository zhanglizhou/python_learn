import numpy as np 
'''a = np.zeros((3, 4), dtype=np.int)
b = np.arange(10,20)
b = b.reshape((2, 5)) #生成一个数列
print(a)
print(b)
'''

a = np.linspace(1, 10, 6, dtype=np.int) #可以改为int
a = a.reshape((2,3))
print(a)