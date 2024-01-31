from flask import Blueprint, jsonify
from data.models import Book, Author, Publisher, Address


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
            "author": book.author_id
        } for book in books
    }
    return jsonify(books=books_dictionary, status=200,
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
    return jsonify(authors=authors_dictionary, status=200,
                   mimetype='application/json')


@api.route('/publishers')
def get_publishers():
    publishers = Publisher.query.all()
    publishers_dictionary = {
        f"{publisher.id}": {
            "name": publisher.name,
            # "authors": [[author.id for author in authors]
            #             for authors in publishers.authors],
            "address": publisher.address.id
        } for publisher in publishers
    }
    return jsonify(publishers=publishers_dictionary, status=200,
                   mimetype='application/json')


@api.route('/addresses')
def get_addresses():
    addresses = Address.query.all()
    addresses_dictionary = {
        f"{address.id}": {
            "street": address.street,
            "city": address.city,
            "postal_code": address.postal_code,
            "publisher": address.publisher.id
        } for address in addresses
    }
    return jsonify(addresses=addresses_dictionary, status=200,
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
