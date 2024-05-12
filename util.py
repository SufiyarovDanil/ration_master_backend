import sqlite3


def fill_db() -> None:
    connection = sqlite3.connect('./app.db')
    cursor = connection.cursor()

    with  open('./res/init.sql', encoding='utf-8') as f:
        for cmd in f.read().split(';'):
            cursor.execute(cmd)

    connection.commit()
    connection.close()


fill_db()
