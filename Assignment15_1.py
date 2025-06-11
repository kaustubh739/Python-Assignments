# write a program which accepts filename from user and check wether that file exists in current directory or not
import os

def main():
    filename = input("Enter the name of the file that you want to check : ")

    ret = os.path.exists(filename)

    if ret == True:
        print("The file is present in the current directory")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()