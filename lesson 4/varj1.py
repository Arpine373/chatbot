import  numpy as  np

x = np.array([1,2,3])
y = np.array([-7,8,9])
print(np.dot(x,y))#bazmapatkum  matricneri
print(np.cross(x,y))#uxahayac  vektori  pntrum
print(x*x)
bazmapatkum=x*x
sum=bazmapatkum.sum()
print(sum)
x_modulus = np.sqrt((x*x).sum())
y_modulus = np.sqrt((y*y).sum())
print(x_modulus)
print(y_modulus)