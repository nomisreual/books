from faker import Faker
# import sqlalchemy as sa
from flask_migrate import upgrade, downgrade

from .models import db
from .models import Book, Author, Publisher, Address


def seed_database(number_of_records: str) -> None:
    print("Beginning the seeding process.")
    # Create a faker instance:
    fake = Faker()
    Faker.seed(1)
    downgrade()
    upgrade()

    # query = sa.select(Author)
    # results = db.session.scalars(query)
    # for result in results:
    #     db.session.delete(result)
    # # Delete all entries for Publisher. Automatically removes
    # # entries for Address
    # query = sa.select(Publisher)
    # results = db.session.scalars(query)
    # for result in results:
    #     db.session.delete(result)

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
