DB_APP_PREFIX = "blog_"
# синхронный движок - pg8000
DB_URL = "postgresql+pg8000://username:passwd@0.0.0.0:5435/blog"
DB_ASYNC_URL = DB_URL.replace("pg8000", "asyncpg")
# DB_ECHO = True
DB_ECHO = False