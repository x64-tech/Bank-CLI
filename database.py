import sqlite3
from strings import AccountTableStr, TransTableStr

conn = sqlite3.connect("bank.sqlite3")
cursor = conn.cursor()


def initDatabase():
    try:
        cursor.execute(AccountTableStr)
        cursor.execute(TransTableStr)
    except Exception as e:
        print(e)


initDatabase()
