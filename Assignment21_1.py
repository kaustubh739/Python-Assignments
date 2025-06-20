# Design automation script which display information of running processes as it's name, PID, username.
import psutil
import time
import os
import sys

def ProcessDisplay():
    Border = "*" * 54

    print(Border)
    print("Information of currently running processes : ")
    print(Border)

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
            #print(info)
        except Exception:
            print("Exception Occured")
    return listprocess

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "kaustubh%s.Log" %(timestamp))

    fobj = open(FileName, 'w')

    Border = "*" * 80

    fobj.write(Border)
    fobj.write("\n\t\tkaustubh's process log")
    fobj.write("\n\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    Data = ProcessDisplay()

    for value in Data:
        fobj.write("%s \n\n" %value)

    fobj.write(Border)

    fobj.close()

def main():
    CreateLog(sys.argv[1])

if __name__ == "__main__":
    main()