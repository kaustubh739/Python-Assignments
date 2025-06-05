# Create a class Student with name, roll_no, and a class variable school_name. print student details and school name. change the school
# name using class name.

class Student:
    School_name = "Shanbhag"

    def __init__(self,A,B):
        self.Name = A
        self.Roll_No = B

    def Display(self):
        print("Student Name : ",self.Name)
        print("Student Roll No : ",self.Roll_No)
        print("School Name : ",Student.School_name)

def main():
    obj = Student("Kaustubh",45)

    print("School name is : ", Student.School_name)
    
    Student.School_name = "Vivekanand"

    print("School name is : ", Student.School_name)


    obj.Display()



if __name__ == "__main__":
    main()