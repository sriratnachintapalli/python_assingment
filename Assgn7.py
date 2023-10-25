class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}"

    def apply_discount(self, discount):
        if 0 < discount <= 100:
            self.price *= (1 - discount / 100)

class EBook(Book):
    def __init__(self, title, author, price, format):
        super().__init__(title, author, price)
        self.format = format

    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}\nFormat: {self.format}"

# Create a Book instance
book1 = Book("Python Programming", "John Smith", 50.0)

# Display the book's information
print("Book Information:")
print(book1.display())

# Apply a discount to the book
book1.apply_discount(10)
print("After 10% Discount:")
print(book1.display())

# Create an EBook instance
ebook1 = EBook("Advanced Python", "Alice Johnson", 40.0, "PDF")

# Display the eBook's information (overridden display method)
print("\nEBook Information:")
print(ebook1.display())

