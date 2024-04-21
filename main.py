from books import Book
from users import User
from orders import Order

class Bookstore:
    def __init__(self):
        self.books_inventory = []
        self.users = []
        self.orders = []
        self.book_id_counter = 1  # Initialize the book ID counter

    def add_book(self, id, title, author, price):
        try:
            id = int(id)  # Convert ID to integer
            if id <= 0:
                raise ValueError("ID must be a positive integer.")
            
            price = float(price)  # Convert price to float
            if price <= 0:
                raise ValueError("Price must be greater than zero.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        # Check if book ID already exists in inventory
        if any(book.id == id for book in self.books_inventory):
            print("Book ID already exists in inventory. Cannot add duplicate book.")
            return

        book = Book(id, title, author, price)
        self.books_inventory.append(book)
        print(f"Book '{title}' added to inventory with ID {id}.")

    def display_books(self):
        if not self.books_inventory:
            print("No books available in inventory.")
        else:
            print("Available Books:")
            for book in self.books_inventory:
                print(f"ID: {book.id}, Title: {book.title} by {book.author} - ${book.price}")

    def register_user(self, username, email):
        if not username:
            print("Username cannot be empty.")
            return
        
        if not email:
            print("Email cannot be empty.")
            return
        
        user = next((user for user in self.users if user.username == username), None)
        if user:
            print("User already registered.")
            return
        
        user = User(username, email)
        self.users.append(user)
        print(f"User '{username}' registered.")

    def display_users(self):
        if not self.users:
            print("No users registered.")
        else:
            print("Registered Users:")
            for user in self.users:
                print(f"Username: {user.username}, Email: {user.email}")

    def add_to_cart(self, username, book_id):
        try:
            book_id = int(book_id)  # Convert book ID to integer
            if book_id <= 0:
                raise ValueError("Book ID must be a positive integer.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        user = next((user for user in self.users if user.username == username), None)
        if not user:
            print("User not found.")
            return
        
        book = next((book for book in self.books_inventory if book.id == book_id), None)
        if not book:
            print("Book not found in inventory.")
            return

        if book in user.cart:
            confirmation = input("Book is already in your cart. Do you want to add it again? (yes/no): ")
            if confirmation.lower() != 'yes':
                return  # Do not add the book if confirmation is not 'yes'

        user.cart.append(book)
        print(f"Book '{book.title}' added to cart for user '{username}'.")

    def place_order(self, username):
        user = next((user for user in self.users if user.username == username), None)
        if not user:
            print("User not found.")
            return
        
        if not user.cart:
            print("User's cart is empty. Add books to cart first.")
            return
        
        order = Order(user)
        order.books = user.cart
        self.orders.append(order)
        total_cost = order.calculate_total()
        print(f"Order placed for user '{username}' with total cost ${total_cost}.")
        user.cart = []  # Clear the user's cart after placing the order

    def display_cart(self, username):
        user = next((user for user in self.users if user.username == username), None)
        if not user:
            print("User not found.")
            return
        
        if not user.cart:
            print("User's cart is empty.")
        else:
            print(f"Cart for user '{username}':")
            for book in user.cart:
                print(f"ID: {book.id}, Title: {book.title} by {book.author} - ${book.price}")

if __name__ == "__main__":
    bookstore = Bookstore()

    while True:
        print("\n1. Add Book\n2. Display Books\n3. Register User\n4. Display Users\n5. Add to Cart\n6. Display Cart\n7. Place Order\n8. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                id = input("Enter book ID: ")
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                price = input("Enter book price: ")
                bookstore.add_book(id, title, author, price)
            elif choice == '2':
                bookstore.display_books()
            elif choice == '3':
                username = input("Enter username: ")
                email = input("Enter email: ")
                bookstore.register_user(username, email)
            elif choice == '4':
                bookstore.display_users()
            elif choice == '5':
                username = input("Enter username: ")
                book_id = input("Enter book ID to add to cart: ")
                bookstore.add_to_cart(username, book_id)
            elif choice == '6':
                username = input("Enter username: ")
                bookstore.display_cart(username)    
            elif choice == '7':
                username = input("Enter username: ")
                bookstore.place_order(username)
            
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

