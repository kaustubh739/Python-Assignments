# create a class calculator with methods for add, subtract, multiply, and divide. ask user input for values and call method accordingly.

class calculator:

    def __init__(self,A,B):
        self.value1 = A
        self.value2 = B

    def Add(self):
        ret = self.value1 + self.value2
        print(ret)

    def Subtract(self):
        ret = self.value1 - self.value2
        print(ret)

    def Multiply(self):
        ret = self.value1 * self.value2
        print(ret)

    def Divide(self):
        ret = self.value1 / self.value2
        print(ret)

def main():
    obj = calculator(20,10)

    obj.Add()
    obj.Subtract()
    obj.Multiply()
    obj.Divide()




if __name__ == "__main__":
    main()
        