import pyodbc
class pastTransdetails:
   
    
   def pastTransdet(self):
       
        print("\n\n Welcome to the Past Transaction page \n\n")
        conn= pyodbc.connect ('Driver={SQL Server};'
                              'Server=MSI\SURYASQL;'
                              'Database=Logistic;'
                              'Trusted_Connection=yes;')
        cursor=conn.cursor()
        cursor.execute('Select * from pastTransaction')

        for row in cursor:
            print(row)
    