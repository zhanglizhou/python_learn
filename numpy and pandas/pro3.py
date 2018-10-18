import numpy as np


A = np.arange(2,14).reshape((3,4))
print(np.argmin(A))  #索引最小值
print(np.argmax(A))


#平均值
print(np.mean(A))
print(np.average(A))

#中位数
print(np.median(A, axis=1))

#逐步的累加
print(np.cumsum(A))

#逐步的累差 
print(np.diff(A))

#输入非0的元素的索引
print(np.nonzero(A))

print(A)

#逐行排列
print(np.sort(A))


print(np.transpose(A)) 
print(A.T)


#让值位于5到6
print(np.clip(A, 5, 6))
