from flask import Blueprint, render_template, request
from data.models import Book

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
        results = Book.query.filter(Book.title.icontains(q)).all()
    else:
        results = []

    return render_template("search_results.html", results=results)
