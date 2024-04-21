class Order:
    def __init__(self, user):
        self.user = user
        self.books = []  # To store books in the order

    def add_book(self, book):
        self.books.append(book)

    def calculate_total(self):
        total_cost = sum(book.price for book in self.books)
        return total_cost
    