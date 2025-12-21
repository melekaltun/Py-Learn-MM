import numpy
import sys

arrlist = []
inp = input()
a = inp.split()
n = int(a[0])
m = int(a[1])
for i in range(n):
    inp2 = input()
    b = list(map(int, inp2.split()))
    if len(b) == m:
      arrlist.append(b)
    else:
      sys.exit()


arrlist = numpy.array(arrlist)
print(numpy.transpose(arrlist))
print(arrlist.flatten())
