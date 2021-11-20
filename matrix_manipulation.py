import numpy

# Two matrices are initialized by value
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# add() to add two matrices
print(f"The addition of two matrices is \n {numpy.add(x, y)}\n")

# subtract() to subtract two matrices
print(f"The subraction between two matrices \n {x} \n and \n {y} \n is \n {numpy.subtract(x, y)}\n")

# divide() to divide two matrices
print(f"Matrix division is \n {numpy.divide(x, y)}\n")

# multiply() to multipy 
print(f"Matrix multiplication is \n {numpy.multiply(x,y)}\n")

# dot() for dot product
print(f"The dot product is \n {numpy.dot(x,y)}\n")

# sqrt() to find square root
print(f"The square root is \n {numpy.sqrt(x)} \n\n {numpy.sqrt(y)} \n")

# sum() to sum elements
print(f"The sum of all elements is {numpy.sum(x)}")

# column-wise summation
print(f"The column wise summation of \n {x} \n is \n {numpy.sum(x, axis=0)} ")

# column-wise summation
print(f"The row wise summation of \n {y} \n is \n {numpy.sum(y, axis=1)} ")

#The transpose is given by .T
print(f"The transpose of matrix \n {x} is \n {x.T}")


