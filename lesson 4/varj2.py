import  numpy as  np
x = np.array([[7, 5], [4, 5]])
y = np.array([[7, 8], [4, 10]])
print ("The element wise addition of matrix is : ")
print (np.add(x,y))
print ("The element wise subtraction of matrix is : ")
print (np.subtract(x,y))
print ("The element wise division of matrix is : ")
print (np.divide(x,y))
print ("The element wise square root is : ")
print (np.sqrt(x))
print ("The summation of all matrix element is : ")
print (np.sum(y))
print ("The column wise summation of all matrix  is : ")
print (np.sum(y,axis=0))
print ("The row wise summation of all matrix  is : ")
print (np.sum(y,axis=1))
print ("The transpose of given matrix is : ")
print (x.T)