# create a class product with attributes name and price. Implement __eq__ method to compare two products if they are equal in price.

class product:

    def __init__(self,A,B):
        self.name = A
        self.price = B

    def __eq__(self,other):
        if self.price == other.price:
            return True
        else:
            return False


def main():
    obj1 = product("kaustubh",1000)
    obj2 = product("Devesh",2000)
    obj3 = product("kaustubh",1000)

    print(obj1 == obj3)
    print(obj2 == obj3)

if __name__ == "__main__":
    main()


