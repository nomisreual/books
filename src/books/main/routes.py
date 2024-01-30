from flask import Blueprint, render_template, request
from data.models import Book, Author
import sqlalchemy as sa
from sqlalchemy import or_
from data.models import db

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def index():
    return render_template("main/index.html",
                           title="Welcome to Bucks - a Book Database")


@main.route("/book_details/<int:id>")
def book_details(id):
    query = sa.select(Book).where(Book.id == id)
    result = db.session.scalars(query).all()[0]

    return render_template("main/book_details.html", result=result)


@main.route("/author_details/<int:id>")
def author_details(id):
    query = sa.select(Author).where(Author.id == id)
    result = db.session.scalars(query).all()[0]

    return render_template("main/author_details.html", result=result)

# API endpoint that returns HTML


@main.route('/search')
def search():
    q = request.args.get("q")
    if q:
        query = sa.select(Book).join(Author) \
            .where(or_(Book.title.icontains(q),
                       Author.fullname.icontains(q)))
        results = db.session.scalars(query).all()
    else:
        results = []

    return render_template("main/search_results.html", results=results)
