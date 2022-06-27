from datetime import datetime
from database.postgres_connector import postgres_connector
from loguru import logger
from database.data_structures import ScreenshotStatistic as SS
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('db_password')
USER = os.getenv('db_user')

dsl = {
        'dbname': 'bot',
        'user': USER,
        'password': PASSWORD,
        'host': '127.0.0.1',
        'port': 5432
    }

def create_row(row: SS):
    with postgres_connector(dsl) as pg_conn:
        cursor = pg_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS statistic (url TEXT, user_id INTEGER, created timestamp with time zone);""")
        cursor.execute(
            f"""INSERT INTO statistic (url, user_id, created) VALUES (%s, %s, %s);""", (row.url, row.user_id, row.created))
        pg_conn.commit()
        cursor.close()


def get_statistic():
    today = datetime.today()
    with postgres_connector(dsl) as pg_conn:
        cursor = pg_conn.cursor()
        cursor.execute(
            """SELECT * FROM statistic WHERE created < %s;""", (today,))
        result = cursor.fetchall()
        cursor.close()
        return result