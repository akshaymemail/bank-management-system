from tables import cur
from database import connection

# To create a new bank account


def createNewAccount():
    acc_n = int(input("Enter Account no. :"))
    name = str(input("Enter name :"))
    print(" "*40+"Gender")
    print(" "*35+"Press 1 for Male")
    print(" "*35+"Press 2 for Female")
    print(" "*35+"Press 3 for Other")
    gender = int(input("Enter input for gender(1/2/3) :"))
    gen = ""
    if(gender == 1):
        gen = 'Male'
    elif(gender == 2):
        gen = 'Female'
    elif(gender == 3):
        gen = 'Other'
    e_mail = str(input("Enter mail :"))
    print(" "*30+"****Transaction Type****")
    print(" "*30+"Press 1 for Savings")
    print(" "*30+"Press 2 for Current")
    acc_type = int(input("Enter input for account type(1/2) :"))
    typ = ""
    if(acc_type == 1):
        typ = 'Savings'
    elif(acc_type == 2):
        typ = 'Current'
    amount = int(input("Enter amount :"))
    activity = 1
    insert = "insert into customer_info values(%d,'%s','%s','%s','%s',%d,%d)" % (
        acc_n, name, gen, e_mail, typ, amount, activity)
    cur.execute(insert)
    if cur.rowcount > 0:
        print(" "*35+"!!!!!Account Created!!!!!")
    else:
        print(" "*40+"!!!!!Error!!!!!")
    connection.commit()

# balance inquiry


def balanceEnquiry():
    acc_n = int(input("Enter account no. :"))
    print("-"*80)
    print("%10s\t%20s\t%10s" % ("Account_no", "Name", "Balance"))
    print("-"*80)
    qry = "Select acc_no,name,balance from customer_info where(acc_no==%d)" % (
        acc_n)
    cur.execute(qry)
    data = cur.fetchall()
    if len(data) > 0:
        for i in data:
            print("%10d\t%20s\t%10d" % (i[0], i[1], i[2]))
        print("-"*80)
    else:
        print(" "*30+"!!!!!Evaild Account Number!!!!!")

# Withdraw Money


def withdrawMoney():
    acc_n = int(input("Enter account no :"))
    t_type = 'Withdraw'
    date = str(input("Enter date(YYYY-MM-DD) :"))
    amount = int(input("Enter amount :"))
    insert = "insert into transaction1 values(%d,'%s','%s',%d)" % (
        acc_n, t_type, date, amount)
    cur.execute(insert)
    qrry = "UPDATE customer_info set balance = balance-%d where (acc_no==%d)" % (
        amount, acc_n)
    cur.execute(qrry)
    if cur.rowcount > 0:
        print(" "*35+"!!!!!Transaction Completed!!!!!")
    else:
        print(" "*40+"!!!!!Error!!!!!")
    connection.commit()


# Deposite Money to account
def depositeMoney():
    acc_n = int(input("Enter account no :"))
    trn_type = 'Deposite'
    date = str(input("Enter date(YYYY-MM-DD) :"))
    amount = int(input("Enter amount :"))
    insert = "insert into transaction1 values(%d,'%s','%s',%d)" % (
        acc_n, trn_type, date, amount)
    cur.execute(insert)
    qry = "UPDATE customer_info set balance = balance+%d where (acc_no==%d)" % (
        amount, acc_n)
    cur.execute(qry)
    if cur.rowcount > 0:
        print(" "*35+"!!!!!Transaction Completed!!!!!")
    else:
        print(" "*40+"!!!!!Error!!!!!")
    connection.commit()


# view record
def viewAllAccounts():
    print("-"*170)
    print("%10s%15s\t%8s\t%20s\t%15s\t%10s\t%12s" % ("Account_no",
          "Name", "Gender", "E_Mail", "Acc_type", "Amount", "Activity"))
    print("-"*170)
    qry = "Select * from customer_info"
    cur.execute(qry)
    data = cur.fetchall()
    for i in data:
        print("%10d%15s\t%8s\t%20s%15s\t%10d\t%12d" %
              (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    print("-"*170)


# editing in account
def editAccount():
    acc_n = int(input("Enter account no. :"))
    qry = "Select * from customer_info where(acc_no==%d)" % (acc_n)
    cur.execute(qry)
    data = cur.fetchall()
    if len(data) > 0:
        print(" "*40+"1 -> Name")
        print(" "*40+"2 -> Gender")
        print(" "*40+"3 -> E-Mail")
        ch = int(input("Enter choice for update :"))
        if ch == 1:
            name = str(input("Enter name :"))
            qry = "UPDATE customer_info set name = '%s' where(acc_no==%d)" % (
                name, acc_n)
        elif ch == 2:
            gender = str(input("Enter gender(Male/Female/Other) :"))
            qry = "UPDATE customer_info set gender = '%s' where(acc_no==%d)" % (
                gender, acc_n)
        elif ch == 3:
            email = str(input("Enter E-Mail :"))
            qry = "UPDATE customer_info set e_mail = '%s' where(acc_no==%d)" % (
                email, acc_n)
        else:
            print(" "*38+"!!!!!Invalid Choice!!!!!")
        if ch >= 1 and ch <= 3:
            cur.execute(qry)
            if cur.rowcount > 0:
                print(" "*38+"!!!!Record Updated!!!!")
            else:
                print(" "*42+"!!!!!ERROR!!!!!")
    else:
        print(" "*32+"!!!!!Invalid Account no.!!!!!")
    connection.commit()

# view statement


def viewStatement():
    acc_n = int(input("Enter account no. :"))
    print("Last 5 transaction of account no. :", acc_n)
    print("-"*80)
    print("%15s\t%15s\t%10s" % ("Trans_type", "Trans_date", "Amount"))
    print("-"*80)
    qry = "Select t_type,t_date,amount from transaction1 where(acc_no==%d) order by t_date asc limit 5" % (
        acc_n)
    cur.execute(qry)
    data = cur.fetchall()
    if len(data) > 0:
        for i in data:
            print("%15s\t%15s\t%10d" % (i[0], i[1], i[2]))
        print("-"*80)
    else:
        print(" "*32+"!!!!!Envaild Account Number!!!!!")


# close an account

def closeAccount():
    acc_n = int(input("Enter account no. :"))
    qry = "UPDATE customer_info set active = 0 where (acc_no==%d)" % (acc_n)
    cur.execute(qry)
    if cur.rowcount > 0:
        print(" "*35+"!!!!!Account Closed!!!!!")
    else:
        print(" "*40+"!!!!!Envaild Account Number!!!!!")
    connection.commit()
