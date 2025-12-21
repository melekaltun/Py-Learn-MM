import numpy
import sys

inp = input()
a = list(map(int, inp.split()))

for i in range(len(a)):
  if a[i] < 1 or a[i] > 3:
     sys.exit()
     
print(numpy.zeros(a, dtype = numpy.int32))
print(numpy.ones(a,dtype = numpy.int32))
    

