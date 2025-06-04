class Demo:
 
    classname = "Marvellous"

    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2
    
    def fun(self):
        print(self.i,self.j)
        
    def gun(self):
        print(self.i,self.j)

def main():
    print("class name : ",Demo.classname)

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()