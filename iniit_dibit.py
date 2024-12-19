import sqlite3
from config import DB_PATH


create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    TITLE TEXT NOT NULL,
    content TEXT NULL
);
"""


connection = sqlite3.connect(DB_PATH)
print(connection)
cursor = connection.cursor()
cursor.execute(create_posts_table)
connection.commit()
connection.close()
print("таблица posts создана")
