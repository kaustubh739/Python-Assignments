# write a program to read and display the contents of a file data.txt
import os

filename = input("Enter the file name that you want to check : ")

ret = os.path.exists(filename)

if ret == True:
    fobj = open(filename, 'r')
    data = fobj.read()
    print(data)
    fobj.close()