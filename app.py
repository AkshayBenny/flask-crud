from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "name": "The Lord of the Rings", "author": "JRR Tolkien"},
    {"id": 2, "name": "The Hobbit", "author": "JRR Tolkien"},
]


# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    return books


# Get book by id
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book

    return {"error": "Book not found. Try again later."}


# Create a new book
@app.route("/books/create", methods=["POST"])
def create_book():
    new_book = {"id": len(
        books) + 1, "name": request.json["name"], "author": request.json["author"]}
    books.append(new_book)

    return books


# Update a book
@app.route("/books/update/<int:book_id>", methods=["PUT"])
def update_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            book["name"] = request.json["name"]
            book["author"] = request.json["author"]

    return books


# Delete a book
@app.route("/books/delete/<int:book_id>", methods=["DELETE"])
def delete_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book["id"])

    return books


if __name__ == "__main__":
    app.run(debug=True)
