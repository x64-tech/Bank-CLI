promptStr = """
[1] Accounts Stuff
[2] Perform Transaction
[3] Check Balance
[4] Check Transaction
[5] Check Accounts
[0] Exit
"""

AccountPromptStr = """
[1] Create Account
[2] Update Account
[3] Search Account
[4] Delete Account
[0] Go Back
"""

TransactionPromptStr = """
[1] Deposit Amount
[2] Withdraw Amount
[3] Transfer Amount
[0] Go Back
"""

Intro = """
    Welcome to x64-Tech Bank
"""

AccountInfo = lambda accNo, name, email, balance: f"""
Account No. {accNo}
Name : {name}
email : {email}
Balance : {balance}
"""

TransactionInfo = lambda ID, prior, tpe, amount, date: f"""
    ID:{ID}
    prior:{prior},
    type:{tpe},
    amount:{amount},
    date:{date}
"""

EmailFormate = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
WrongInput = "\nWrong Input...\n"
RequiredInput = "\nAll inputs are required (0 to cancel)\n"

InputCommandStr = lambda stage: f"[{stage}] your command > "

EmailInput = lambda email: "Enter Your Email : " if email == "" else f"Enter Your Email {email} : "
NameInput = lambda name: "Enter Your Name : " if name == "" else f"Enter Your Name {name} : "
AccNoInput = "Enter Account No. : "
AmountInput = "Enter Amount : "
BalanceInput = "Enter Balance : "
Back = "\nGoing Back..\n"
AmountError = "\nAmount Should Be Positive Integer Only\n"
EmailError = "\nInvalid Email Format\n"

DisplayingContent = lambda total, cont: f"\nDisplaying {total} {cont}\n"
NotExists = lambda accNo: f"\nUser Not Exists With Account No. {accNo}\n"
CancelProcess = lambda process: f"\nOkk, canceling \"{process}\"\n"
ProcessCompleted = lambda process, rowID: f"\nUser account is {process} with acc no. {rowID}\n"
ConfirmDeletion = lambda accNo: f"\nDelete Account No. {accNo} User ? (y to confirm) : "
TransactionCompleted = lambda trans, date: f"\nAmount is {trans} at {date}\n"
Balance = lambda accNo, balance: f"\nCurrent Balance Of Account No. {accNo} Is {balance}\n"

AccountTableStr = """create table if not exists users (accountNo integer primary key autoincrement, name varchar(50), 
email varchar(50), balance integer) """

TransTableStr = """create table if not exists transactions (transID integer primary key autoincrement, prior varchar(50)
,type varchar(50), amount integer, accountNo integer, date varchar(50))"""
