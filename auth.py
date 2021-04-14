#register
# - first name, last name, password, email
# - generate user account

#login
# - account number & password

#bank operations

#Initializing the system

import random
import time

database = {} #dictionary
global balance
def init():

    
    print("Welcome to bankPHP")
    
    haveAccount = int(input("Do you have an account with us? 1 (Yes)  2 (No) \n"))
    
    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option")
        init()

def login():
    print("******** Login ********")

    accountNumberFromUser = int(input("What is your number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                isLoginSuccessful = True

    print('Invalid account number or password entered')

def register():
    print("****** Register ******")

    email = input("What is your e-mail address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a new password \n")
    
    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created")
    print("== ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure to keep it safe")
    print("== ==== ====== ===== ===")

    login()

def bankOperation(user):
    print("Welcome %s %s " % ( user[0], user[1]))
    selectedOption = int(input("Please select an option. \n1. Deposit \n2. Withdrawal \n3. Log Out \n4. Exit \n"))
    
    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()
    
    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        print("Goodbye")
        exit()

    else:
        print("Invalid option entered")
        bankOperation(user)

def depositOperation():
    deposit = float(input("How much would you like to deposit? \n"))
    login()

def withdrawalOperation():
    withdraw = float(input("How much would you like to withdraw? \n"))
    if(withdraw > 0):
        print('Please take your cash')
        time.sleep(1)
        login()
        
    elif(withdraw <= 0):
        print('Invalid entry. Withdrawal amount must be greater than zero.')


def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()





    

### ACTUAL BANKING SYSTEM ###

init()