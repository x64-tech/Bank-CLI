from database import cursor, conn
from extras import clearScreen
from strings import AccountPromptStr, InputCommandStr


def createAcc():
    clearScreen()
    print("all details are required, q to cancel\n")
    name = input("Enter Name : ")
    email = input("Enter Email : ")
    balance = int(input("Enter Balance : "))

    if name == "q" or email == "q":
        print("okk, canceling")
    cursor.execute("insert into users values (?,?,?,?);", (None, name, email, balance,))
    conn.commit()
    print(f"\nuser account is created with acc no. {str(cursor.lastrowid)}")


def updateAcc():
    clearScreen()
    accNo = int(input("Enter your acc no. : "))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("\nUser Not exists...")
        return

    print("Enter your details to update, q to cancel\n")
    name = input(f"Enter name ({data[1]}) : ")
    email = input(f"Enter name ({data[2]}) : ")
    if name == "q" or email == "q":
        print("okk, canceling")
        return
    cursor.execute("update users set name=?, email=? where accountNo=?", (name, email, accNo,))
    conn.commit()
    print(f"\nuser account is updated with acc no. {str(accNo)}")


def getOne():
    accNo = int(input("Enter your acc no. : "))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("\nUser Not exists...")
        return
    print(f"""
        Account No. {data[0]}
        Name : {data[1]}
        email : {data[2]}
        Balance : {data[3]}
        """)


def getAll():
    data = cursor.execute("select * from users;").fetchall()
    print(f"displaying {str(len(data))} users\n")
    for user in data:
        print(f"""
        Account No. {user[0]}
        Name : {user[1]}
        email : {user[2]}
        Balance : {user[3]}
        """)


def deleteAcc():
    accNo = int(input("Enter Account No. : "))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("\nUser Not exists...")
        return
    if input(f"Confirm to delete acc no. {accNo} user ? (y to confirm)") == "y":
        cursor.execute("delete from users where accountNo=?", (accNo,))
        conn.commit()
        print(f"Account no. {accNo} user deleted successfully...")
    else:
        print("okk... canceled ")


def parseInp(inp):
    if inp == "1":
        createAcc()
    elif inp == "2":
        updateAcc()
    elif inp == "3":
        getOne()
    elif inp == "4":
        deleteAcc()

    else:
        print("wrong input...")


def run():
    account: bool = True
    while account:
        print(AccountPromptStr)
        ins = input(InputCommandStr("Account"))
        if ins == "5":
            print("\nGoing Back....\n")
            account = False
        else:
            parseInp(ins)
