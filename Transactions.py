import pyodbc as odbc
import Cur_Trans
import PastTrans

class TransPage:

    print("Welcome to Transactions Page!")

Trans_Value= int(input("""\n\n\n  
Press 1 To View the Current Transaction ,
Press 2 To View the Past Transaction \n\n\n"""))

def Trans_Input():


    if(Trans_Value ==1):
        dis = "Current Transaction "
        print()
        print(dis + "  is the option you have selected. ")
        print()
        excus = Cur_Trans.currentTransdetails()
        excus.curTransdetails()

    elif(Trans_Value == 2):

        dis = "Past Transaction"
        print()
        print(dis + "  is the option you have selected. ")
        print()
        admin = PastTrans.pastTransdetails()
        admin.pastTransdet()

    else:
        
        print("Wrong Entry, Try Later.")


if __name__ == '__main__':
    driver = TransPage()
    Trans_Input()