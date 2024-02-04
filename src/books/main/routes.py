from flask import Blueprint, render_template, request, url_for
from data.models import Book, Author
import sqlalchemy as sa
from sqlalchemy import or_
from data.models import db

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def index():
    q = request.args.get("q")
    page = request.args.get("page")
    if q and page:
        return render_template("main/index.html",
                               title="Welcome to Bucks - a Book Database",
                               q=q, page=page)
    else:
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
    page = request.args.get("page", 1, type=int)
    # if q:
    query = sa.select(Book).join(Author) \
        .where(or_(Book.title.icontains(q),
                   Author.fullname.icontains(q)))
    results = db.paginate(query, page=page,
                          per_page=20, error_out=False)

    return render_template("main/_search_results.html",
                           results=results.items,
                           q=q, page=page,
                           next=results.has_next,
                           prev=results.has_prev)
    # else:
    #     return render_template("main/_search_results.html", results=None)
