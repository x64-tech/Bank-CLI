import datetime
import strings
from database import cursor, conn


def deposit():
    print(strings.RequiredInput)
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select balance from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    amount = int(input(strings.AmountInput))
    if amount < 0:
        print(strings.AmountError)
        return
    userBalancer = int(data[0])
    cursor.execute("update users set balance=? where accountNo=?;", (amount + userBalancer, accNo))
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("insert into transactions values (?,?,?,?,?,?)", (None, "bank", "credit", amount, accNo, date))
    conn.commit()

    print(strings.TransactionCompleted("Deposited", date))


def withdraw():
    print(strings.RequiredInput)
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select balance from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    userBalancer = int(data[0])
    amount = int(input(strings.AmountInput))
    if amount < 0:
        print(strings.AmountError)
        return
    elif amount > userBalancer:
        print("Not enough amount ....")
        return
    cursor.execute("update users set balance=? where accountNo=?;", (userBalancer - amount, accNo))
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("insert into transactions values (?,?,?,?,?,?)", (None, "bank", "debit", amount, accNo, date))
    conn.commit()

    print(strings.TransactionCompleted("Withdraw", date))


def transfer():
    senderAcc = int(input("Enter Sender Account No. : "))
    senderData = cursor.execute("select balance from users where accountNo=?;", (senderAcc,)).fetchone()
    if senderData is None:
        print(strings.NotExists(str(senderAcc)))
        return
    receiverAcc = int(input("Enter Receiver Account No. : "))
    receiverData = cursor.execute("select balance from users where accountNo=?;", (receiverAcc,)).fetchone()
    if receiverData is None:
        print(strings.NotExists(str(receiverAcc)))
        return
    senderBal = int(senderData[0])
    receiverBal = int(receiverData[0])
    amount = int(input("Enter Amount (int only) : "))
    if amount > senderBal:
        print("Not enough amount ....")
        return
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("update users set balance=? where accountNo=?;", (senderBal - amount, senderAcc))
    cursor.execute("insert into transactions values (?,?,?,?,?,?)",
                   (None, receiverAcc, "debit", amount, senderAcc, date))
    cursor.execute("update users set balance=? where accountNo=?;", (amount + receiverBal, receiverAcc))
    cursor.execute("insert into transactions values (?,?,?,?,?,?)",
                   (None, senderAcc, "debit", amount, receiverAcc, date))
    conn.commit()
    print(strings.TransactionCompleted("Transfer", date))


def getTransactions():
    accNo = int(input(strings.AccNoInput))
    data = cursor.execute("select * from transactions where accountNo=?;", (accNo,)).fetchall()
    if data is None:
        print(strings.NotExists(str(accNo)))
        return
    print(strings.DisplayingContent(str(len(data)), "Translations"))
    for tr in data:
        print(strings.TransactionInfo(tr[0], tr[1], tr[2], tr[3], tr[4]))


def parseInp(ins):
    if ins == "1":
        deposit()
    elif ins == "2":
        withdraw()
    elif ins == "3":
        transfer()

    else:
        print("wrong input...")


def run():
    transaction: bool = True
    while transaction:
        print(strings.TransactionPromptStr)
        ins = input(strings.InputCommandStr("Transaction"))
        if ins == "0":
            print(strings.Back)
            transaction = False
        else:
            parseInp(ins)
