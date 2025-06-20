# Design automation script which accept proces name and display information of that process if it's running
import psutil
import sys
import time
import os

def ProcessDisplay(name):

    Border = "-" * 54

    print(Border)
    print("Information of currently running processes : ")
    print(Border)

    listprocess = []

    for proc in psutil.process_iter(['pid','name','username']):
        if proc.info['name'] == name:
            info = proc.as_dict(attrs = ['pid','name','username'])
            listprocess.append(info)
            #print(info)
    return listprocess

def CreateLog(FolderName,Data):
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

    #Data = ProcessDisplay(name)

    for value in Data:
        fobj.write("%s \n\n" %value)

    fobj.write(Border)

    fobj.close()

def main():

    Arr = ProcessDisplay(sys.argv[1])
    CreateLog(sys.argv[2],Arr)

if __name__ == "__main__":
    main()