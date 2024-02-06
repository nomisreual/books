from flask import Blueprint
from flask_restx import Resource, Namespace, fields
from extensions import api
from http import HTTPStatus

from data.models import Book, Author, Publisher


api_bp = Blueprint("apis", __name__, url_prefix="/apis")
api.init_app(api_bp)

ns = Namespace("restx")
api.add_namespace(ns)

address_model = api.model("Address", {
    "id": fields.Integer,
    "stree": fields.String,
    "city": fields.String,
    "postal_code": fields.String
})

publishers_model = api.model("Publisher Light", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model)
})

author_model = api.model("Author Light", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "publishers": fields.List(fields.Nested(publishers_model))
})

book_model = api.model("Book Light", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
})


author_model_full = api.model("Author", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "books": fields.List(fields.Nested(book_model)),
    "publishers": fields.List(fields.Nested(publishers_model))
})

author_model_without_publisher = api.model("Author Extended", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
})

book_model_full = api.model("Book", {
    "id": fields.Integer,
    "title": fields.String,
    "year": fields.Integer,
    "isbn": fields.String,
    "author": fields.Nested(author_model_without_publisher)
})

publishers_model_all = api.model("Publishers", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model),
    "authors": fields.List(fields.Nested(author_model_without_publisher))
})


@ns.route("/books")
class BooksAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @ns.marshal_list_with(book_model_full)
    def get(self):
        return Book.query.all()


@ns.route("/books/<int:id>")
class BookAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @ns.marshal_with(book_model_full)
    def get(self, id):
        book = Book.query.get(id)
        if book:
            return book
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")


@ns.route("/authors")
class AuthorsAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @ns.marshal_list_with(author_model_full)
    def get(self):
        return Author.query.all()


@ns.route("/authors/<int:id>")
class AuthorApi(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @ns.marshal_with(author_model_full)
    def get(self, id):
        author = Author.query.get(id)
        if author:
            return author
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")


@ns.route("/publishers")
class PublishersAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @ns.marshal_list_with(publishers_model_all)
    def get(self):
        return Publisher.query.all()


@ns.route("/publishers/<int:id>")
class PublisherAPI(Resource):
    @api.response(HTTPStatus.OK.value, "Success")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Not Found")
    @ns.marshal_with(publishers_model_all)
    def get(self, id):
        publisher = Publisher.query.get(id)
        if publisher:
            return publisher
        else:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Not Found")
