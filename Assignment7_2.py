# Accept a list of integer from the user and use the map function to double each value.




Data = [1,2,3,4,5]
print("Input data is : ",Data)

MData = list(map(lambda x : x * 2,Data))
print("Double list : ",MData)