# Accept 10 numbers from the user and write them into a file named Numbers.txt each on new line

filename = input("ENter the file that you want to create : ")

fobj = open(filename,'w')

for i in range(10):
    data = input(f"Enter the numbers {i+1} : " + "\n")
    data = fobj.write(data + "\n")

