#include <bits/stdc++.h>

namespace std;

class Book {
private:
    string title;
    string author;
    double price;

public:
    Book(const string& title, const string& author, double price)
        : title(title), author(author), price(price) {}

    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    double getPrice() const { return price; }
};

class User {
private:
    string username;
    vector<Book> cart;

public:
    User(const string& username) : username(username) {}

    void addToCart(const Book& book) { cart.push_back(book); }

    double getTotalCost() const {
        double totalCost = 0.0;
        for (const Book& book : cart) {
            totalCost += book.getPrice();
        }
        return totalCost;
    }

    void displayCart() const {
        cout << "Shopping Cart for " << username << ":\n";
        for (const Book& book : cart) {
            cout << "Title: " << book.getTitle() << ", Author: " << book.getAuthor()
                      << ", Price: $" << book.getPrice() << "\n";
        }
    }

    string getUsername() const { return username; }
};

class Bookstore {
private:
    vector<Book> booksInventory;
    vector<User> registeredUsers;

public:
    void addBook(const Book& book) { booksInventory.push_back(book); }

    void displayBooks() const {
        cout << "Available Books:\n";
        for (const Book& book : booksInventory) {
            cout << "Title: " << book.getTitle() << ", Author: " << book.getAuthor()
                      << ", Price: $" << book.getPrice() << "\n";
        }
    }

    void registerUser(const string& username) {
        registeredUsers.emplace_back(username);
    }

    void placeOrder(const string& username) {
        auto it = find_if(registeredUsers.begin(), registeredUsers.end(),
                               [&username](const User& user) { return user.getUsername() == username; });

        if (it != registeredUsers.end()) {
            cout << "Order placed successfully for user: " << username << endl;
        } else {
            throw invalid_argument("User not found!");
        }
    }
};

int main() {
    Bookstore bookstore;
    Book book1("Python Programming", "John Doe", 25);
    Book book2("Data Structures", "Jane Smith", 30);

    bookstore.addBook(book1);
    bookstore.addBook(book2);

    bookstore.displayBooks();

    bookstore.registerUser("user1");
    User user1("user1");

    user1.addToCart(book1);
    user1.addToCart(book2);

    user1.displayCart();

    try {
        bookstore.placeOrder("user1");
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}
