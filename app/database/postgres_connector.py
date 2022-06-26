from contextlib import contextmanager

import psycopg2


@contextmanager
def postgres_connector(dsn: dict):
    conn = psycopg2.connect(**dsn)
    yield conn
    conn.close()