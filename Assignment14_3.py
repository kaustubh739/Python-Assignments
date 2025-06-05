# Create a class Book with private attribute __price. add method to get and set the price. show encapsulation.

class Book:

    def __init__(self,A):
        self.__price = A

    def Display(self):
        print(self.__price)


def main():
    obj = Book(1000)

    obj.Display()

if __name__ == "__main__":
    main()