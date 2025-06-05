class Numbers:

    def __init__(self):
        self.value = int(input("Enter the value : "))

    def ChkPrime(self):
        for i in range(2,self.value):
            if (self.value % i == 0):
                return False
        else:
            return True

    def Factors(self):
        for i in range(1,self.value):
            if self.value % i == 0:
                print(i, end = " ")
        print()

    def SumFactors(self):
        self.sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                self.sum = self.sum + i
        print(self.sum)
    
    def ChkPerfect(self):
        if self.sum == self.value:
            return True
        else:
            return False

def main():
    obj = Numbers()

    ret = obj.ChkPrime()
    print(ret)
    obj.Factors()
    obj.SumFactors()
    ret = obj.ChkPerfect()
    print(ret)


if __name__ == "__main__":
    main()