# FastAPI_Assessment

To get started, follow the steps below:

1. Installation:
   - Make sure you have Python installed on your system. You can download it from https://www.python.org/.
   - Clone this repository to your local machine using Git:
     git clone <repository_url>
   - Navigate to the project directory:
     cd FastAPI_Assessment
   - Create a virtual environment to manage dependencies:
     python -m venv venv
   - Activate the virtual environment:
     - On Windows:
       venv\Scripts\activate
       source venv/bin/activate
   - Install the required dependencies using pip:
     pip install -r requirements.txt
    

2. Database Setup:
   - The application uses SQLite as the database backend, and it will create the necessary database file (`book_reviews.db`) automatically.
   - There's no need for additional database setup.

3. Running the Application:
   - Once the dependencies are installed, you can run the FastAPI application using the following command:
     uvicorn main:app --reload
   - This command starts the FastAPI server with automatic reloading enabled.

4. Using the APIs:
   - Once the server is running, you can access the APIs using a tool like Postman or by sending HTTP requests directly.
   - Here are the available endpoints:
     - POST /books/`: Create a new book.
        request body:
        {
                "title": "Sample Book097",
                "author": "Rakesh1",
                "publication_year": 2026
            }


     - GET /books/`: Retrieve all books, with optional filtering by author or publication year.
        http://127.0.0.1:8000/books/?author=Rakesh1


     - POST /reviews/`: Submit a review for a book.
     http://127.0.0.1:8000/reviews/
        request body={
            "book_id": 8,
            "review_text": "testing text rakesh111422",
            "rating": 9
        }
        


     - GET /reviews/{book_id}`: Retrieve all reviews for a specific book.
     http://127.0.0.1:8000/reviews/2


     - POST /email_reviews/`: Submit a review for a book and trigger a background task to send a confirmation email.
     http://localhost:8000/email_reviews/

     {
    "book_id": 5,
    "review_text": "Great book",
    "rating": 5
    }

   - Make sure to include the required parameters and payload according to the API documentation.

5. Testing:
   - You can run the provided test cases using pytest to ensure that the APIs are functioning correctly:
     ```
     pytest
     ```
   - This command will execute all the test cases defined in the `test_main.py` file.

6. Additional Notes:
   - Please refer to the code comments and documentation within the source files for more details on each endpoint and function.

Please reach out to me if you face any difficulties while access the apis
