import sys
import pyodbc as odbc

class insert:

    def insertRecord(self,Order_NO,Transaction_Amount,Order_Status):
        self.Order_NO= Order_NO
        self.Transaction_Amount= Transaction_Amount
        self.Order_Status=Order_Status
       
        records = [[Order_NO,Transaction_Amount,Order_Status]]
        

        DRIVER = 'SQL Server'
        SERVER_NAME = 'MSI\SURYASQL'
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

        
        ins_statement = """
            INSERT INTO currentTransaction

            VALUES (?, ?, ?)
        """

        try:
            
            for num in records:
                print(num)
                
                cursor.execute(ins_statement, num)        
        except Exception as e:
            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        else:
            print('records inserted successfully')
            cursor.commit()
            cursor.close()

