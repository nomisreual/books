from flask import render_template, request, redirect, url_for
from app import app
from app.models import Book
# import sqlalchemy as sa
# import sqlalchemy.orm as so


@app.route("/")
@app.route("/index")
def books_table():
    return render_template("index.html",
                           title="Welcome to Bucks - a Book Database")


# API endpoint that returns HTML
@app.route('/search')
def search():
    q = request.args.get("q")
    if q:
        results = Book.query.filter(Book.title.icontains(q)).all()
    else:
        results = []

    return render_template("search_results.html", results=results)
