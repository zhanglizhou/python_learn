import numpy as np 

a = np.array(4)
b = a
c = a
d = b   #改一个都改变了


e = a.copy() #deep copy 此时改变e不会影响a