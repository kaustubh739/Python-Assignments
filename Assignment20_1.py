# Design automation script which accept directory name and display checksum of all files.
import os
import hashlib
import sys
import time

def CalculateCheckSum(path):

    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while(len(buffer)>1):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def directorywatcher(dirname):
    
    flag = os.path.isabs(dirname)

    if flag == False:
        dirname = os.path.abspath(dirname)

    flag = os.path.exists(dirname)

    if flag == False:
        print("There is no directory with such name.")
        exit()
    
    print("the directory path is : ",dirname)
    
    for foldername, subfoldername, filenames in os.walk(dirname):
        for fname in filenames:
            fname = os.path.join(foldername,fname)
            checksum = CalculateCheckSum(fname)
            print("The file name is : ",fname)
            print("The checksum name is : ",checksum)

    timestamp = time.ctime()

    filename = "MarvellousLog%slog" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,'w')

    Border = "*" * 54

    fobj.write(Border+"\n")
    fobj.write("This is a kaustubh's automation script\n")
    fobj.write("...............Welcome................\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")
    for foldername, subfoldername, filenames in os.walk(dirname):
        for fname in filenames:
            fname = os.path.join(foldername,fname)
            checksum = CalculateCheckSum(fname)
            fobj.write("The file name is : "+ fname + "\n")
            fobj.write("The checksum name is : "+ checksum + "\n")
        fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("Thanks to come into kaustubh's automation script\n")
    fobj.write("....................ThankYou....................\n")
    fobj.write("This is created at\n" +timestamp+"\n")
    fobj.write(Border+"\n")


def main():
    Border = "*" * 54
    print(Border)
    print("This is a kaustubh's automation script\n")
    print("...............Welcome................\n")
    print(Border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):
            print("please enter the directory name that exists")

        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("It's use to calculate the checksum value")

        else:
            directorywatcher(sys.argv[1])
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("This is a kaustubh's automation script\n")
    print("...............ThankYou...............\n")
    print(Border)
    

if __name__ == "__main__":
    main()