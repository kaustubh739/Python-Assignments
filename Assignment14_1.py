# Create a class Employee with attributes name, emp_id, and salary. create object of this class and print their details using a method.
# Expected output : Rohit, Id : 101, Salary : 50000

class Employee:

    def __init__(self,A,B,C):
        self.Name = A
        self.Id = B
        self.Salary = C

    def Details(self):
        print("the name is : ",self.Name)
        print("The id is : ",self.Id)
        print("the salary is : ",self.Salary)

def main():
    obj = Employee('Rohit',101,50000)

    print("The name is : ",obj.Name)
    print("The Id is : ",obj.Id)
    print("The salary is : ",obj.Salary)

    obj.Details()


if __name__ == "__main__":
    main()