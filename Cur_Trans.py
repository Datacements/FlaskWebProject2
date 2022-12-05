import pyodbc
class currentTransdetails:

    def curTransdetails(self):
       
        print("\n\n Welcome to the Current Transaction page \n\n")
        conn= pyodbc.connect ('Driver={SQL Server};'
                              'Server=MSI\SURYASQL;'
                              'Database=Logistic;'
                              'Trusted_Connection=yes;')
        cursor=conn.cursor()
        cursor.execute('Select * from currentTransaction')

        for row in cursor:
            print(row)