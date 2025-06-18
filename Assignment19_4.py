# Design automation script which accepts two directory names and one file extention. copy all files with the specified extentions from
# first directory into second directory. second directory should be created at runtime.
import os
import sys
import shutil

def directorywatcher(dirname1,dirname2,extention):

    dirname1 = os.path.abspath(dirname1)
    print("the old path is : ",dirname1)

    dirname2 = os.path.abspath(dirname2)
    print("The new path is : ",dirname2)

    if not os.path.exists(dirname2):
        os.mkdir(dirname2)

    for foldername,subfoldernames,filenames in os.walk(dirname1):
        for fname in filenames:
            olddir = os.path.join(foldername,fname)
            if fname.endswith (extention):
                newdir = os.path.join(dirname2,fname)
                shutil.copy(olddir,newdir)

def main():

    directorywatcher(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()