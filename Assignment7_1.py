# Write two lambda functions: calulate square and cube.

print("Enter a number")
no = int(input())

calculatesquare = lambda x : x ** 2
print("square of the given number is : ",calculatesquare(no))

calculatecube = lambda x : x ** 3
print("cube of the given number is : ",calculatecube(no))



