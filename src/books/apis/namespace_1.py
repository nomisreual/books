from flask_restx import Namespace, Resource, fields

from http import HTTPStatus

from data.models import Book, Author, Publisher

api = Namespace(name="", description="Data on books,\
                 authors and publishers.")

# Defining various models:

address_model_4 = api.model("Address with four fields.", {
    "id": fields.Integer,
    "stree": fields.String,
    "city": fields.String,
    "postal_code": fields.String
})

publisher_model_3 = api.model("Publisher with three fields.", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model_4)
})

author_model_4 = api.model("Author with four fields.", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "publishers": fields.List(fields.Nested(publisher_model_3))
})

book_model_4 = api.model("Book with four fields.", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
})

author_model_5 = api.model("Author with five fields.", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "books": fields.List(fields.Nested(book_model_4)),
    "publishers": fields.List(fields.Nested(publisher_model_3))
})

author_model_3 = api.model("Author with three fields.", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
})

book_model_5 = api.model("Book with five fields.", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
    "author": fields.Nested(author_model_3)
})

publisher_model_4 = api.model("Publisher with 4 fields.", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model_4),
    "authors": fields.List(fields.Nested(author_model_3))
})

# Defining the actual routes to be exposed:


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


@api.route("/authors")
class AuthorsAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.marshal_list_with(author_model_5)
    def get(self):
        return Author.query.all()


@api.route("/authors/<int:id>")
class AuthorApi(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @api.marshal_with(author_model_5)
    def get(self, id):
        author = Author.query.get(id)
        if author:
            return author
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")


@api.route("/publishers")
class PublishersAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.marshal_list_with(publisher_model_4)
    def get(self):
        return Publisher.query.all()


@api.route("/publishers/<int:id>")
class PublisherAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @api.marshal_with(publisher_model_4)
    def get(self, id):
        publisher = Publisher.query.get(id)
        if publisher:
            return publisher
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")
