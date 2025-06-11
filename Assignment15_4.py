# Write a program which accepts two file names from user and compare contents of both the files. If both the files contains same contents
# then display success otherwise display failure. Accept names of both the files from command line. 
import sys
import filecmp

def file(file1,file2):
    '''if filecmp.cmp(file1, file2, shallow = False):
        print("Success")
    else:
        print("Failure")'''
    with open (file1, 'r') as f1, open (file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            print("Success")
        else:
            print("Failure")

def main():
    A = sys.argv[1]
    B = sys.argv[2]

    file(A,B)

if __name__ == "__main__":
    main()