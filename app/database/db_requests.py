from datetime import datetime
from postgres_connector import postgres_connector
from loguru import logger
from data_structures import ScreenshotStatistic as SS
from dotenv import load_dotenv
import os

load_dotenv()

DSL = os.getenv('dsl')

def create_row(row: SS):
    with postgres_connector(DSL) as pg_conn:
        cursor = pg_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXIST statistic (
            url TEXT, 
            user_id INTEGER, 
            created DATETIME);"""
            )
        cursor.execute(f"""INSERT INTO statistic (%s, %s, %s);""", (row.url, row.user_id, row.created))
        cursor.close()


