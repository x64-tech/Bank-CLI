from os import system, name
from database import cursor


def clearScreen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def checkExists(accNo: int):
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("Not exists")
    else:
        print(data)
