item1=[]
def Chicken():
    print("\n\t\t 1.Chicken Kosha(F)-200/- \n\t\t 2.Chicken Kosha(H)-120/-  \n\t\t 3.Chilli Chicken(F)-120/- \n\t\t 4.Chilli Chicken(H)-80/- \n\t\t 5.Chicken Tanduri-100/- \n\t\t 6.Chicke Chettinad-220/- \n\t\t 7.Chicken lolipop-100/-")
    ch2=int(input("Enter your choice:-"))
    if(ch2==1):
        item="Chicken Kosha(F)-200.00"
        p=int(input("Enter the number of plate:-"))
        amt=200.00*p
    elif(ch2==2):
        item="Chicken Kosha(H)-120.00"
        p=int(input("Enter the number of plate:-"))
        amt=120.00*p
    elif(ch2==3):
        item=" Chilli Chicken(F)-120.00"
        p=int(input("Enter the number of plate:-"))
        amt=120.00*p
    elif(ch2==4):
        item=" Chilli Chicken(H)-80.00"
        p=int(input("Enter the number of plate:-"))
        amt=80.00*p
    elif(ch2==5):
        item="Chicken Tanduri-100.00"
        p=int(input("Enter the number of plate:-"))
        amt=100.00*p
    elif(ch2==6):
        item="Chicken Chettinad-220.00"
        p=int(input("Enter the number of plate:-"))
        amt=220.00*p
    elif(ch2==7):
        item="Chicken Lolipop-100.00"
        p=int(input("Enter the number of plate:-"))
        amt=100.00*p
    print("Item Id :-",item,"\tPlate :-",p,"\t Amount :-",amt)
    item1.append(item)
    item1.append(p)
    item1.append(amt)
    return item1
