# print sum of even numbers between 1 to 100. use a loop to find and print the sum of all even numbers from 1 to 100.

'''sum = 0
for i in range(1,101,1):
    Ans = i % 2 == 0
    sum = sum + Ans
    print("Even number are : ",sum)'''

i = 1
while i <= 100:
    Ans = i % 2 == 0
    i = i + 1
    print(i)
    

