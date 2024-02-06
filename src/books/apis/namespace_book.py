from flask_restx import Namespace, Resource, fields

from http import HTTPStatus

from data.models import Book

api = Namespace("books", description="Data on Books.")

# Models


book_model_4 = api.model("Book Light", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
})

# Prevent circular imports
from .namespace_author import author_model_3

book_model_5 = api.model("Book", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
    "author": fields.Nested(author_model_3)
})

# Routes


@api.route("/books")
class BooksAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.marshal_list_with(book_model_5)
    def get(self):
        return Book.query.all()


@api.route("/books/<int:id>")
class BookAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @api.marshal_with(book_model_5)
    def get(self, id):
        book = Book.query.get(id)
        if book:
            return book
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")
