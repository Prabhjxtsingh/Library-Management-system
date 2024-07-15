
# Library Management System

This is a simple library management system implemented in Python using the Pandas and Matplotlib libraries. The system allows users to manage a catalog of books, search for books, borrow books, and return books.

## Features

- Display the catalog of books including title, author, ISBN, and availability.
- Search for a book by title, author, or ISBN.
- Borrow a book from the library (decrease availability).
- Return a book to the library (increase availability).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    ```
2. Change to the project directory:
    ```bash
    cd library-management-system
    ```
3. Install the required libraries:
    ```bash
    pip install pandas matplotlib
    ```

## Usage

Run the script using Python:

```bash
python library_management_system.py
```

### Main Menu

1. **Display Book Catalog**: View the current catalog of books with their details.
2. **Search for a Book**: Search for a book by title, author, or ISBN.
3. **Borrow a Book**: Borrow a book by entering the title of the book.
4. **Return a Book**: Return a book by entering the title of the book.
5. **Exit**: Exit the application.

## Example

### Display Book Catalog

```
Library Management System
1. Display Book Catalog
2. Search for a Book
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 1

Book Catalog:
                    Title                Author           ISBN  Availability
0       The Great Gatsby  F. Scott Fitzgerald  978-0743273565            10
1  To Kill a Mockingbird           Harper Lee  978-0061120084             5
2                   1984         George Orwell  978-0451524935             7
3     Pride and Prejudice          Jane Austen  978-1503285700             8
4   The Catcher in the Rye        J.D. Salinger  978-0316769174             3
```

### Search for a Book

```
Library Management System
1. Display Book Catalog
2. Search for a Book
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 2
Enter a book title, author, or ISBN to search: pride

Search Results:
                Title        Author           ISBN  Availability
3  Pride and Prejudice  Jane Austen  978-1503285700             8
```

### Borrow a Book

```
Library Management System
1. Display Book Catalog
2. Search for a Book
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 3
Enter the title of the book you want to borrow: 1984

You have borrowed '1984' successfully.
```

### Return a Book

```
Library Management System
1. Display Book Catalog
2. Search for a Book
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 4
Enter the title of the book you want to return: 1984

Thank you for returning '1984'.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Acknowledgements

- [Pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
- [Matplotlib](https://matplotlib.org/) - For data visualization.

Feel free to customize this README file according to your project's specific details and requirements.
