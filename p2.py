import numpy  as np
print(dir(np))

zarray=np.zeros((2,3))
print(zarray)
x = np.array([1,2,3])
y= np.array([4,5,6])
a=np.concatenate((x,y),axis=0)
print(a)
z = np.array([1,2,3])
b=np.array([2,3,4])
r=np.array([5,6,7])
b=np.append(z,b)
print(b)
w=np.sqrt(x)
print(w)


g=z.max(axis=0)

print(g)