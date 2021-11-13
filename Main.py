from helpers import createNewAccount
from helpers import balanceEnquiry
from helpers import depositeMoney
from helpers import withdrawMoney
from helpers import balanceEnquiry
from helpers import viewAllAccounts
from helpers import editAccount
from helpers import viewStatement
from helpers import closeAccount


# Runs infinite until exit or ctrl + c
while True:
    print("*"*129)
    print("-"*79+"Enter your choice"+"-"*79)
    print(" "*65+" Enter 1 for Open a New Account.")
    print(" "*65+" Enter 2 for Deposit Amount.")
    print(" "*65+" Enter 3 for Withdraw Amount.")
    print(" "*65+" Enter 4 for Balance Enquiry.")
    print(" "*65+" Enter 5 for view all account holder.")
    print(" "*65+" Enter 6 for Editing in account.")
    print(" "*65+" Enter 7 for view mini statement.")
    print(" "*65+" Enter 8 for Close an account.")
    print(" "*65+" Enter 9 for Exit.")
    print("*"*129)
    print("\n")
    print("\n")
    choice = int(input("Enter your choice :"))
    if(choice == 1):
        createNewAccount()
    elif(choice == 2):
        depositeMoney()
    elif(choice == 3):
        withdrawMoney()
    elif(choice == 4):
        balanceEnquiry()
    elif(choice == 5):
        viewAllAccounts()
    elif(choice == 6):
        editAccount()
    elif(choice == 7):
        viewStatement()
    elif(choice == 8):
        closeAccount()
    elif(choice == 9):
        break
