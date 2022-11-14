
import configparser
import email
import sys
import pyodbc as odbc
import re


email = (input("Please Enter Email Address: "))
passwd = (input("Please enter Password: "))


# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# Define a function for
# for validating an Email
def check():
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

list_login = [email,passwd]

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



select_statement = """
    SELECT customer_email,customer_password FROM dbo.Customer_details 
"""


try:
    #for record in list1:
        #print(record)
        cursor.execute(select_statement) 
        row=cursor.fetchall()
        #print (row)

        
     #for rec in row:

        for record in row:

            if record[0] == email:
                print("That username is stored")

            if record[1] == passwd:
                print("That is a valid password")

            else:
                print("Your credentials are incorrect.")



except Exception as e:  
    cursor.rollback()
    print(e.value)
    print('transaction rolled back')
else:
    #print('records fetched successfully')
    cursor.commit()
    cursor.close()

 



