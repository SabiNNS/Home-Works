import sqlite3

connect = sqlite3.connect("books.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS readers(
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        reader_id INTEGER,
        FOREIGN KEY(reader_id) REFERENCES readers(rowid)
    )
''')

connect.commit()

def add_reader(name):
    cursor.execute(
        'INSERT INTO readers(name) VALUES (?)',
        (name,)
    )
    connect.commit()
    print("читатель добавлен")

def add_book(title, author, reader_id):
    cursor.execute(
        'INSERT INTO books(title, author, reader_id) VALUES (?,?,?)',
        (title, author, reader_id)
    )
    connect.commit()
    print("книга добавлена")

def get_all_books():
    cursor.execute('''
        SELECT books.title, books.author, readers.name
        FROM books
        LEFT JOIN readers ON books.reader_id = readers.rowid
    ''')
    all_books = cursor.fetchall()
    print("все книги:")
    for b in all_books:
        print("Книга:", b[0], "| Автор:", b[1], "| Читает:", b[2])

def update_book_title(title, rowid):
    cursor.execute(
        'UPDATE books SET title = ? WHERE rowid = ?',
        (title, rowid)
    )
    connect.commit()
    print("название обновлено")

def delete_book(rowid):
    cursor.execute(
        'DELETE FROM books WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print("книга удалена")

add_reader("Kirito")
add_reader("Do ro ro")
add_reader("Sabrina")

add_book("Гарри Поттер", "Дж. Роулинг", 1)
add_book("Преступление и наказание", "Ф.М. Достоевский", 2)
add_book("1984", "Джордж Оруэлл", 1)
add_book("Мастер и Маргарита", "М.А. Булгаков", 2)
add_book("Убить пересмешника", "Харпер Ли", 3)

get_all_books()