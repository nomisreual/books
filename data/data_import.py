from csv_importer import read_csv
from data_models import Base, Book, Author, Publisher, Address
from datetime import datetime
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os
from dotenv import load_dotenv

# Load envs for connecting to Postgres DB
load_dotenv("./database.env")

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
# Path to CSV
FILE_PATH = "./books_data.csv"


def main():
    # Use an on-disk database:
    # engine = create_engine("sqlite:///app.db", echo=True)
    # Use an in-memory database:
    # engine = create_engine("sqlite://", echo=True)
    # Use postgresql database:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)

    # Create a faker instance:
    fake = Faker()
    Faker.seed(1)
    # Create the database schema:
    Base.metadata.create_all(engine)

    # start a session using our engine:
    # changes made are only applied once commited
    with Session(engine) as session:
        # bad data formatting led to ValueErrors while processing
        # abort process in that case
        # try:
        #     # for each 'line' read the values and add respective database entries to our tables
        #     for title in read_csv(FILE_PATH):
        #         print("Add entry...")
        #         session.add(
        #             Book(
        #                 title=title.get("Title"),
        #                 year=int(title.get("Publication Date")),
        #                 isbn=title.get("ISBN"),
        #                 author=Author(
        #                     fullname=title.get("Author"),
        #                     birthdate=datetime.strptime(
        #                         title.get("Birthdate"), "%B %d, %Y")
        #
        #                 )
        #             ))
        #         # Some manual data cleaning. Only had one outlier.
        #         # this dirty fix is contained within the next 3 lines
        #
        #         address_as_list = title.get("Address").split(", ")
        #         if len(address_as_list) > 3:
        #             address_as_list = address_as_list[1:]
        #         session.add(
        #             Publisher(
        #                 name=title.get("Publisher"),
        #                 address=Address(
        #                     street=address_as_list[0],
        #                     city=address_as_list[1],
        #                     postal_code=address_as_list[2]
        #                 )
        #             )
        #         )
        # except ValueError:
        #     session.reset()
        for _ in range(10000):
            session.add(
                Book(
                    title=fake.unique.sentence(nb_words=4),
                    year=fake.date_time().year,
                    isbn=fake.unique.isbn13(),
                    author=Author(
                        fullname=fake.name(),
                        birthdate=fake.date_time()
                    )
                ))
            session.add(
                Publisher(
                    name=fake.unique.company(),
                    address=Address(
                        street=fake.street_address(),
                        city=fake.city(),
                        postal_code=fake.postcode()
                    )
                ))
        session.commit()


if __name__ == "__main__":
    print("Starting seeding...")
    main()
    print("Seeding complete!")
