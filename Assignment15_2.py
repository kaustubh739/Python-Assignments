# write a program which accept filename from user and open that file and display the contents of that file on screen
import os

def main():
    filename = input("Enter the file that you want to check : ")

    ret = os.path.exists(filename)

    if ret == True:
        print("the file is present in current directory")
        fobj = open(filename, 'w')
        data = input("Enter the data that you want to write")
        data = fobj.write(data)

        fobj.close()

        fobj = open(filename, 'r')
        data = fobj.read()

        print("Data from file is : ",data)

if __name__ == "__main__":
    main()