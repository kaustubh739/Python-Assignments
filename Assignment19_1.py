# Design automation script which accept directory name and file extension from user. Display all files with that extension.
import os
import sys
def directorywatcher(DirectoryName,Extension):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("path is valid but the target is not directory")
        exit()

    print("The directory path is : ",DirectoryName)

    for Foldername, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            if (fname.endswith(Extension)):
                print(fname)

def main():
    directorywatcher(sys.argv[1],sys.argv[2])



if __name__ == "__main__":
    main()