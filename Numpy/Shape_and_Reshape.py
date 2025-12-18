import numpy
array = input()
sayilar = list(map(int, array.split()))

my_array = numpy.array(sayilar)
print (numpy.reshape(my_array,(3,3)))
