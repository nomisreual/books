# Books

This is learning project in which I broaden my knowledge in various topics such as:
- Working with databases and utilizing ORMs to integrate them neatly into a web application.
- Building web applications with the Flask framework with an emphasis on data handling and building APIs
- Cherry on top: HTMX for fast implementation of useful frontend features.

## What can you do with this app?

This is a simple webpage that allows the user to search for books by, e.g. tile and name of the author. For each book, the user can access additional ressurces. For example, what other books have been authored by this author?

## Planned features:
- Improve search functionality and performance on landing page.
- Add filter options for search (maybe also what is displayed).
- Redirects to pages with details about a specific book or author.


## Local Set Up

Clone the repository and cd into the newly created directory.

Create a virtual environment, activate it an install the requirements:

```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements
```

After that you can run the application using the following command:

```
flask run
```

Out of the box, this application runs off of an in-memory SQLite database. To use another database, create a folder called *instance* in the project's root directory. Alternatively, you can run the application once as the folder will then be created if it does not exist.

In this folder, create a file called *config.py* and add one line setting the *SQLALCHEMY_DATABASE_URI*. For using a an on-disk SQLite database, the contents of *config.py* would look like this:

```
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
```

After that there is one more command to actually set up the needed tables in the database:

```
flask db upgrade
```

Note: in case of SQLite, this command also creates the database file before creating the tables. Conveniently, the created database SQLite database is stored in the same *instance* folder and as such excluded from version control.
