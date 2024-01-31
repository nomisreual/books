from flask import Blueprint, jsonify
from data.models import Book, Author


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return "Here are APIs being worked on."


@api.route('/books')
def get_books():
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


@api.route('/authors')
def get_authors():
    authors = Author.query.all()
    authors_dictionary = {
        f"{author.id}": {
            "full_name": author.fullname,
            "birthdatet": author.birthdate.date(),
            "books": [book.id for book in author.books]
        } for author in authors
    }
    return jsonify(book=authors_dictionary, status=200,
                   mimetype='application/json')


@api.route('/books/<int:id>')
def get_book(id: int):
    book = Book.query.filter_by(id=id).first()
    if book:
        book_dictionary = {
            f"{book.id}": {
                "title": book.title,
                "year": book.year,
                "author": book.author.fullname
            }
        }
        return jsonify(book=book_dictionary, status=200,
                       mimetype='application/json')
    return jsonify(message="No result", status=204,
                   mimetype='application/json')


@api.route('/authors/<int:id>')
def get_author(id: int):
    author = Author.query.filter_by(id=id).first()
    if author:
        author_dictionary = {
            f"{author.id}": {
                "full_name": author.fullname,
                "birthdatet": author.birthdate.date(),
                "books": [book.id for book in author.books]
            }
        }
        return jsonify(author=author_dictionary, status=200,
                       mimetype='application/json')
    return jsonify(message="No result", status=204,
                   mimetype='application/json')
