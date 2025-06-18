# Design automation script which accept directory name and two file extentions from user. rename all files with first file extension with
# the second file extention
import os
import sys

def directorywatcher(directoryname,ext1,ext2):
    
    flag = os.path.isabs(directoryname)
    
    if flag == False:
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)

    if flag == False:
        print("The path is invalid")
        exit()

    print("The directory path is : ",directoryname)

    for FolderName, subfolders, FileNames in os.walk(directoryname):
        for fname in FileNames:
            if(fname.endswith(ext1)):
                old_filepath = os.path.join(FolderName,fname)
                new_filename = fname.replace(ext1,ext2)
                new_filepath = os.path.join(FolderName,new_filename)

                os.rename(old_filepath,new_filepath)


def main():
    directorywatcher(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()