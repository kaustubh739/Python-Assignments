# Design automation script which accept two directory names. copy all files from first directory into second directory.
# second directory should be created at runtimne.

import os
import sys
import shutil

def directorywatcher(dirname1,dirname2):

    dirname1 = os.path.abspath(dirname1)
    dirname2 = os.path.abspath(dirname2)

    print("The directory path is : ",dirname1)

    if not os.path.exists(dirname2):
        os.mkdir(dirname2)
    print("created the new directory : ",dirname2)

    for FolderName, subfolder, FileNames in os.walk(dirname1):
        for fname in FileNames:
            olddir = os.path.join(FolderName,fname)
            newdir = os.path.join(dirname2,fname)
            shutil.copy(olddir,newdir)


def main():

    directorywatcher(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()