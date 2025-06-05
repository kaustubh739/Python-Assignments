# create a class BankAccount with Account_number, name and balance. use __init__ and create methods for deposit, withdraw and displaying balance.

class BankAccount:

    def __init__(self,A,B,C):
        
        self.Account_number = A
        self.name = B
        self.balance = C

    def Display(self):
        
        print("Account number : ",self.Account_number)
        print("Account holder name : ",self.name)
        print("Account Balance : ",self.balance)

    def deposit(self):
        self.value = int(input("Enter the deposited amount"))
        self.balance += self.value
        print("Deposited balance is : ",self.balance)


    def WithDraw(self):
        self.value = int(input("Enter the withdraw amount"))
        self.balance -= self.value
        print("withdraw balance is : ",self.balance)

    def Balance(self):
        print("current balance is : ",self.balance)

def main():
    obj = BankAccount(101,"Kaustubh",1000)

    obj.Display()
    obj.deposit()
    obj.WithDraw()
    obj.Balance()


if __name__ == "__main__":
    main()
