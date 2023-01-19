import datetime
import json

date = str(datetime.datetime.now())

users = {"p@gmail.com":{"id":date, "name": "prisca", "password":"123"}}
accounts = {date:{"account_no":"01235674", "account_name":"prisca matthews", "account_type":"savings", "account_balance":6500}}

def write(content, filename):
    with open (filename, "w") as file:
        json.dump(content, file)
#    print("Write Successful")

# write(users, r'bank-app\users.json')
# write(accounts, r'bank-app\accounts.json')

def read(filename):
    with open (filename, 'r') as file:
        data = json.load(file)
        return (data)

# c = read(r'bank-app\users.json')
# print(c)
