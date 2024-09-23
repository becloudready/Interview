Assignment: Basic Python OOP and FastAPI Application

The code(given in main.py) represents small application that simulates a Bookstore API.

Following endpoints used:

1. GET /books: Retrieve a list of all books.
2. GET /books/{isbn}: Retrieve a specific book by its ISBN.
3. POST /books: Add a new book. The request body should contain details like title, author, year, and ISBN.
4. PUT /books/{isbn}: Update the details of an existing book.
5. DELETE /books/{isbn}: Delete a book by its ISBN.

Storage used for this assignment: Python dictionary(in-memory storage)

How to run:

Step 1: Install dependencies,

pip install "fastapi[standard]"

step 2: In the current directory, run in terminal

fastapi dev main.py

step 3: in the web browser, go to http://127.0.0.1:8000/docs