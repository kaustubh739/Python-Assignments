# Find largest among three numbers accept three numbers from the user and print the largest using nested if-else statement.

print("Enter the three numbers : ")
no1 = int(input())
no2 = int(input())
no3 = int(input())

if no1 > no2 and no1 > no3:
    print("no1 is largest : ",no1)
elif no2 > no3 and no2 > no1:
    print("no2 is largest : ",no2)
else:
    print("no3 is largest : ",no3)