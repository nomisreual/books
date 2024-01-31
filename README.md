# Books

This is a learning project in which I broaden my knowledge in various topics such as:
- Working with databases and utilizing ORMs to integrate them neatly into a web application.
- Building web applications with the Flask framework with an emphasis on data handling and building APIs
- Cherry on top: HTMX for fast implementation of useful frontend features.

## What can you do with this app?

This is a simple webpage that allows the user to search for books by, e.g. tile and name of the author. For each book, the user can access additional ressurces. For example, what other books have been authored by this author?

## Current design issues:
- [ ] The database model doesn't establish a relationship between books and publishers.

## Planned features:
- [x] Improve search functionality and performance on landing page.
- [ ] Add filter options for search:
    - precision of search (perfect match vs loose match)
- [x] Redirects to pages with details about a specific book or author.
- [ ] Filling the database with more real data (in development a database with 10 000 records of dummy data is in use,
- [ ] Adding APIs making the data more accessible (*in progress, see down below*).
the live demo currently has 500 records due to hosting limitations).

Checked off features already made it into the application.

## Possible features:
- User login system to facilitate bookmarking certain books, or follow authors.

## Maybe features:
- Build a flask extension that eases prepopulating a database with real or fake data. It should also allow for an easy database teardown (deleting all records across tables). [Update: 29.01.2024] So far I created a custom flask command called *flask seeding* to make it easier for this project.

## APIs

APIs are currently worked on. Every API is prefixed with `/api`. One API endpoint is already live, namely `/api/books` returning information about each book in the database in JSON format.

## Local Set Up

Clone the repository and cd into the newly created directory. 

```
cd ./books/
```

Create a virtual environment, activate it an install the requirements:

```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

Out of the box, this application runs off of an on-disk SQLite database. To use another database, do the following: create a file called *database.env* inside of the *instance* folder and include a line setting *PRODUCTION_DATABASE". The *instance* is created whenever the first *flask* command is called. Alternatively, just create it to make sure you use your database and proceed with the next steps afterwards:

```
mkdir instance
echo PRODUCTION_DATABASE=sqlite:///example.db > ./instance/database.env
```

The example above sets the production database key to use a SQLite database. You can use any other relational database that is supported by SQLAlchemy.

After that, create the database tables with this command:

```
flask db upgrade
```

Note: in case of SQLite, this command also creates the database file before creating the tables. Conveniently, the created database SQLite database is stored in the same *instance* folder and as such excluded from version control.

Prepolutating the database with dummy data using the following command:

```
flask seeding
```

After that you can run the application using the following command:

```
flask run
```

