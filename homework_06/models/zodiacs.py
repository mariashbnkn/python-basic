from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Date

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class ZodiacBase(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    first_date = Column(Integer, primary_key=False, nullable=False)
    last_date = Column(Integer, primary_key=False, nullable=False)
    name = Column(String, nullable=False)

    if TYPE_CHECKING:
        query: Query


class Zodiacs(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    zodiac_name = Column(String)
    id_zodiac = Column(
        Integer,
        ForeignKey("zodiac_base.id"),
        unique=False,
        nullable=False,
    )
    date_bth = Column(
        Date,
    )

    if TYPE_CHECKING:
        query: Query