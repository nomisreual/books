from faker import Faker
import sqlalchemy as sa

from .models import db
from .models import Book, Author, Publisher, Address


def seed_database():
    print("Beginning the seeding process.")
    # Create a faker instance:
    fake = Faker()
    Faker.seed(1)
    # Delete all entries for Author. Automatically removes
    # entries for Book
    print("Deleting all existing records across all tables...")
    query = sa.select(Author)
    results = db.session.scalars(query)
    for result in results:
        db.session.delete(result)
    # Delete all entries for Publisher. Automatically removes
    # entries for Address
    query = sa.select(Publisher)
    results = db.session.scalars(query)
    for result in results:
        db.session.delete(result)

    print("Populating all tables...")
    for _ in range(10000):
        db.session.add(
            Book(
                title=fake.unique.sentence(nb_words=4),
                year=fake.date_time().year,
                isbn=fake.unique.isbn13(),
                author=Author(
                    fullname=fake.name(),
                    birthdate=fake.date_time()
                )
            ))
        db.session.add(
            Publisher(
                name=fake.unique.company(),
                address=Address(
                    street=fake.street_address(),
                    city=fake.city(),
                    postal_code=fake.postcode()
                )
            ))
    db.session.commit()
    print("Seeding process complete!")
