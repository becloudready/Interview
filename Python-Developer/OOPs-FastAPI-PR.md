### **Assignment: Basic Python OOP and FastAPI Application with GitHub PR Submission**

**Objective:**  
The goal of this assignment is to evaluate your ability to write clean, well-structured Python code using Object-Oriented Programming (OOP), implement a simple REST API using FastAPI, and submit your work via a Pull Request (PR) on GitHub.

### **Problem Statement:**
You are tasked with creating a small application that simulates a Bookstore API. The bookstore will allow users to add, view, update, and delete books using REST API endpoints.

### **Assignment Requirements:**

1. **Use Object-Oriented Programming (OOP) Concepts:**
   - Implement a `Book` class that will represent individual books in the store. The class should contain at least the following attributes:
     - `title`: The title of the book (string).
     - `author`: The author of the book (string).
     - `year`: The year the book was published (integer).
     - `isbn`: A unique identifier for the book (string).

   - Add methods for:
     - `update_book_info` – to update the details of the book.
     - `get_book_info` – to retrieve the book's details.

2. **FastAPI Implementation:**
   - Implement a FastAPI web application with the following endpoints:
     - `GET /books`: Retrieve a list of all books.
     - `GET /books/{isbn}`: Retrieve a specific book by its ISBN.
     - `POST /books`: Add a new book. The request body should contain details like title, author, year, and ISBN.
     - `PUT /books/{isbn}`: Update the details of an existing book.
     - `DELETE /books/{isbn}`: Delete a book by its ISBN.
   - Use in-memory storage for this assignment (e.g., a Python dictionary) to store and manage the list of books.

3. **Code Quality:**
   - Ensure your code follows PEP 8 standards.
   - Write clear and concise docstrings for all classes and methods.
   - Use type hints where appropriate.
   - Include basic error handling (e.g., return appropriate HTTP status codes when a book is not found).

4. **GitHub Repository & PR Submission:**
   - Fork the provided repository (You will be provided with a GitHub link to fork).
   - Clone the forked repository to your local machine.
   - Implement the solution in a directory named `bookstore`.
   - Ensure the code is well-documented and tested.
   - Create a `README.md` file in your project directory with instructions on how to set up and run the FastAPI application.
   - Commit your changes to a new branch and push it to your forked repository.
   - Open a Pull Request (PR) from your branch to the original repository and request a review.

---

### **Bonus Points:**
- Write unit tests for your `Book` class and API endpoints using `pytest` or `unittest`.
- Deploy your FastAPI application locally and test using `http://127.0.0.1:8000/docs` (FastAPI’s auto-generated docs).
- Add pagination to the `GET /books` endpoint.

### **Submission Guidelines:**
- Ensure your PR includes a clear and descriptive title.
- Add a description in the PR body explaining your approach and any assumptions made.
- Include screenshots (if possible) showing your API tests with a tool like Postman or cURL.

---

**Deadline:**  
You have **7 days** to complete this assignment.

Good luck! We look forward to reviewing your submission.

