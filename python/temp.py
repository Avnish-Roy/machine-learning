import numpy as np
a=np.arange(2,12,2)
b=np.arange(1,15,3)
c=np.concatenate((a,b))
print(c)
print(a.shape)