import datetime
from strings import TransactionPromptStr, InputCommandStr
from database import cursor, conn


def deposit():
    accNo = int(input("Enter Account No. : "))
    data = cursor.execute("select balance from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("\nUser Not exists...")
        return
    amount = int(input("Enter Amount (int only) : "))
    if amount < 0:
        print("amount should be only positive integer ")
        return
    userBalancer = int(data[0])
    cursor.execute("update users set balance=? where accountNo=?;", (amount + userBalancer, accNo))
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("insert into Transactions values (?,?,?,?,?,?)", (None, "bank", "credit", amount, accNo, date))
    conn.commit()

    print(f"amount deposited at {date}")


def withdraw():
    accNo = int(input("Enter Account No. : "))
    data = cursor.execute("select balance from users where accountNo=?;", (accNo,)).fetchone()
    if data is None:
        print("\nUser Not exists...")
        return
    userBalancer = int(data[0])
    amount = int(input("Enter Amount (int only) : "))
    if amount < 0:
        print("amount should be only positive integer ")
        return
    elif amount > userBalancer:
        print("Not enough amount ....")
        return
    cursor.execute("update users set balance=? where accountNo=?;", (userBalancer - amount, accNo))
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("insert into Transactions values (?,?,?,?,?,?)", (None, "bank", "debit", amount, accNo, date))
    conn.commit()

    print(f"amount withdraw at {date}")


def transfer():
    senderAcc = int(input("Enter Sender Account No. : "))
    senderData = cursor.execute("select balance from users where accountNo=?;", (senderAcc,)).fetchone()
    if senderData is None:
        print("\nSender Not exists...")
        return
    receiverAcc = int(input("Enter Receiver Account No. : "))
    receiverData = cursor.execute("select balance from users where accountNo=?;", (receiverAcc,)).fetchone()
    if receiverData is None:
        print("\nReceiver Not exists...")
        return
    senderBal = int(senderData[0])
    receiverBal = int(receiverData[0])
    amount = int(input("Enter Amount (int only) : "))
    if amount > senderBal:
        print("Not enough amount ....")
        return
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("update users set balance=? where accountNo=?;", (senderBal - amount, senderAcc))
    cursor.execute("insert into Transactions values (?,?,?,?,?,?)",
                   (None, receiverAcc, "debit", amount, senderAcc, date))
    cursor.execute("update users set balance=? where accountNo=?;", (amount + receiverBal, receiverAcc))
    cursor.execute("insert into Transactions values (?,?,?,?,?,?)",
                   (None, senderAcc, "debit", amount, receiverAcc, date))
    conn.commit()
    print(f"amount transferred success at {date}")


def getTransactions():
    accNo = int(input("Enter Account No. : "))
    data = cursor.execute("select * from Transactions where accountNo=?;", (accNo,)).fetchall()
    if data is None:
        print("\nTransactions Not exists...")
        return
    print(f"""
        displaying {str(len(data))} transactions
        """)
    for tr in data:
        print(f"""
        ID:{tr[0]}
        prior:{tr[1]},
        type:{tr[2]},
        amount:{tr[3]},
        date:{tr[5]}
        """)


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
        print(TransactionPromptStr)
        ins = input(InputCommandStr("Transaction"))
        if ins == "4":
            print("\nGoing Back....\n")
            transaction = False
        else:
            parseInp(ins)

