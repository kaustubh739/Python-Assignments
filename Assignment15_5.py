# Accept file name and one string from user and return the frequency of that string from file
import sys

def file(filename,stringname):
    with open (filename, 'r') as f1:
        content = f1.read()
        count = content.count(stringname)
        print(count)


def main():
    A = sys.argv[1]
    B = sys.argv[2]

    file(A,B)
if __name__ == "__main__":
    main()