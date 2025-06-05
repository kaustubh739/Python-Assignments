# Write a class rectangle with length and width. Add a method to compute area and perimeter. area = 50, perimeter = 30

class Rectangle:

    def __init__(self,A,B):
        self.length = A
        self.Width = B

    def Compute(self):
        area = self.length * self.Width
        print(area)

        perimeter = 2 * (self.length + self.Width)
        print(perimeter)


def main():
    obj = Rectangle(50,30)

    obj.Compute()


if __name__ == "__main__":
    main()