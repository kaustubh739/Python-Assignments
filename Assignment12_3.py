class Arithmetic:

    def __init__(self):
        self.value1 = 0.0
        self.value2 = 0.0

    def Accept(self):
        self.value1 = float(input("ENter the first number : "))
        self.value2 = float(input("Enter the second number : "))

    def Addition(self):
        Add = self.value1 + self.value2
        return Add

    def Subtraction(self):
        Sub = self.value1 - self.value2
        return Sub

    def Multiplication(self):
        Mul = self.value1 * self.value2
        return Mul

    def Division(self):
        Div = self.value1 / self.value2
        return Div

def main():
    obj = Arithmetic()

    obj.Accept()

    Ret = obj.Addition()
    print(Ret)

    Ret = obj.Subtraction()
    print(Ret)

    Ret = obj.Multiplication()
    print(Ret)

    Ret = obj.Division()
    print(Ret)



if __name__ == "__main__":
    main()