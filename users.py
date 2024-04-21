class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = []  # To store books in the user's cart
