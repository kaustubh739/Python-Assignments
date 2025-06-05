# create a base class person with name and age Derive a class teacher with subject and salary. use super to call base class constructor
# and print both

class person:

    def __init__(self,A,B):
        self.name = A
        self.age = B

    def Display(self):
        print("name is : ",self.name)
        print("The age is : ",self.age)

class teacher(person):
    
    def __init__(self,A,B,C,D):
        super().__init__(A,B)
        self.subject = C
        self.salary = D

    def Display(self):
        super().Display()
        print("The subject is : ",self.subject)
        print("the salary is : ",self.salary)

def main():

    obj = teacher("kaustubh",24,"Python",100000)

    obj.Display()

if __name__ == "__main__":
    main()