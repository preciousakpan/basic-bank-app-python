from datetime import datetime
from read_write import read, write

date = str(datetime.now())

def add_user(email, name, password):
    entry = {email:{"id":date, "name":name, "password":password}}
    content = read(r'C:\Users\HP\OneDrive\Desktop\ISAAC\bank-app\users.json')
#    print (cont)
    content.update(entry)
    write(content, r'C:\Users\HP\OneDrive\Desktop\ISAAC\bank-app\users.json')
    print (f"{email} added successfully")

#add_user("j@gmail.com", "jerry", "abc12")

def add_user_account(email,acc_no, acc_type, acc_bal):
    c = read(r'C:\Users\HP\OneDrive\Desktop\ISAAC\bank-app\users.json')
    user_id = c[email]["id"]    
    entry = {user_id:{"account_no":acc_no, "account_type": acc_type, "account_balance":acc_bal }}
    content = c = read(r'C:\Users\HP\OneDrive\Desktop\ISAAC\bank-app\accounts.json')
    content.update(entry)
    write(content, r'C:\Users\HP\OneDrive\Desktop\ISAAC\bank-app\accounts.json')

#add_user_account("j@gmail.com", "54673856", "current", 56900)
