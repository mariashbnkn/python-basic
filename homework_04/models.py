"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import (
    sessionmaker, declared_attr,
)

from sqlalchemy.orm import declarative_base

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text,
    DateTime,
    func,
)

from sqlalchemy.orm import (
    relationship,
)


ASYNC_PG_CONN_URI = "postgresql+asyncpg://username:passwd@0.0.0.0:5432/dz"
DB_ECHO = False


async_engine = create_async_engine(
    url=ASYNC_PG_CONN_URI,
    echo=DB_ECHO,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"dz_{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, unique=True)


Base = declarative_base(cls=Base)

Session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession)


class User(Base):
    name = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=True)
    email = Column(String(180), unique=True)
    posts = relationship(
        "Post",
        back_populates="user",
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at})"

    def __repr__(self):
        return str(self)


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("dz_users.id"),
        unique=False,
        nullable=False,
    )
    title = Column(
        String(90),
        nullable=False,
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )
    user = relationship(
        "User",
        back_populates="posts",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)



