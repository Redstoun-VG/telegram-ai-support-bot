import sqlite3

conn = sqlite3.connect(
    "support.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS support_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
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
        VALUES (?, ?, ?)
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
        """
    )

    return cursor.fetchall()