from flask_restx import Namespace, Resource, fields
from .namespace_publisher import publisher_model_3

from http import HTTPStatus

from data.models import Author

api = Namespace("authors", description="Data on Authors.")

# Models

author_model_3 = api.model("Author Extended", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
})

author_model_4 = api.model("Author Light", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "publishers": fields.List(fields.Nested(publisher_model_3))
})

from .namespace_book import book_model_4

author_model_5 = api.model("Author", {
    "id": fields.Integer,
    "fullname": fields.String,
    "birthdate": fields.Date,
    "publishers": fields.List(fields.Nested(publisher_model_3)),
    "books": fields.List(fields.Nested(book_model_4))
})

# Routes


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
