import sqlite3


def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()


def add_book(title, author, user_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)", (title, author, user_id))
    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT
            books.title,
            books.author,
            users.username
        FROM books
        JOIN users ON books.user_id = users.id
    ''')
    books = cursor.fetchall()
    conn.close()
    return books


def update_book_title(book_id, new_title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()

    add_user('Kirito')
    add_user('Do ro ro')
    add_user('Alice')

    add_book('Гарри Поттер', 'Дж. Роулинг', 1)
    add_book('Преступление и наказание', 'Ф.М. Достоевский', 2)
    add_book('Метро 2033', 'Дмитрий Глуховский', 1)
    add_book('1984', 'Джордж Оруэлл', 3)

    print("Список всех книг с читателями:")
    all_books = get_all_books()
    for book in all_books:
        print(f"Книга: {book[0]}, Автор: {book[1]}, Читатель: {book[2]}")

    update_book_title(4, '1984 (Особое издание)')

    print("\nСписок всех книг после обновления:")
    all_books_updated = get_all_books()
    for book in all_books_updated:
        print(f"Книга: {book[0]}, Автор: {book[1]}, Читатель: {book[2]}")

    delete_book(3)

    print("\nСписок всех книг после удаления:")
    all_books_after_delete = get_all_books()
    for book in all_books_after_delete:
        print(f"Книга: {book[0]}, Автор: {book[1]}, Читатель: {book[2]}")