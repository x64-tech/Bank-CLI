import strings
from database import cursor, conn
from extras import clearScreen


def createAcc():
    print(strings.RequiredInput)
    name = input(strings.NameInput(""))
    email = input(strings.EmailInput(""))
    balance = int(input(strings.BalanceInput))

    if name == "0" or email == "0":
        print(strings.CancelProcess("Create Account"))
        return

    cursor.execute("insert into users values (?,?,?,?);", (None, name, email, balance,))
    conn.commit()
    print(strings.ProcessCompleted("Created", str(cursor.lastrowid)))


def updateAcc():
    clearScreen()
    print(strings.RequiredInput)
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    name = input(strings.NameInput({data[1]}))
    email = input(strings.EmailInput({data[2]}))
    if name == "0" or email == "0":
        print(strings.CancelProcess("Update Account"))
        return
    cursor.execute("update users set name=?, email=? where accountNo=?", (name, email, accNo,))
    conn.commit()
    print(strings.ProcessCompleted("Updated", str(accNo)))


def getOne():
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    print(strings.AccountInfo(data[0], data[1], data[2], data[3]))


def getAll():
    data = cursor.execute("select * from users;").fetchall()
    print(strings.DisplayingContent(str(len(data)), "Users"))
    for user in data:
        print(strings.AccountInfo(user[0], user[1], user[2], user[3]))


def deleteAcc():
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select * from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    if input(strings.ConfirmDeletion(str(accNo))) == "y":
        cursor.execute("delete from users where accountNo=?", (accNo,))
        conn.commit()
        print(strings.ProcessCompleted("Deleted", str(accNo)))
    else:
        print(strings.CancelProcess("Delete Account"))


def getBalance():
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select name, balance from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    print(strings.Balance(data[0], data[1]))


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
        print(strings.AccountPromptStr)
        ins = input(strings.InputCommandStr("Account"))
        if ins == "0":
            print(strings.Back)
            account = False
        else:
            parseInp(ins)
