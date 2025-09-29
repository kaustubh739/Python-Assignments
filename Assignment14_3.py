# Create a class Book with private attribute __price. add method to get and set the price. show encapsulation.

class Book:
    def __init__(self,price):
        self._price = price

    def get_price(self):
        return self._price
    
    def set_price(self,new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("price cannot be negative")

def main():
    obj = Book(1000)

    print("Initial price : ",obj.get_price())

    obj.set_price(500)
    print("Updated price : ",obj.get_price())

    #obj.Details()
    
if __name__ == "__main__":
    main()
