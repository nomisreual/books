from flask_restx import Namespace, Resource, fields
from .namespace_address import address_model_4

from http import HTTPStatus

from data.models import Publisher

api = Namespace("publishers", description="Data on Publishers.")

# Models

publisher_model_3 = api.model("Publisher Light", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model_4)
})

# Prevent circular imports:
from .namespace_author import author_model_3

publisher_model_4 = api.model("Publishers", {
    "id": fields.Integer,
    "name": fields.String,
    "address": fields.Nested(address_model_4),
    "authors": fields.List(fields.Nested(author_model_3))
})

# Routes


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
