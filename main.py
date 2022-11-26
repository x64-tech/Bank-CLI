import account
import transaction
from database import initDatabase
from strings import promptStr, InputCommandStr


def parseInp(ins):
    if ins == 1:
        account.run()
    elif ins == 2:
        transaction.main()
    elif ins == 4:
        account.getAll()
    else:
        print("wrong input...")


if __name__ == '__main__':
    initDatabase()
    working = True
    while working:
        print(promptStr)
        inp = input(InputCommandStr("Main"))

        if inp == "q" or inp == "Q":
            print("\nQuiting....\n")
            working = False
        else:
            parseInp(int(inp))
