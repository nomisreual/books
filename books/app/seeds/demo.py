from app import db
from models import Book, Author, Publisher, Address
from faker import Faker
from flask_seeder import Seeder


class DemoSeeder(Seeder):
    def run(self):
        # Create a faker instance:
        fake = Faker()
        Faker.seed(1)

        print("Start seeding...")
        # Populate the database with fake entries:
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
