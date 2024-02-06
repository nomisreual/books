from flask import Blueprint
from flask_restx import Api

# from .namespace_address import api as address
# from .namespace_author import api as author
# from .namespace_book import api as book
# from .namespace_publisher import api as publisher
from .routes import api as book_data

apis_bp = Blueprint("apis", __name__, url_prefix="/apis")

api = Api(
    app=apis_bp,
    title="Get from the books database.",
    version="1.0",
    description="Get data on books, authors\
                 and publishers."
)

# api.add_namespace(address)
# api.add_namespace(author)
# api.add_namespace(book)
# api.add_namespace(publisher)
api.add_namespace(book_data)
