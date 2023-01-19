from read_write import read
from add import add_user, add_user_account


user = read(r'bank-app\users.json')
account = read(r'bank-app\accounts.json')


def login(email):
    email_list = user.keys()
    if email in email_list:
        password = input("What is your password ")
        correct_password = user[email]["password"]
        if password == correct_password:
            name = user[email]["name"]
            id = user[email]["id"]
            account_info = account[id]
            account_no = account_info["account_no"]
            account_type = account_info["account_type"]
            account_bal = account_info["account_balance"]

            print (f"***********Hello {name} welcome ***********\n")
            print (f"ACC_NO: \t {account_no}")
            print (f"ACC_TYPE: \t {account_type}")
            print (f"ACC_BAL: \t {account_bal}")
        else:
            print (f"WRONG PASSWORD FOR {email}")
    else:
        print(f"SORRY, {email} DOES NOT EXIST \n")
        reg = input("WOULD YOU LIKE TO REGISTER?  [y or n] ")
        if reg.upper() == "Y":
            register(email)
        else:
            print ("*****BYE*****")

def register(email):
    if email in user:
        print (f"{email} IS ALREADY REGISTERED \n")
        log = input("WOULD YOU LIKE TO LOGIN? [y or n] ")
        if log.upper() == "Y":
            login(email)
        else:
            print ("*****BYE*****")
    else:
        name = input ("What is your name ")
        password = input("What is your password ")
        acc_no = input("What is your account number ")
        acc_type = input("Account type [Savings or Current] ")
        acc_bal = int(input("What is your account balance "))
        add_user(email,name,password)
        add_user_account(email, acc_no, acc_type, acc_bal )
