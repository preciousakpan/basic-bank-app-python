from login_reg import login, register

task = input("Login or Register [L or R] ")

if task.upper() == "L":
    e = input("What is your email ")
    login(e)
elif task.upper() == "R":
    e = input("What is your email ")
    register(e)        
else:
    print (f"SORRY USERS CAN NOT PERFORM {task}")
