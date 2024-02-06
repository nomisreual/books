from flask_restx import Namespace, Resource, fields

api = Namespace("address", description="Data on Addresses.")

# Models

address_model_4 = api.model("Address", {
    "id": fields.Integer,
    "stree": fields.String,
    "city": fields.String,
    "postal_code": fields.String
})

# Routes
