class BookStore:
    NoOfBooks = 0 

    def __init__(self,A,B):
        self.name = A
        self.author = B
        BookStore.NoOfBooks += 1 


    def Display(self):
        print("the name of the book is : ",self.name)
        print("the name of the author is : ",self.author)
        print("The number of Books are : ",BookStore.NoOfBooks)
        print(self.name, "by", self.author, "No Of Books : ", BookStore.NoOfBooks)



def main():
    obj1 = BookStore("Linux system programming","Robert love")
    obj1.Display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()