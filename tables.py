# import database instance
from database import connection

# creating tables
customer = "create table if not exists customer_info(acc_no bigint,name varchar(30),gender varchar(8),e_mail varchar(30),acc_type varchar(9),balance bigint,active int(3),primary key(acc_no))"
transaction = "create table if not exists transaction1(acc_no bigint,t_type varchar(10),t_date date,amount int,foreign key(acc_no) references customer_info(acc_no))"

cur = connection.cursor()

cur.execute(customer)
cur.execute(transaction)
