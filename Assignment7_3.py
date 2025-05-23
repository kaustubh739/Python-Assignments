# accept the list of numbers and use filter() to keep only even numbers

Data = [1,2,3,4,5,6]
print("Input list is : ",Data)

FData = list(filter(lambda x : x % 2 == 0, Data))
print("Even number is : ",FData)