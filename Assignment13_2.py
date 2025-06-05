class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter the name : ")
        self.Amount = float(input("Enter the initial amount : "))

    def Display(self):
        print("Account Holder name : ",self.Name)
        print("Enter the current Balance : "+self.Amount)

    def Deposit(self):
        Add = int(input("Enter the amount taht you want to deposit : "))
        self.Amount = self.Amount + Add
        return self.Amount

    def Withdraw(self):
        Sub = int(input("Enter the amount that you want to withdraw : "))
        self.Amount = self.Amount - Sub
        return self.Amount

    def CalculateIntrest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    obj = BankAccount()
    
    ret = obj.Deposit()
    print(ret)

    ret = obj.Withdraw()
    print(ret)

    ret = obj.CalculateIntrest()
    print("The current intrest is : ",ret)


if __name__ == "__main__":
    main()