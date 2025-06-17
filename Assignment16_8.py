# write a script to remove all blank lines from a file. save a cleaned output to a new file.
import os

def main():
    filename = input("Enter a file to check : ")
    
    ret = os.path.exists(filename)

    if ret == True:
        fobj = open(filename, 'w')

    data = input("Enter the data into it : ")
    data = fobj.write()
    print("The data is : ",data)
    fobj.close()


if __name__ == "__main__":
    main()
