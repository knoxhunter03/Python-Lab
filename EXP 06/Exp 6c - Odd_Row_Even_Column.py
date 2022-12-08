import numpy
sA = numpy.array([
                          [3,6,9,12],
                          [15,18,21,24],
                          [27,30,33,36],
                          [39,42,45,48],
                          [51,54,57,60]
                         ])
print("\t Printing Array :")
print(sA)
print("\t Printing Odd Rows and Even Columns : ")
nA = sA[::2,1::2]
print(nA)
