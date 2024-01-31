from faker import Faker
from flask_migrate import upgrade, downgrade
from .models import db
from .models import Book, Author, Publisher, Address

import os
import sys
from contextlib import contextmanager


# Context manager to suppress output of function calls.
@contextmanager
def suppress_output():
    # Save the original stdout and stderr
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    # Open /dev/null or NUL for writing
    with open(os.devnull, 'w') as null:
        # Redirect stdout and stderr to /dev/null or NUL
        sys.stdout = null
        sys.stderr = null
        try:
            # Yield control back to the caller
            yield
        finally:
            # Restore stdout and stderr
            sys.stdout = original_stdout
            sys.stderr = original_stderr


def seed_database(number_of_records: str) -> None:
    print("Beginning the seeding process.")

    # Create a faker instance:
    fake = Faker()
    Faker.seed(1)

    print("Deleting all records across all tables...")
    # Use the suppress_output context manager to suppress output
    # of downgrade() and upgrade()
    with suppress_output():
        # Downgrade to the base revision
        downgrade(revision='base')
        upgrade()

    print("Populating all tables...")
    for _ in range(int(number_of_records)):
        # Create author:
        author = Author(fullname=fake.name(),
                        birthdate=fake.date_time())
        # Append one book to author:
        author.books.append(Book(title=fake.unique.sentence(nb_words=4),
                                 year=fake.date_time().year,
                                 isbn=fake.unique.isbn13()))
        # Create a publisher:
        publisher = Publisher(name=fake.unique.company())
        # Assign author to publisher:
        publisher.authors.append(author)
        # Create an address:
        address = Address(street=fake.street_address(),
                          city=fake.city(),
                          postal_code=fake.postcode())
        # Assign address to publisher:
        publisher.address = address
        # Add objects to session:
        db.session.add_all([author, publisher, address])

    # Commit changes:
    db.session.commit()
    print("Seeding process complete!")
