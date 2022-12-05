import sys
import pyodbc as odbc

class insertPast:

    def insertpastRecord(self,Order_No,Transaction_Amount,Transaction_Status):
        self.Order_No= Order_No
        self.Transaction_Amount= Transaction_Amount
        self.Transaction_Status=Transaction_Status
       
        records = [[Order_No,Transaction_Amount,Transaction_Status]]
        

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
            INSERT INTO pastTransaction

            VALUES (?, ?, ?)
        """

        try:
            
            for rec in records:
                print(rec)
                
                cursor.execute(ins_statement, rec)        
        except Exception as e:
            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        else:
            print('records inserted successfully')
            cursor.commit()
            cursor.close()


