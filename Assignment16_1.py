# write a python program to create a text file named student.txt and write the names of 5 students into it.
import os

def main():
    filename = input("Enter the name of the file that you want to check : ")
    
    ret = os.path.exists(filename)
    
    if ret == True:

        fobj = open(filename, 'w')
        for i in range(5):
            

            data = input(f"Enter the data that you want to write {i+1} : " + "\n")

            data = fobj.write(data + "\n")

            #fobj.close()


if __name__ == "__main__":

    main()