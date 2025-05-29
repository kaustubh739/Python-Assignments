# sum of digits write a function to calculate to sum of digits of a number.
sum = 0
def Sum(no):
    global sum
    if(no > 0): 
        digit = no % 10 # shevatcha no bhetato
        sum = sum + digit
        #no = no / 10
        no = int(no / 10) # shevatcha no nighun jato
        Sum(no)
    return sum



def main():
    ret = Sum(1234)
    print(ret)


if __name__ == "__main__":
    main()