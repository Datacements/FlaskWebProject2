import configparser
import sys
import pyodbc as odbc
import warnings

warnings.filterwarnings('ignore')

class deletePastProduct:
    
    def delOperationsFunc(self):

        
        
        

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

        print("\n\n Welcome to Past Transactions page")
        Orderno = input("""\n\n Please provide Order_NO that need to be deleted:  """)
        del_statement = "delete from pastTransaction where Order_No="+Orderno
            
        

        try:
            cursor.execute(del_statement)

        
     
        except Exception as e:

            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        
        else:
            print()
            print("Record deleted")
            cursor.commit()
            cursor.close()          
            
if __name__ == '__main__':
    driver = deletePastProduct()
    driver.delOperationsFunc()