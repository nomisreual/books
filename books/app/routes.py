from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Book, Author, Address, Publisher
import sqlalchemy as sa
import sqlalchemy.orm as so


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/books')
def books():
    return render_template('books.html', title='Books')


@app.route('/authors')
def authors():
    return render_template('authors.html', title='Authors')


# List searched for books in table format. Extends base.html
@app.route('/books_table')
def books_table():
    return render_template("books_table.html",
                           title="Table of Books")


# API endpoint that returns HTML
@app.route('/search')
def search():
    q = request.args.get("q")
    if q:
        # results = Book.query.filter(Book.title.icontains(q)
        #                             | Book.author.fullname.icontains(q)).all()
        # results = Book.query.filter(Book.title.icontains(q) |
        #                             Author.fullname.icontains(q)).all()
        results = Book.query.filter(Book.title.icontains(q)).all()
    else:
        results = []

    return render_template("/search_results.html", results=results)
