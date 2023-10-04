#PROJECT

from time import sleep
from random import randint
def accnum():
        an=""
        for i in range(9):
                an+=str(randint(0,9))
        return an

def checkamt(acc_no):
        sq1=f"select amount from account where acc_no={acc_no}"
        cur.execute(sq1)
        data=cur.fetchall()
        return data[0][0]

def addacc(an,n,a,p,amt,t,):
        sq1="insert into account(Acc_no, Name, Age, Phone_no, Amount, Acc_Type) values({},'{}',{},{},{},'{}')".format(an,n,a,p,amt,t)
        cur.execute(sq1)
        con.commit()

def fd(an,pa,i,d,t,fa):
        sq1=f"insert into fd values({an},{pa},{i},{d},{t},{fa})"
        cur.execute(sq1)
        con.commit()

import mysql.connector as ms
con=ms.connect(
        host='localhost',
        user='root',
        passwd='12345'
        )
cur=con.cursor()

#TABLE AND DATABASE CREATION

db="create database Bank"
use="use Bank"
t1="create table Account(Acc_no varchar(10), Name varchar(30), Age int(3), Phone_no varchar(10), Amount int, Acc_Type varchar(30))"
t2="create table FD(Acc_no varchar(10), P_Amt int, Interest int(2), Date date, Time int, Final_Amt int )"
cur.execute(db)
cur.execute(use)
cur.execute(t1)
cur.execute(t2)
con.commit()

#MAIN PROGRAM

sq="select acc_no from account"
cur.execute(sq)
l=cur.fetchall()
q1=input("Do you have an bank account? (y/n) \n->")
if q1=="y"or q1=="Y":
        q2=int(input("Kindly enter your bank account number -> "))
        if q2 in l[0]: 
                q3=1
                #MENU 1
                print("\nWELCOME")
                while q3:
                        print("\nHow can I help you?")
                        q3=int(input("1.Deposit Money\n2.Withdraw Money \n3.Create new bank account\n4.Do a FD\n5.Check Balance\n6.Exit\n(Choose an option)\n->"))

                        if q3==1:
                                q4=int(input("Enter amount you want to deposit in your bank account -> "))
                                c=checkamt(q2)
                                sq1=f"update account set amount = {c+q4} where acc_no ={q2}"
                                cur.execute(sq1)
                                con.commit()
                                print("Adding amount in your account\nPlease Wait. . . . ")
                                sleep(3)
                                print("\nRs.",q4, "credited in your bank account\nAvailable balance in your bank account -> ",c+q4,"\n") 
                                sleep(2)

                        elif q3==2:
                                q4=int(input("\nEnter amount you want to withdraw from your bank account -> "))
                                c=checkamt(q2)
                                if q4>c:
                                        print("Insufficent Balance!!!\n")
                                        sleep(2)
                                else:
                                        sq1=f"update account set amount = {c-q4} where acc_no ={q2}"
                                        cur.execute(sq1)
                                        con.commit()
                                        print("Please Wait. . . .")
                                        sleep(3)
                                        print("\nRs.",q4,"debited from your bank account \nAvailable balance in your account -> ",c-q4,"\n")
                                        sleep(2)
                                        
                        elif q3==3:
                                q4=int(input("\nWhat type of bank account you want to open ?\n1.Savings Account\n2.Current Account\n-> "))
                                if q4==1:
                                        name=input("\nEnter your name -> ")
                                        phno=int(input("Enter your Phone no. -> "))
                                        age=int(input("Enter your age -> "))
                                        if age<18:
                                                print("You are underage to be an account holder. Sorry for your inconvenience. ")
                                                break
                                        amt=0
                                        while amt<3000:
                                                amt=int(input("\nEnter amount you want to deposit in your bank account (minimum amount- 3000) \n-> "))
                                                if amt<3000:
                                                        print("Amount entered is less than the minimum amount,so it can't be deposited.\nSorry for the inconvenience.")
                                                else:
                                                        print("\nYour savings bank account is being created \nPlease Wait . . . . ")
                                                        sleep(4)
                                                        print("Your savings bank account has been created successfully.\n ")
                                                        s=accnum()
                                                        print("Your Savings Bank Account Number -> ",s,"\n")
                                                        addacc(s,name,age,phno,amt,"Savings")
                                                        sleep(2)
                                elif q4==2:
                                        name=input("Enter your name -> ")
                                        phno=int(input("Enter your Phone no. -> "))
                                        age=int(input("Enter your age -> "))
                                        if age<18:
                                                print("You are underage to be an account holder. Sorry for your inconvenience. ")
                                                break
                                        amt=0
                                        while amt<3000:
                                                amt=int(input("Enter amount you want to deposit in your bank account (minimum amount- 3000) \n-> "))
                                                if amt<3000:
                                                        print("\nAmount entered is less than the minimum amount,so it can't be deposited.\nSorry for your inconvenience. ")
                                                else:
                                                        print("\nCreating your current bank account \nPlease Wait . . . . ")
                                                        sleep(4)
                                                        print("Your current bank account has been created successfully.\n ")
                                                        s=accnum()
                                                        print("Your Current Bank Account Number -> ",s,"\n")
                                                        addacc(s,name,age,phno,amt,"Current")
                                                        sleep(2)

                        elif q3==4:
                                amt=int(input("\nEnter investment amount to start your FD (Minimum amount -5000 ) -> "))
                                if amt<5000:
                                        print("Amount entered is less than the minimum amount. We can not create your FD.\nSorry for your inconvenience.")
                                else:
                                        time=int(input("Enter time period( in years) for your FD ->  "))
                                        f_amt=amt+((amt*time*6)/100)
                                        print("Your amount after",time,"years will be -> ",f_amt,"\nAre you sure you want to continue? (y/n)")
                                        q4=input("\n-> ")
                                        if q4=="y"or q4=="Y":
                                                print("Creating your FD\nPlease Wait . . . .")
                                                sleep(4)
                                                fd(q2,amt,6,'current_date()',time,f_amt)
                                                print("Your FD is successfully created.")
                                                sleep(2)
                                        elif q4=="n"or q4=="N":
                                                print("As your wish. Thanks for visiting us.")
                                                sleep(2)
                                        else:
                                                print("\nKindly Enter Valid Input")
                                                sleep(2)
                        elif q3==5:
                                c=checkamt(q2)
                                print("Fetching you data. . . . ")
                                sleep(4)
                                print("Available Balance in your account is ",c,"\n")
                                sleep(2)
                        elif q3==6:
                                print("\nThanks for visiting us, have a good day! ")
                                break

                        else:
                                print("\nKindly Enter Valid Input")
                                        
        else:
                print("This account number does not exist.\n\nKindly recheck your account number.")
                
elif q1=="n"or q1=="N":
        q2=1
        #MENU 2
        while q2:
                print("\nHow can I help you?")
                q2=int(input("1.Create an account\n2.Do a FD\n3.Exit\n->"))
                if q2==1:
                        q3=int(input("\nWhat type of account you want to open ?\n1.Savings Account\n2.Current Account\n-> "))
                        if q3==1:
                                name=input("\nEnter your name -> ")
                                phno=int(input("Enter your Phone no. -> "))
                                age=int(input("Enter your age -> "))
                                if age>=18:
                                        amt=0
                                        while amt<3000:
                                                amt=int(input("\nEnter amount you want to deposit in your bank account (minimum amount- 3000) \n-> "))
                                                if amt<3000:
                                                        print("The amount entered is less than the minimum amount, so it can't be deposited.\nSorry for your inconvenience.")
                                                else:
                                                        print("\nCreating your savings bank account \nPlease Wait . . . . ")
                                                        sleep(4)
                                                        print("Your savings bank account has been created successfully.\n ")
                                                        s=accnum()
                                                        print("Your Savings Bank Account Number -> ",s,"\n")
                                                        addacc(s,name,age,phno,amt,"Savings")
                                                        sleep(2)
                                else:
                                        print("Sorry, You are underaged to be an account holder. ")
                                        break
                        elif q3==2:
                                name=input("Enter your name -> ")
                                phno=int(input("Enter your Phone no. -> "))
                                age=int(input("Enter your age -> "))
                                if age<18:
                                        print("You are underage to be an account holder. Sorry for your inconvenience. ")
                                        break
                                amt=0
                                while amt<3000:
                                        amt=int(input("Enter amount you want to deposit in your bank account (minimum amount- 3000) \n-> "))
                                        if amt<3000:
                                                print("\nThe amount entered is less than the minimum amount,so it can't be deposited.\nSorry for your inconvenience. ")
                                        else:
                                                print("\nCreating your current bank account \nPlease Wait . . . . ")
                                                sleep(4)
                                                print("Your current bank account has been created successfully.\n ")
                                                s=accnum()
                                                print("Your Bank Account Number -> ",s,"\n")
                                                addacc(s,name,age,phno,amt,"Current")
                                                sleep(2)

                        else:
                                print("Invalid Input")
                elif q2==2:
                        amt=int(input("\nEnter amount of investment to start your FD (Minimum amount is 5000 ) -> "))
                        if amt<5000:
                                print("The amount entered is less than the minimum amount, so we can not create your FD.\nSorry for your inconvenience. ")
                        else:
                                time=int(input("Enter time period( in years )for your FD->  "))
                                f_amt=amt+((amt*time*6)/100)
                                print("Your amount after",time,"years will be -> ",f_amt,"\nAre you sure you want to continue? (y/n)")
                                q4=input("\n-> ")
                                if q4=="y"or q4=="Y":
                                        print("Creating your FD\nPlease Wait . . . .")
                                        sleep(4)
                                        print("Your FD has been created successfully.")
                                        s=accnum()
                                        print("\nYour FD Account Number -> ",s,"\n")
                                        fd(s,amt,6,'current_date()',time,f_amt)
                                        sleep(2)
                                elif q4=="n"or q4=="N":
                                        print("As your wish. Thanks for visiting us.")
                                        sleep(2)
                                else:
                                        print("\nKindly Enter Valid Input")
                                        sleep(2)
                elif q2==3:
                        print("\nThanks for visiting us, have a good day!")
                        break
                        
                else:
                        print("\nKindly Enter Valid Input")
else:
        print("\nKindly Enter Valid Input")
        
