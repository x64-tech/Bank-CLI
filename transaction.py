from strings import TransactionPromptStr, InputCommandStr
from extras import clearScreen


def deposit():
    pass


def withdraw():
    pass


def transfer():
    pass


def parseInp(ins):
    pass


def main():
    transaction: bool = True
    while transaction:
        print(TransactionPromptStr)
        ins = input(InputCommandStr("Transaction"))
        if ins == "4":
            print("\nGoing Back....\n")
            transaction = False
        else:
            parseInp(ins)
