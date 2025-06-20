# Design automation script which accepts directory name and delete all duplicate files from that directory. write names of duplicate files
# from that directory into log file named as Log.txt. Log.txt file should be created into current directory.Display execution time 
# required for the script.
import hashlib
import os
import sys
import time

def CalculateCheckSum(path):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def findduplicate(dirname):

    flag = os.path.isabs(dirname)

    if flag == False:
        dirname = os.path.abspath(dirname)

    flag = os.path.exists(dirname)

    if flag == False:
        print("There is no such directory ")
        exit()
    print("The directory is : ",dirname)

    duplicate = {}

    for foldername, subfoldername,filenames in os.walk(dirname):
        for fname in filenames:
            fname = os.path.join(foldername,fname)
            checksum = CalculateCheckSum(fname)
            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum] = [fname]
    return duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("----------------------------------------------------")
        print("value of count is : ",Count)
        print("----------------------------------------------------")
        Count = 0

def DeleteDuplicate(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            count = count + 1
            print(subvalue)
            if(count > 1):
                os.remove(subvalue)
                print("deleted values : ",subvalue)
                Cnt = Cnt + 1
        count = 0
    print("Total deleted files : ",Cnt)

    timestamp = time.ctime()

    filename = "Log%s.txt" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,'w')

    Border = "*" * 54

    fobj.write(Border+"\n")
    fobj.write("This is a kaustubh's automation script\n")
    fobj.write("...............Welcome................\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(subvalue)
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")


    fobj.write(Border+"\n")
    fobj.write("Thanks to come into kaustubh's automation script\n")
    fobj.write("....................ThankYou....................\n")
    fobj.write("This is created at\n" +timestamp+"\n")
    fobj.write(Border+"\n")


def main():

    start_time =time.time()

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
            result = findduplicate(sys.argv[1])
            print(result)
            DeleteDuplicate(result)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("This is a kaustubh's automation script\n")
    print("...............ThankYou...............\n")
    print(Border)

    end_time = time.time()

    print("execution time is : ",end_time - start_time)
    
if __name__ == "__main__":
    main()