# create a file marks.txt with student name and marks.then read the file and display students who scored more than 75 marks.
import os
def main():

    filename = input("Enter the name of the file that you want to check : ")

    ret = os.path.exists(filename)

    if ret == True:
        fobj = open(filename, 'w')

        for i in range(5):
            data = input(f"Enter the data that you want to enter {i + 1} :" +"\n")

            data = fobj.write(data + "\n")

    fobj = open(filename, 'r')
    data = fobj.read()
    
    print("The data is : "+"\n",data)

    lines = data.strip().split(("\n"))
    print("students who scored more than 75 marks are : ")
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            name = parts[0]
            marks = parts[1]
            if marks.isdigit() and int(marks) > 75:
                print(line)

    fobj.close()




if __name__ == "__main__":
    main()