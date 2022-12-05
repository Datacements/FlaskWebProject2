import sys
import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

class updatecurTrans:
    
    def UpdatecurFunc(self):


        inputcur = int(input("""\n\n\n 
        Press 1 If you want to update Current Transaction details for Order Status for a given Order Number , 
        Press 2 If you want to update Current Transaction details for Transaction amount for a given Order Number,
        Press 3 If you want to update Past Transaction details for Transaction Status for a given Order Number,
        Press 4 If you want to update Past Transaction details for Transaction amount for a given Order Number
        \n\n """))
        
        

        DRIVER = 'SQL Server'
        SERVER_NAME = 'MSI\SURYASQL'
        DATABASE_NAME = 'Logistic'

        conn_string = f"""
            Driver={{{DRIVER}}};
            Server={SERVER_NAME};
            Database={DATABASE_NAME};
            Trust_Connection=yes;"""
        
        

        try:
            conn = odbc.connect(conn_string)
            
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        if(inputcur ==1):
            orderID= input("""\n\n 
            Please provide order number that need to be updated """)
            order_input = input("""\n\n 
            Please provide Order status that need to be updated """)
            update_statement = " update currentTransaction set Order_Status ="+"'"+order_input+"'"+"where Order_NO="+orderID

        elif(inputcur ==2):
            orderID = input("""\n\n 
            Please provide Order number that need to be updated """)
            Trans_input = input("""\n\n 
            Please Transaction Amount that need to be updated """)
            update_statement = " update currentTransaction set Transaction_Amount ="+"'"+Trans_input+"'"+"where Order_NO="+orderID

        elif(inputcur ==3):
            orderID = input("""\n\n 
            Please provide Order number that need to be updated """)
            Trans_input = input("""\n\n 
            Please Transaction Status that need to be updated """)
            update_statement = " update pastTransaction set Transaction_Status ="+"'"+Trans_input+"'"+"where Order_No="+orderID

        elif(inputcur ==4):
            orderID = input("""\n\n 
            Please provide Order number that need to be updated """)
            Trans_input = input("""\n\n 
            Please Transaction Amount that need to be updated """)
            update_statement = " update pastTransaction set Transaction_Amount ="+"'"+Trans_input+"'"+"where Order_No="+orderID
           
        else:
            pass
        
        try:
           cursor.execute(update_statement)

        except Exception as e:

            cursor.rollback()
            print(e)
            print('transaction rolled back')
        
        else:
            print()
            print("Record updated")
            cursor.commit()
            cursor.close()
                       
if __name__ == '__main__':
    driver = updatecurTrans()
    driver.UpdatecurFunc()
   







