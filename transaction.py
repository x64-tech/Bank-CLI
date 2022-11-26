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
    pass


def transfer():
    pass


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
run()