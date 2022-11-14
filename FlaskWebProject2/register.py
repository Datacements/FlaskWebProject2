
import configparser
import email
import sys
import pyodbc as odbc

#records = [
#   ['John', 'john@gmail.com', '34,st. eugene street,Brampton',2267535993, 'jo'], 
#   ['Sam', 'sam@gmail.com', '20,Rolling rockway street,Brampton',2467535793, 'sam123']
#]


    
name =(input("Please Enter First Name: "))
email = (input("Please Enter Email Address: "))
address = (input("Please Enter Address: "))
ph_num = int(input("Please Enter phone number:"))
passwd = (input("Please enter Password: "))

list1 = [name,email,address,ph_num,passwd]




DRIVER = 'SQL Server'
SERVER_NAME = 'KRISHNA-GANDHI\KSQL'
DATABASE_NAME = 'Logistic'

conn_string = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trust_Connection=yes;
"""

try:
    conn = odbc.connect(conn_string)
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    cursor = conn.cursor()


insert_statement = """
    INSERT INTO dbo.Customer_details 
    (customer_name,customer_email,customer_address,customer_contact,customer_password)
    VALUES (?, ?, ?, ?, ?)
"""

try:
    #for record in list1:
        #print(record)
        cursor.execute(insert_statement, list1)        
except Exception as e:
    cursor.rollback()
    print(e.value)
    print('transaction rolled back')
else:
    print('records inserted successfully')
    cursor.commit()
    cursor.close()