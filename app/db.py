import os
from psycopg2 import pool
from app.settings import settings


connection_pool = pool.SimpleConnectionPool(1, 10, settings.DATABASE_URL)


def get_connection():
    conn = connection_pool.getconn()
    try:
        yield conn
    finally:
        connection_pool.putconn(conn)
