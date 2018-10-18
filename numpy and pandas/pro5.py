#python合并
import numpy as np 
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]

C = np.vstack((A,B)) #vertical stack
D = np.hstack((A,B)) #horizonal stack

print(D.shape)

print(A.shape, C.shape)
print(A.reshape((1,3)).shape)




E = np.concatenate((A,A,B,B), axis=0) #相对于vstack和hstac可以设置axis
print(E)