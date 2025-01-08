class Book:
    #constructor
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        #encapsulaciom: private attributes
        self.__price = price
        self.__discount= None

    #setter method
    def set_discount(self, discount):
        self.__discount = discount

    #getter function
    def get_price(self):
        if self.__discount:
            return self.__price*(1-self.__discount)
        return self.__price
    
    #return a printable representation of the object
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}, Price: {self.get_price()}"
    
book1 = Book("Python Programming", 10, "John Doe", 50)
book2 = Book("Data Science", 20, "Jane Doe", 100)
book3 = Book("Machine Learning", 15, "John Smith", 80)

print(book1)
print(book2)
print(book3)

print(book1.title)
print(book1.author)
print(book1.quantity)
print(book1.get_price())
#print(book1.__discount)