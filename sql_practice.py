import sqlite3
from config import DB_PATH


def add_post(title: str, content: str) -> None:
    add_post_query = """ 
    INSERT INTO posts(title, content) VALUES (?, ?); 
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()

    return f"Пост добавлен: {cursor.rowcount}"


def get_posts():
    get_posts_query = """ 
    SELECT * FROM posts; 
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_posts_query)
    posts = cursor.fetchall()
    connection.close()
    return posts


def delete_post(post_id: int) -> None:
    delete_post_query = """ 
    DELETE FROM posts WHERE post_id = ? 
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    return f"Удалено постов: {cursor.rowcount}"


# ? = затычка
def update_post(post_id: int, new_title: str, new_content: str) -> None:
    update_post_query = """ 
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?; 
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (
            post_id,
            new_title,
            new_content,
        ),
    )

    update_rows_count = cursor.rowcount

    connection.commit()
    connection.close()

    if update_rows_count == 0:
        return "Вова ЛОХ"
        connection.close()
    else:
        return post_id, new_title, new_content
        connection.close()


update_post(
    post_id=3,
    new_title="Обновления SQL до 3 версии",
    new_content="Скачать на офик сайте",
)
