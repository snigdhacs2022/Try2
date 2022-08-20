import chicken
import mutton
import roti
item1=[]
def first_menu():
    print("1.Order now \n 2.Billing \n 3.Print order \n 4.Clean \n 5.Exit")
    ch=int(input("Enter your choice:-"))
    if ch==1:
        second_menu()
        first_menu()
    elif ch==2:
        Billing()
def second_menu():
    print("1.Biriyani \n 2.Chicken \n 3.Mutton \n 4.Roti \n 5.Veg \n 6.Mislenious")
    ch1=int(input("Enter your choice:-"))
    if(ch1==1):
        r2=Biriyani()
        return r2
    elif(ch1==2):
        r3=chicken.Chicken()
        return r3
    elif(ch1==3):
        r4=mutton.Mutton()
        return r4
    elif(ch1==4):
        r5=roti.Roti()
        return r5
def Biriyani():
    print("\n\n\t\t 1:-Chicken Biriyani(Full)-120/- \n\t\t 2:- Chicken Biriyani(Half)-80/- \n\t\t 3:-Mutten Biriyani(Full)-150/- \n\t\t 4:-Mutton Biriyani(Half)-120/- \n\t\t 5:-Veg Biriyani(Ful)-100/- \n\t\t 6:-Veg Biriyani(Half)-60")
    ch2=int(input("Enter your choice:-"))
    if(ch2==1):
        item="Chicken Biriyani(Full)-120.00"
        p=int(input("Enter the number of plate:-"))
        amt=120.00*p
    elif(ch2==2):
        item="Chicken Biriyani(Half)-80.00"
        p=int(input("Enter the number of plate:-"))
        amt=80.00*p
    elif(ch2==3):
        item="Mutton Biriyani(Full)-150.00"
        p=int(input("Enter the number of plate:-"))
        amt=150.00*p
    elif(ch2==4):
        item="Mutton Biriyani(Half)-120.00"
        p=int(input("Enter the number of plate:-"))
        amt=120.00*p
    elif(ch2==5):
        item="Veg Biriyani(Full)-100.00"
        p=int(input("Enter the number of plate:-"))
        amt=100.00*p
    elif(ch2==6):
        item="Veg Biriyani(Half)-60.00"
        p=int(input("Enter the number of plate:-"))
        amt=60.00*p
    print("Item Id :-",item,"\tPlate :-",p,"\t Amount :-",amt)
    item1.append(item)
    item1.append(p)
    item1.append(amt)
    return item1
def Billing():
    print(item1[0])
    print(item1[1])
    print(item1[2])
    print(item1[3])
