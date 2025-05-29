# print a number using recursion : write a recursive function to print number from 1 to N.
'''def function(no):
    sum = 0
    for i in range(1,no + 1):
        sum = sum + i
        i = i + 1
        function(no)
    return i 


def main():
    ret = function(5)
    print(ret)


if __name__ == "__main__":
    main()
'''

Fact = 1
def Factorial(no):
    global Fact
    #Fact = 1
    while(no >= 1):
        Fact = Fact * no
        no = no - 1

        Factorial(no)
    return Fact

def main():
    ret = Factorial(4)
    print(ret)


if __name__ == "__main__":
    main()