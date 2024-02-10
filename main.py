from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

# Initialize FastAPI app
app = FastAPI()

# Database connection
conn = sqlite3.connect('book_reviews.db')
cursor = conn.cursor()

def get_connection():
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()
    return conn, cursor

# Create tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        review_text TEXT NOT NULL,
        rating INTEGER NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
''')
conn.commit()

# Pydantic models for data validation
class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    book_id: int
    review_text: str
    rating: int

# Endpoints to create book api
@app.post("/books/")
def create_book(book: Book):
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
                   (book.title, book.author, book.publication_year))
    conn.commit()
    conn.close()
    return {"message": "Book added successfully"}
    

# endpoint to get books
@app.get("/books/")
def get_books(author: Optional[str] = None, publication_year: Optional[int] = None):
    book_dict={}
    conn, cursor = get_connection()
    if author:
        cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
    elif publication_year:
        cursor.execute("SELECT * FROM books WHERE publication_year = ?", (publication_year,))
    else:
        cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    book_list = []
    for book in books:
        book_dict = {
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "publication_year": book[3]
        }
        book_list.append(book_dict)

    return {"books": book_list}
    

#endpoint to create reviews api
@app.post("/reviews/")
def create_review(review: Review):
    conn, cursor = get_connection()  # Obtain a new connection and cursor
    cursor.execute("SELECT * FROM books WHERE id = ?", (review.book_id,))
    book = cursor.fetchone()
    if book is None:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    
    cursor.execute("INSERT INTO reviews (book_id, review_text, rating) VALUES (?, ?, ?)",
                   (review.book_id, review.review_text, review.rating))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Review added successfully"}


#endpoint to fetch reviews
@app.get("/reviews/{book_id}")
def get_reviews(book_id: int):
    conn, cursor = get_connection()  # Obtain a new connection and cursor
    cursor.execute("SELECT * FROM reviews WHERE book_id = ?", (book_id,))
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not reviews:
        raise HTTPException(status_code=404, detail="Reviews not found")
    
    review_list=[]
    for review in reviews:
        review_dict={
            "id":review[0],
            "book_id": review[1],
            "review_text": review[2],
            "rating": review[3]
        }
        review_list.append(review_dict)
    
    return {"reviews": review_list}


# Background task for sending confirmation email (simulated)
def send_confirmation_email(review_id: int):
    # Simulated email sending
    print(f"Confirmation email sent for review {review_id}")
    

@app.post("/email_reviews/")
def create_review_with_email(review: Review, background_tasks: BackgroundTasks):
    # Simulate checking if the book exists
    book_exists = True 

    # Simulate adding the review to the database
    review_added = True

    if not book_exists:
        raise HTTPException(status_code=404, detail="Book not found")

    if not review_added:
        raise HTTPException(status_code=500, detail="Failed to add review")

    # Simulate sending confirmation email asynchronously
    background_tasks.add_task(send_confirmation_email, review_id=review.book_id)

    return {"message": "Review added successfully"}

