class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0        

    def Accept(self):
        self.Radius = float(input("Enter the raius : "))

    def CalculateArea(self):
        self.Area = self.PI * (self.Radius ** 2)
         

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        
    
    def Display(self):
        print("The radius of the circle is : ",self.Radius)
        print("The Area of the circle is : ",self.Area)
        print("The circumference is : ",self.Circumference)


def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()


if __name__ == "__main__":
    main()