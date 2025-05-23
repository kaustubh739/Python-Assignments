# Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.

from functools import reduce

Data = [2,3,4]
print("Input is : ",Data)

RData = (reduce(lambda x,y,z : x*y*z,Data))
print("reduce is : ",RData)