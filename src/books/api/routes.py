from flask import Blueprint, jsonify
from data.models import Book


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return "Here are APIs being worked on."


@api.route('/books')
def get_users():
    books = Book.query.all()
    books_dictionary = {
        f"{book.id}": {
            "title": book.title,
            "year": book.year,
            "author": book.author.fullname
        } for book in books
    }
    return jsonify(book=books_dictionary, status=200,
                   mimetype='application/json')
