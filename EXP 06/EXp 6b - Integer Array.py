import numpy
firstArray = numpy.empty([4,2],dtype=numpy.uint16)
print("\t Printing First Array : ")
print(firstArray)
print("\t Printing numpy array Attributes ")
print("\t 1) Array Shape is : ",firstArray.shape)
print("\t 2) Array Dimensions are : ",firstArray.ndim)
print("\t 3) Length of each element of array in bytes is ",firstArray.itemsize)
