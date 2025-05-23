# Arithematic Operations on two numbers. write a program to acept two integers from the user and display their: SUm, difference,product division

print("Enter the first number : ")
value1 = int(input())

print("Enter the second number : ")
value2 = int(input())

sum = lambda value1, value2 : (value1 + value2)
print("addition is : ",sum(value1,value2))

difference = lambda value1, value2 : (value1 - value2)
print("Substraction is : ",difference(value1,value2))

product = lambda value1, value2 : (value1 * value2)
print("Multiplication is : ",product(value1,value2))

division = lambda value1, value2 : (value1 / value2)
print("Division is : ",division(value1,value2))