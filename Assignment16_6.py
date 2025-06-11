# write a python program to copy the contents of one file (source.txt) into destination.txt

def main():
    file1 = input("Enter the source file name : ")

    file2 = input("Enter the destination file name : ")

    with open (file1, 'r') as f1, open (file2, 'a') as f2:
        f2.write(f1.read())

    print(f2)

if __name__ == "__main__":
    main()