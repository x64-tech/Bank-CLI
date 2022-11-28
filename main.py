import account
import transaction
from database import initDatabase
import strings


def parseInp(ins):
    if ins == 1:
        account.run()
    elif ins == 2:
        transaction.run()
    elif ins == 3:
        account.getBalance()
    elif ins == 4:
        transaction.getTransactions()
    elif ins == 5:
        account.getAll()
    else:
        print(strings.WrongInput)


if __name__ == '__main__':
    print(strings.Intro)
    initDatabase()
    working = True
    while working:
        print(strings.promptStr)
        inp = input(strings.InputCommandStr("Main"))

        if inp == "0":
            print("\nQuiting....\n")
            working = False
        else:
            parseInp(int(inp))
