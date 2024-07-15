import pandas as pd
import matplotlib.pyplot as plt

# Sample book data
books_data = {
    'Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'ISBN': ['978-0743273565', '978-0061120084', '978-0451524935', '978-1503285700', '978-0316769174'],
    'Availability': [10, 5, 7, 8, 3]
}

# Create a DataFrame from the sample data
library_df = pd.DataFrame(books_data)

# Function to display the book catalog
def display_catalog():
    print("\nBook Catalog:")
    print(library_df[['Title', 'Author', 'ISBN', 'Availability']])

# Function to search for a book
def search_book():
    search_query = input("Enter a book title, author, or ISBN to search: ").strip().lower()
    search_result = library_df[library_df.apply(lambda row: search_query in row['Title'].lower() or
                                                               search_query in row['Author'].lower() or
                                                               search_query in row['ISBN'], axis=1)]
    if not search_result.empty:
        print("\nSearch Results:")
        print(search_result[['Title', 'Author', 'ISBN', 'Availability']])
    else:
        print("\nNo matching books found.")

# Function to borrow a book
def borrow_book():
    title = input("Enter the title of the book you want to borrow: ").strip()
    if title in library_df['Title'].values:
        index = library_df.index[library_df['Title'] == title].tolist()[0]
        if library_df.at[index, 'Availability'] > 0:
            library_df.at[index, 'Availability'] -= 1
            print(f"You have borrowed '{title}' successfully.")
        else:
            print("Sorry, this book is currently unavailable.")
    else:
        print("Book not found in the catalog.")

# Function to return a book
def return_book():
    title = input("Enter the title of the book you want to return: ").strip()
    if title in library_df['Title'].values:
        index = library_df.index[library_df['Title'] == title].tolist()[0]
        library_df.at[index, 'Availability'] += 1
        print(f"Thank you for returning '{title}'.")

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. Display Book Catalog")
    print("2. Search for a Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_catalog()
    elif choice == '2':
        search_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
