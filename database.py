import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS support_requests (
id SERIAL PRIMARY KEY,
user_id BIGINT,
username TEXT,
question TEXT
)
"""
)

conn.commit()

def save_request(
user_id,
username,
question
):


    cursor.execute(
    """
    INSERT INTO support_requests
    (user_id, username, question)
    VALUES (%s, %s, %s)
    """,
    (
        user_id,
        username,
        question
    )
)

conn.commit()


def get_requests():


    cursor.execute(
    """
    SELECT * FROM support_requests
    ORDER BY id DESC
    """
)

    return cursor.fetchall()


