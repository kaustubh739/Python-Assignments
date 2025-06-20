# Design automation script which accepts directory name from user and create log file in that directory which contains the information of
# running processes as it's name, pid and username.
import psutil
import os
import time
import sys

def processdisplay():

    Border = "-" * 54

    print(Border)
    print("Information of currently running processes : ")
    print(Border)

    listprocess = []

    for proc in psutil.process_iter(['name','pid','username']):
        info = proc.as_dict(attrs = ['name','pid','username'])
        listprocess.append(info)
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

    Data = processdisplay()

    for value in Data:
        fobj.write(f"Name    : {value['name']}\n")
        fobj.write(f"username    : {value['username']}\n")
        fobj.write(f"pid    : {value['pid']}\n")

    fobj.write(Border)

    fobj.close()


def main():
    CreateLog(sys.argv[1])

if __name__ == "__main__":
    main()