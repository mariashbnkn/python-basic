"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Base, User, async_engine, Post, Session


async def create_user(session: AsyncSession, users_data):
    for u_d in users_data:
        user = User(
            id=u_d.get('id'),
            username=u_d.get('username'),
            name=u_d.get('name'),
            email=u_d.get('email'),
        )
        session.add(user)


async def create_post(session: AsyncSession, posts_data):
    for p_d in posts_data:
        post = Post(
            id=p_d.get('id'),
            user_id=p_d.get('userId'),
            title=p_d.get('title'),
            body=p_d.get('body'),
        )
        session.add(post)


async def async_main():
    async with Session() as session:
        async with async_engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)
        users_data: List[dict]
        posts_data: List[dict]
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )
        await create_user(session=session, users_data=users_data)
        await create_post(session=session, posts_data=posts_data)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(async_main())
