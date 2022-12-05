import configparser
import pyodbc as odbc
import Insert_Cur
import Insert_Past

class InsertDetails:

    def insert_Details(self):
        
        admin_entry = int(input("""\n\n\
        Press 1 if you want to add data in current transaction , 
        Press 2 if you want to add data in past transaction\n\n"""))

        if(admin_entry ==1):

            details = "Please add the details"            
            print(details)
            insertcurfun()
        
        elif(admin_entry ==2):
            details = "Please add the details"
            print(details)
            insertpastfun()

        else:
            pass


            

def insertcurfun():
    
    Order_NO = int(input("\n enter the Order Number "))
    Transaction_Amount=  input("\n enter the Transaction Amount ")
    Order_Status = input("\n enter the Order status")
    fun = Insert_Cur.insert()
    fun.insertRecord(Order_NO,Transaction_Amount,Order_Status)



def insertpastfun():

    Order_No = input("\n enter the Order Number ")
    Transaction_Amount=  input("\n enter the Transaction Amount ")
    Transaction_Status = input("\n enter the Transaction status")
    fun = Insert_Past.insertPast()
    fun.insertpastRecord(Order_No,Transaction_Amount,Transaction_Status)

if __name__ == '__main__':
    driver = InsertDetails()
    driver.insert_Details()
