import test_main
from fastapi.testclient import TestClient
from main import app

# Instantiate a test client
client = TestClient(app)

# Define test cases for the endpoints

def test_create_book():
    # Test creating a book
    response = client.post("/books/", json={"title": "Test Book", "author": "Test Author", "publication_year": 2022})
    assert response.status_code == 200
    assert response.json() == {"message": "Book added successfully"}
    print("Test create book!!")

def test_get_books():
    # Test retrieving all books
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()["books"]) > 0
    print("Test get book!!")

def test_create_review():
    # Test creating a review
    response = client.post("/reviews/", json={"book_id": 1, "review_text": "Great book", "rating": 5})
    assert response.status_code == 200
    assert response.json() == {"message": "Review added successfully"}
    print("Test create reviews!!")

def test_get_reviews():
    # Test retrieving reviews for a book
    response = client.get("/reviews/1")
    assert response.status_code == 200
    assert len(response.json()["reviews"]) > 0
    print("Test get reviews!!")

def test_create_review_with_email():
    # Test creating a review with email
    response = client.post("/email_reviews/", json={"book_id": 1, "review_text": "Great book", "rating": 5})
    assert response.status_code == 200
    assert response.json() == {"message": "Review added successfully"}
    print("Test create review email!!")
