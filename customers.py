from mysql.connector import (connection)
import mysql.connector

import os

#CLASS USED IN PROJECT
#customer information"

class customer:
    def init_(self):
        self. cust_id=0
        self. cname=""
        self. address=""
        self._phno=""

##- -Public functions
#-- -modify customer details starts
# def modifycust_data(n1,nm, add,q): **COMPANY NAME TO BE MODIFIED ENDS HERE #

def getcustid(self):
    return self._cust_id
def getcustnm(self):
    return self._cname
def getcustadd(self):
    return self._address
def getphno(self):
    return self._phno
#--to set the values----- 

def setcustid(self,cid):
    self._cust_id=int(cid)
def setcustnm(self,cnm):
    self. cname=cnm
def setcustadd(self,add):
    self._address=add
def setphno(self,ph1):
    self._phno=ph1

def cust_input(self,custid):
    print("===========================================")
    print("CUST NO:")
    self. cust_id=custid
    self._cname=input("NAME OF CUST:")
    print(self._cust_id)
    self. address=input("ADDRESS:")
    self. phno-input("PHONE NO.:")
    print("==========================================")

def show_cust(self):
    print("==========================================")
    print("CUST NO:",self._cust_id)
    print("NAME OF CUST:",self. cname)
    print("ADDRESS:", self.__address)
    print("PHONE NO.:", self.__phno)
    print("===========================================")

def showallcust(self):
    print(self._cust_id,"\t\t",self._cname,"it",self._address,"\t\t", self._phno)
def showcustdatamulti(self):
    print("======================================")
    print("CUST NO:",self.__cust_id)
    print("NAME OF CUSTD:",self._cname)
    print("ADDRESS:", self._address)
    print("PHONE NO.:", self.___phno)
    print("========================================")

def giveno():
    count=1000
    mydb=connection.MySQLConnection(host="localhost",user="root",password="@HAppy1234", database="canteensys")
    print(mydb)
    mycursor=mydb.cursor()
    query=("SELECT COUNT(*) FROM customer")
    q=("SELECT MAX(custid) FROM customer")
    mycursor.execute(query)
    rc=mycursor.fetchone()

    #mycursor.execute(q)
    #rc-mycursor.fetchone()
    #print(rc[0])
    #count=rc[0]

    tmp=rc[0]
    print(tmp)
    if tmp==0:
        count=1001
    else:
        #mycursor.close()
        q=("SELECT MAX(custid) FROM customer")
        mycursor.execute(q)
        rc-mycursor.fetchone()
        count=rc[0]
        count=count+1

    mycursor.close()
    mydb.close()
    return count

def writecustdata():
    try:
        cobj=customer()
        conn=connection.MySQLConnection(user='root', password='@HAppy1234',host='localhost',database="canteensys" )
        C=conn.cursor()
        Query=("INSERT INTO customer VALUES (%s,%,%,%s)")
        cno=giveno()
        cobj.cust_input(cno)
        data=(cobj.getcustid(),cobj.getcustnm(),cobj.getcustadd(),cobj.getphno())
        C.execute(Query.data)
        conn.commit()
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to display all the customers

def displaallcustdata():
    try:
        cobj=customer()
        C=conn.cursor()
        Query=("SELECT FROM customer")
        C.execute(Query)
        rc=C.fetchall()
        print("CUSTID\t\tCUSTNAME\\CUSTADDRESS\t\tCUSTPHONE")
        for x in rc:
            cobj.setcustid(x[0])
            cobj.setcustnm(x[1])
            cobj.setcustadd(x[2])
            cobj.setphno(x[3])
            cobj.showallcust()
        input("press the key")
        os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#------search and display the customer record
def searchdisplaycustdata():
    try:
        cobj=customer()
        conn=connection.MySQLConnection(user='root',password='@HAppy1234',host='localhost', database='canteensys')
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        Query=("SELECT FROM customer WHERE custid=%s")
        data=(cno,)
        C.execute(Query,data)
        rc=C.fetchone()
        print("CUSTID\t\tCUSTNAME\t\tCUSTADDRESS\t\tCUSTPHONE")
        cobj.setcustid(rc[0])
        cobj.setcustnm(rc[1])
        cobj.setcustadd(rc[2])
        cobj.setphno(rc[3])
        cobj.showallcust()
        input("press the key")
        os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to search and update the customer name
def search_mod_custom():
    try:
        cobj=customer()
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        rc1=searchcustdata(cno)
        if rc1:
            cnm=input("Enter the name")
            Query=("UPDATE customer SET custname=%s WHERE custid=%s")
            data=(cnm,cno)
            C.execute(Query,data)
            conn.commit()
            print(C.rowcount, "record(s) affected")
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to search and update the customer addres
def search_mod_custadd():
    try:
        cobj=customer()
        conn-connection.MySQLConnection(user='root',password='@HAppy1234',host='localhost', database='canteensys')
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        rc1=searchcustdata(cno)
        if rc1:
            cad=input("Enter the new address")
            Query=("UPDATE customer SET custadd=%s WHERE custid=%s")
            data=(cad,cno)
            C.execute(Query.data)
            conn.commit()
            print(C.rowcount, "record(s) affected")
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to search and update the customer phone number
def search_mod_custphno():
    try:
        cobj=customer()
        conn-connection.MySQLConnection(user='root', password='@HAppy1234',host='localhost',database='canteensys')
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        rc1=searchcustdata(cno)
        if rc1:
            cph-input("Enter the new phone number")
            Query=("UPDATE customer SET cusrphno=%s WHERE custid=%s")
            data=(cph,cno)
            C.execute(Query,data)
            conn.commit()
            print(C.rowcount, "record(s) affected")
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to search and delete the customer
def search_del_cust():
    try:
        cobj=customer()
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        rc1=searchcustdata(cno)
        if rc1:
            Query=("DELETE FROM customer WHERE custid=%s")
            data=(cno,)
            C.execute(Query.data)
            conn.commit()
            print(C.rowcount, "record(s) affected")
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#search and display the customer record using parameter
def searchcustdata(scid):
    try:
        cobj=customer()
        conn-connection.MySQLConnection(user='root', password='@HAppy1234',host='localhost', database='canteensys')
        C=conn.cursor()
        Query=("SELECT * FROM customer WHERE custid=%s")
        data=(scid,)
        C.execute(Query,data)
        rc=C.fetchone()
        if rc:
            print("CUSTID\t\tCUSTNAME\t USTADDRESS\t\tCUSTPHONE") 
            cobj.setcustid (rc[0])
            cobj.setcustnm(rc[1])
            cobj.setcustadd(rc[2])
            cobj.setphno(rc[3])
            cobj.showallcust()
            input("press the key")
            os.system('cls')
            C.close()
            conn.close()
        return rc
    except mysql.connector.Error as err:
        print(err)
        conn.close()


















































      
