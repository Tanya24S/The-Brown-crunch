from mysql.connector import(connection)
import mysql.connector
import os
import datetime

#Product info
class product:
    def _init_(self):
        self._prod_id=0
        self._prodname=" "
        self._prod_comp=" "
        self._prod_price=0
        self._prod_qty=0
        self._prod_dis=0
        self._prod_DOP=0 


def setprodid(self,pid):
    self._prod_id=int(pid)

def setprodnm(self,pnm):
    self._prodname=pnm
def setprodcmpy(self,cpy):
    self._prod_comp=cpy
def setprodpr(self,pr):
    self._prod_price=int(pr)
def setprodqty(self,qty):
    self._prod_qty=int(qty)
def setproddis(self,ds):
    self._prod_dis=int(ds)
def setproddate(self,dt):
    self._prod_DOP=dt

#Product TO BE MODIFIED 

def getprodid(self):
    return self._prod_id
def getprodnm(self):
    return self._prodname
def getprodcompy(self):
    return self._prod_comp
def getprodpr(self):
    return self._prod_price
def getprodaty(self):
    return self._prod_qty
def getproddis(self):
    return self._-prod_dis
def getproddate(self):
    return self._prod_DOP

def prod_input(self,pid):
    print("==========================================")
    print("PROD NO:")
    self._prod_id=pid
    print(self._prod_id)
    self._prodname=input("NAME OF PRODUCT")
    self._prod_comp=input("NAME OF PRODUCT COMPANY:")
    self. prod_price=int(input("PRODUCT PRICE:"))
    self._prod_qty=int(input("PRODUCT QUANTITY"))
    self._prod_dis=int(input("PRODUCT DISCOUNT:"))
    self._prod_DOP=input("PRODUCT DATE(yyyy-mm-dd) OF PURCHASED:")
    print("=============================================")

def show_product(self):
    print("===========================================")
    print("PROD NO:", self._prod_id)
    print("NAME OF PRODUCT:", sell._prodname)
    print("PRODUCT COMPANY:", sell._prod_comp)
    print("PRODUCT PRICE:", self._prod_price)
    print("PRODUCT QUANTITY:", self._prod_qty)
    print("PRODUCT DISCOUNT:", self._prod_dis)
    print("DATE OF PURCHASED:", self._prod_DOP)
    print("==============================================")

def showallprod(self):
    print(self._prod_id"\t",self._prodname"\t",self._prod_comp"\t",self._prod_price"\t", self._prod_qty"\t",self._prod_DOP)

def showproddatamulti(self):
    print("==============================================")
    print("PROD NO:", self._prod_id)
    print("NAME OF PRODUCT:", self._prodname)
    print("PRODUCT COMPANY", self._prod_comp)
    print("PRODUCT PRICE:", self._prod_price)
    print("PRODUCT QUANTITY", self._prod_aty)
    print("PRODUCT DISCOUNT". sell._prod_dis)
    print("DATE OF PURCHASED:", self.prod_DOP)
    print("=============================================")

def getprodname(prid):
    mydb=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
    mycursor=mydb.cursor()
    query("SELECT prod nm FROM product WHERE prodid=%")
    data(prid,)
    mycursor.execute(query,data)
    rc=mycursor.fetchone()
    tmp=rc[0]
    mycursor.close()
    mydb.close()
    retum tmp

def giveprodno():
    count 1000
    mydb=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
    print(mydb)
    mycoursor=mydb.cursor()
    query=("SELECT COUNT(*) FROM product")
    q=("SELECT MAX (prodid) FROM product")
    mycursor.execute(query)
    romyoursoc.fetchone()
    temp=rc[0]
    print(tmp)
    if temp==0:
        count=5001
    else:
        q=("Select MAX(prodid) FROM product")
        mycursor.execute(q)
        rc=mycursor.fetchone()
        count=rc[0]
        count count+1
    mycursor.cose()
    mydb.close()
    return count

def giveprrodINVOICEno():
    count=1
    mydb=connection.MYSQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
    print(mydb)
    mycursor=mydb.cursor()
    query=("SELECT COUNT(*) FROM product_invoice")
    q=("SELECT MAX(prodinv_id) FROM product_invoice")
    mycursor.execute(query)
    rc=mycursor.fetchone()
    temp=rc[0]
    print(tmp)
    if tmp==0:
        count=1
    else:
        q=("SELECT MAX(prodinv-id) FROM product_invoice")
        mycursor.execute(q)
        rc=mycursor.fetchone()
        count=rc[0]
        count=count+1
    mycursor.close()
    mydb.close()
    return count
    
 #INVOICE NUMBER
def writeprod_invodata(prid,pr_nm,pr_dt,pr_qty,pr_st,prinvo):
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        n=giveprodINVOICEno()
        Query("INSERT INTO product invoice VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        if pr_st=="PAID" or pr_st=="Paid" or pr_st"paid":
            data=(n,prid,pr_nm,pr_dt,pr_qty,"CASH or CHEQUE", prinvo)
        else:
            data=(n,prid,pr_nm,pr_dt,pr_qty,"Not Paid", prinvo)
        C.execute(Query data)
        conn.commit()
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

def writeproddata():
    try:
        pobj=product()
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        Query=Query("INSERT INTO product invoice VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        no=giveprodno()
        pobj.prod_input(no)
        prodinvo=int(input("ENter the invoice no:"))
        prdstat=input("Enter the status PAID or not paid")

        now=pobj.getproddate()
        data=(pobj.getprodid(), pobj.getprodnm(), pobj.getprodcompy(), pobj.prodpr(), pobj.getproddis(), now())
        C.execute(Query,data)
        conn.commit()
        C.close()
        conn.close()
        writeprod_invodata(pobj.getprodid(), pobj.getprodnm(),now,pobj.getprodqty(), prdstat, prdinvo)
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        

def displaalproddata():
    try:
        pobj=product()
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        Query("SELECT * FROM product")
        C.execute(Query)
        rc=C.fetchall
        print("PRODID\tPRODNAME\tCOMPANY\tPRODPRICE\tPROQTY\tDISCOUNT\tDATEOFPURCHASE")
        for x in rc:
            pobj.setprodid(x[0])
            poj.setprodnm(x[1])
            pobj.setprodcmpy(x[2])
            pobj.setpropr(x[3])
            pobj.setprodqty(x[4])
            pobj.setproddis(x[5]
            pobj.setprodate(x[6])
            input("press the key")
            os.system('cs')
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

def searchdisplayproddata():
    try:
        pobj=product()
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        no=int(input("ENTER PRODUCT ID"))
        Query=("SELECT * FROM product WHERE prodid=%s")
        C.execute(Query.data)
        rc=C.fetchone()
        print("PRODID\tPRODNMAE\tCOMPANY\tPRODPRICE\tPRODQTY\tDISCOUNT\tDATEOFPURCHASE")
        pobj.setprodid(rc[0])
        pobj.setprodnm(rc[1])
        pobj.setprodcmpy(rc(21)
        pobj.setprodpr(rc[3])
        pobj.setprodqty(rc[4])
        pobj.setproddis(rc[5])
        pobj.setproddate(rc[6])
        pobj.showallprod()
        input ("press the key")
        os.system("cls")
        C.close()
        conn.close()

    except mysql connector Error as err:
        print(or)
        conn.close()


def search_mod_prodnim():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=int(input("Enter PROD ID"))
        pnm=input("ENTER THE PRODUCT NAME")
        Query=("'UPDATE product SET prod_nm=%s WHERE prodid=%s")
        data=(pnm,pno)
        C.execute(Query.data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.dose()
    except mysql.connector.Error as em:
        print(err)
        conn.close()

#-to search and update the product company name

def search_mod_prodcompy:
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=int((input("ENTER PROD ID"))
        pcnm=input("Enter the new company name")
        Query("UPDATE product SET prod_company%s WHERE prodid=%s")
        data=(pcnm,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()

#to search and update the product price
def search_mod_prodprice:
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        cno=int((input("ENTER PROD ID"))
        cph=input("Enter the new price")
        Query=("UPDATE product SET_prod price%s WHERE prodid=%s")
        data (cph,cno)
        C.execute(Query data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
   except mysql.connector Error as em:
       print(err)
       conn.close()


def search_mod_prodity:
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=(input("ENTER PROD ID"))
        pqty=int(input("Enter the add more qty")
        prdate=input("Enter the purchase datelyyyy-mm-dd)")
        prdinvo=int(input("Enter the Invoice no."))
        prdstat=input("Enter the status PAID or NOT PAID")
        Query=("UPDATE product SET_prod_glyprod_ WHERE prodid=%s")
        data=(pqty,pno)
        C.execute(Query.data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
        prnm=getprodname(pno)
    except mysql.connector.Error:
        print(err)
        conn.close()

def search_mod_proddiscount():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=(input("ENTER PROD ID"))
        pdis=int(input("Enter the new discount")
        Query=("UPDATE product SET prod_discount=%s WHERE prodid=%s")
        data=(pdis,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount "record(s) affected")
        C.close()
        conn.close()
    except mysql connector.Error as err:
        print(err)
        conn.close()

def search_mod_proddate():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=(input("ENTER PROD ID"))
        pdis=int(input("Enter the date of purchase")
        Query=("UPDATE product SET prod_purchasedt=%s WHERE prodid=%s")
        data(pdt,pno)
        C.execute(Query,data)
        conn.commit()
        print(Crowcount, "record(s) affected")
        C.close()
        conn.close
    except mysql connector Error as err:
        print(err)
        conn.close()

#to search and delete the product

def search_del_prod():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=(input("ENTER PROD ID"))
        Query=("UPDATE FROM product WHERE prodid=%s")
        data=(pno,)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close
    except mysql.connector.Error as err:
        print(err)
        conn.close()

def search_updt_invoice():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=(input("ENTER PROD ID"))
        Query=("SELECT * FROM product_invoice WHERE prodinv_invoiceno=%s")
        data(pno,)
        C.execute(Query,data)
        row_count=C.rowcount
        rc=C.fetchone()
        C.close()
        conn.close()

def showallprodinvoice():
    try:
        conn=connection.MySQLConnection(host="localhost",user="root", password "@HAppy", database="canteensys")
        C=conn.cursor()
        pno=int(input("ENTER PROD NO"))
        Query=("SELECT * FROM product_invoice WHERE prodid=%s")
        data=(pno,)
        C.execute(Query.data)
        rc=C.fetchall()
        if rc:
            print("PRODID\tPRODNAME\tDATE\tPRODOTY\tSTATUS\tINVOICENO")
            for x in rc:
                print(x[1],"t", x[2]"\t\t", x[3]"\t\t",x[4]"\t",x[5]"\t",x[6])
        else:
            print("not such invoice exists")
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()



































