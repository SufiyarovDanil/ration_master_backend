import sqlite3


def fill_db() -> None:
    connection = sqlite3.connect('./app.db')
    cursor = connection.cursor()

    with  open('./res/init.sql', encoding='utf-8') as f:
        cursor.execute(f.read())

    connection.commit()
    connection.close()


fill_db()
