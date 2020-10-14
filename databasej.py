import sqlite3


class DatabaseContextManager(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


def create_table_books():
    query = """CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    pages INTEGER,
    library_id INTEGER,
    FOREIGN KEY (library_id) REFERENCES Library(library_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_library():
    query = """CREATE TABLE IF NOT EXISTS Library(
    library_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_book(title: str, author: str, pages: int, library_id: int):
    query = f"""INSERT INTO Books(title, author, pages, library_id) VALUES('{title}', '{author}', {pages}, {library_id})"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def get_books():
    query = """SELECT * FROM Books"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_book_title(old_title: str, new_title: str):
    query = f"""UPDATE Books
                SET title = '{new_title}'
                WHERE title = '{old_title}'"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def delete_book(title: str):
    query = f"""DELETE FROM Books
                WHERE title = '{title}'"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# LIBRARY FUNCTIONS -------------------------------------------------------------------------------------


def get_libraries():
    query = """SELECT * FROM Library"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_library_name(old_name: str, new_name: str):
    query = f"""UPDATE Library
                SET name = '{new_name}'
                WHERE name = '{old_name}'"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def delete_library(name: str):
    query = f"""DELETE FROM Library
                WHERE name = '{name}'"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def drop_table():
    query = f"""DROP TABLE Library"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def get_books_libraries():
    query = f"""SELECT * FROM Books
                JOIN Library
                    ON Books.library_id = Library.library_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def create_library(name: str, address: str):
    query = """INSERT INTO Library(name, address) VALUES(?, ?)"""
    parameters = [name, address]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


create_library("new", "sqlinjection")
get_libraries()
