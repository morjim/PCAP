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
    
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}, Price: {round(self.get_price(),3)}, Genero : {self.branch}"
    
novela1 = Novel("La comunidad del Anillo", 30, "J.R.R. Tolkien", 30, 560)
novela1.set_discount(0.20)

ensayo1 = Academic("Modernidad líquida", 12, "Z. Bauman", 18, "Sociología")

print(novela1)
print(ensayo1)