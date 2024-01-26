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

### For contributors and the curious:

## Connecting to a local postgreSQL database:
Create a file in ./books and ./data called *database.env* setting the following environmental variable:
*SQLALCHEMY_DATABASE_URI*

The value should be set like this: *postgresql://username:password@host/database_name*
