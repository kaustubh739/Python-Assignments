# write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file
# Accept file name through command line arguments.
import sys
import shutil

def copy(sourcefile, destinationfile = "ABC.txt"):
    shutil.copy(sourcefile, destinationfile)
    print("contents copy from sourcefile to destinationfile")
    


def main():
    sourcefile = sys.argv[1] 
    copy(sourcefile)
    

if __name__ == "__main__":
    main()