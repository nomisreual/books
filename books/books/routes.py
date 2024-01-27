from flask import Blueprint, render_template, request
from data.models import Book, Author
import sqlalchemy as sa
from sqlalchemy import or_
from data.models import db

books = Blueprint("books", __name__, template_folder="templates")


@books.route("/")
def books_table():
    return render_template("index.html",
                           title="Welcome to Bucks - a Book Database")


# API endpoint that returns HTML
@books.route('/search')
def search():
    q = request.args.get("q")
    if q:
        # results = Book.query.filter(Book.title.icontains(q)).all()
        query = sa.select(Book).join(Author) \
            .where(or_(Book.title.icontains(q),
                   Author.fullname.icontains(q)))
        results = db.session.scalars(query).all()
    else:
        results = []

    print(results)
    return render_template("search_results.html", results=results)
