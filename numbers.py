#print function only take string data type. so if you would like to print an integer, need to convert to string
my_num = 5
print(str((my_num)) + " is my favourite number")

print(pow(4,6)) #4 power of 6 
print(4 ** 6) #same like 4 power  of 6
print(max(4,6)) #print which one is largest number
print(min(4,6)) #print which one is smallest number
print(round(3.7)) #round to number whether up or down

print(10%3) # % means modulus. modulues means it will show the remainder of the division. 10 divided by 3 is 3 with remainder 1 so output will be 1

''' python have a set of math function, in order to access them need to include this:'''

from math import * #the math is called module

#we cal
 
print(floor(3.7)) #chop off decimal point
print(ceil(3.7)) #round the number up no matter what
print(sqrt(36)) #square root

