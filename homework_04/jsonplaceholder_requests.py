"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data(url=USERS_DATA_URL):
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list = await response.json()
            return data


async def fetch_posts_data(url=POSTS_DATA_URL):
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list = await response.json()
            return data
