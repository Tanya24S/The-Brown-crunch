import Canteenmenu as CM
import customers as cust
import product as pr

def modifyprodshow():
    choice1=" "
    choice1=CM.modify_prodmenu()
    while True:
        if choice1==1:
            pr.search_mod__prodnum()
            break
        elif choice1==2:
            pr.search_mod_prodcomy()
            break
        elif choicee1==3:
            pr.search_mod_prodprice()
            break
        elif choice1==4:
            pr.search_mod_prodqty()
            break
        elif choice1==5:
            pr.search_mod_proddiscount()
            break
        elif choice1==6:
            pr.search_mod_proddate()
            break
        elif choice1==7:
            pr.search_updt_invoice()
            input("-----------press any key------------")
            break
        elif choice1==8:
            main()
        else:
            print("ENter the correct choicw")
            input("ENter any key to continue")
            modifyprodshow()

def product_show():
    choice1=""
    choice1=CM.admin_menu()
    while True:
        if choice1==1:
            pr.writeprodata()
            break
        elif choice1==2:
            pr.displayproddata()
            break
        elif choice1==3:
            pr.searchdisplayproddata()
            break
        elif choice1==4:
            modifyprodshow()
            break
        elif choice1==5:
            pr.search_del_prod()
            input("--------press any key-------")
            break
        elif choice1==6:
            pr.showallprodinvoice()
            nput("--------press any key-------")
            break
        elif choice1==7:
            main()
        else:
            print("Enter the correct choice")
            input("ENter any key to continue")
            product_show()

def cust_show():
    choice1=" "
    choice1=CM.admin_menu1()
    while True:
        if choice1==1:
            cust.writecustdata()
            break
        elif choice1==2:
            cust.displayallcustdata()
            break
        elif choice1==3:
            cust.searchdisplaycustdata()
            break
        elif choice1==4:
            modifyshow()
            break
        elif choice1==5:
            cust.search_del_cust()
            input("--------press any key-------")
            break
        elif choice1==6:
            main()
        else:
            print("Enter the correct choice")
            input("ENter any key to continue")
            cust_show()

def modifyshow():
    choice1=" "
    choice1=CM.admin_menu1()
    while True:
        if choice1==1:
            cust.search_mod_custnm()
            break
        elif choice1==2:
            cust.search_mod_custadd()
            input("--------press any key-------")
            break
        elif choice1==3:
            cust.ssearch_mod_custphno()
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("--------press any key-------")
            choice1=0
            modifyshow()

def midmenu():
    choice1=CM.middleadminmenu()
    while True:
        if choice1==1:
            cust_show()
            break
        elif choice1==2:
            cproduct_show()
            input("--------press any key-------")
            break
        elif choice1==3:
            canteen_show()
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("--------press any key to continue-------")
            choice1=0
            midmenu()

#WAIT
def canteen_show():
    choice1=CM.canteen_menu()
    while True:
        if choice1==1:
            cust.search_mod_custnm()
            break
        elif choice1==2:
            cust.search_mod_custadd()
            input("--------press any key-------")
            break
        elif choice1==3:
            cust.ssearch_mod_custphno()
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("--------press any key-------")
            choice1=0
            modifyshow()

#WAIT


#MAIN MENU
def main():
    CM.intro()
    choice=0
    while True:
        choice=CM.main()
        if choice==1:
            CM.myclear()
            break
        elif choice==2:
            CM.myclear()
            midmenu()
            break
        elif choice1==3:
            exit(1)
        else:
            print("Enter the correct choice")
            input("--------press any key-------")

main()































            
