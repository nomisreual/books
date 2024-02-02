from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer, UniqueConstraint, \
    Column, Table
from sqlalchemy.orm import Mapped, \
    mapped_column, relationship
from datetime import datetime

from extensions import db

authorpublisher = Table(
    "authorpublisher",
    db.metadata,
    Column("author_id", ForeignKey("authors.id"), primary_key=True),
    Column("publisher_id", ForeignKey("publishers.id"), primary_key=True)
)


class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    year: Mapped[int] = mapped_column(Integer())
    isbn: Mapped[Optional[str]] = mapped_column(String(64), index=True,
                                                unique=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, \
        title={self.title!r})"


class Author(db.Model):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(256))
    birthdate: Mapped[datetime]

    books: Mapped[List["Book"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    publishers: Mapped[List["Publisher"]] = relationship(
        secondary=authorpublisher,
        back_populates="authors"
    )

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, \
        fullname={self.fullname!r})"


class Publisher(db.Model):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))

    authors: Mapped[List["Author"]] = relationship(
        secondary=authorpublisher,
        back_populates="publishers"
    )

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))

    address: Mapped["Address"] = relationship(back_populates="publisher",
                                              single_parent=True)

    __table_args__ = (UniqueConstraint("address_id"),)

    def __repr__(self) -> str:
        return f"Publisher(id={self.id!r}, \
        fullname={self.name!r})"


class Address(db.Model):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(128))
    city: Mapped[str] = mapped_column(String(128))
    postal_code: Mapped[str] = mapped_column(String(128))

    publisher: Mapped["Publisher"] = relationship(back_populates="address",
                                                  cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r})"
