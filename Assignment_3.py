# 3. Write a program which contains one function named as Add() which accepts two number from user and return addition of that two numbers. \

def Add(no1, no2):
    ans = no1 + no2
    return ans

print("Enter the first number")
num1 = int(input())

print("Enter the second number")
num2 = int(input())

result = Add(num1, num2)

print("Addition is : ",result)



#if __name__ == "__main__":
 #   Add()