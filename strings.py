promptStr = """
[1] Accounts Stuff
[2] Perform Transaction
[3] Check Balance
[4] All Accounts
[Q] Exit
"""

AccountPromptStr = """
[1] Create Account
[2] Update Account
[3] Search Account
[4] Delete Account
[5] Go Back
"""

TransactionPromptStr = """
[1] Deposit Amount
[2] Withdraw Amount
[3] Transfer Amount
[4] Go Back
"""

InputCommandStr = lambda stage: f"[{stage}] your command > "

AccountTableStr = """create table if not exists users (accountNo integer primary key autoincrement, name varchar(50), 
email varchar(50), balance integer) """

TransTableStr = """create table if not exists Transactions (transID integer primary key autoincrement, prior varchar(50),
 type varchar(50), amount integer, accountNo integer, date varchar(50))"""
