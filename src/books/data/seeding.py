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
    db.drop_all()
    # Make sure table "alembic_version" is created if not there.
    with suppress_output():
        upgrade()

    db.create_all()
    print("Populating all tables...")
    for _ in range(int(number_of_records)):
        author = Author(fullname=fake.name(),
                        birthdate=fake.date_time())
        book = Book(title=fake.unique.sentence(nb_words=4),
                    year=fake.date_time().year,
                    isbn=fake.unique.isbn13(),
                    author=author)
        publisher = Publisher(name=fake.unique.company())

        address = Address(street=fake.street_address(),
                          city=fake.city(),
                          postal_code=fake.postcode())
        publisher.address = address
        publisher.authors.append(author)
        db.session.add_all([author, book, publisher, address])

    db.session.commit()
    print("Seeding process complete!")
