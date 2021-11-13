from tables import cur
from helpers import create_account
from helpers import bal_enq
from helpers import deposite
from helpers import withdraw
from helpers import bal_enq
from helpers import view_rec
from helpers import edit_acc
from helpers import view_st
from helpers import close_acc


# function for view mini statement->


# Main Frame
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
# Choice for add new account->
    if(choice == 1):
        create_account()
# Choice for deposite amount->
    elif(choice == 2):
        deposite()
# Choice for withdraw amount->
    elif(choice == 3):
        withdraw()
# Choice for balance inquiry->
    elif(choice == 4):
        bal_enq()
# Choice for view all account holder->
    elif(choice == 5):
        view_rec()
# Choice for edit account details->
    elif(choice == 6):
        edit_acc()
# Choice for view last 5 statements->
    elif(choice == 7):
        view_st()
# Choice for close an account->
    elif(choice == 8):
        close_acc()
# Choice for close the application->
    elif(choice == 9):
        break
