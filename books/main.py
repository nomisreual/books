from app import create_app

import sqlalchemy as sa
import sqlalchemy.orm as so

from data.models import Book, Author, Publisher, Address
from data.models import db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "so": so, "db": db,
            "Book": Book, "Author": Author,
            "Publisher": Publisher, "Address": Address}
