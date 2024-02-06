from flask import Blueprint
from flask_restx import Api

from .namespace_1 import api as book_data

# Create a blueprint:
apis_bp = Blueprint("apis", __name__, url_prefix="/apis")

# Create the restx Api instance. Here passing in the blueprint,
# rather than the application model.
api = Api(
    app=apis_bp,
    title="Get from the books database.",
    version="1.0",
    description="Get data on books, authors\
                 and publishers."
)

# Add namespaces:
api.add_namespace(book_data)
