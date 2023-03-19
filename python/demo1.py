from numpy import *
a=array([2,34,78,9,12])
b=array([3,45,23,45,5])
c=where(a>b,a,b)
print(c)