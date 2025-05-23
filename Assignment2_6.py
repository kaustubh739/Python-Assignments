# Write a program which accepts one number and display below pattern
'''*****
****
***
**
*'''

def main():

    print("Enter a number")
    no = int(input())

    for i in range(no):
        for j in range(no):
            no = no - 1
            print(" * ", end ="")
        print()


if __name__ == "__main__":
    main()