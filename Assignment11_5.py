# count zeros in a number (Recursively)
def count(no):
    value = 0
    while(no > 0):
        digit = no % 10
        if(digit == 0):
            value = value + 1
        no =(no // 10)
    return value

def main():
    ret = count(10600309)
    print(ret)


if __name__ == "__main__":
    main()