item3=[]
def Roti():
    print("\n\t\t 1.Aloo Paratha - 60/- \n\t\t 2.Malabar Paratha - 80/- \n\t\t 3.Poori - 50/- \n\t\t 4.Appam - 55/- \n\t\t 5.Roomali Roti - 60/- \n\t\t 6.Kashmiri Roti -90/- \n\t\t 7.Tardoori Garlic Naan -85/- \n\t\t 8.Sheermal -75/- \n\t\t 9.Amritsari Kulcha -80/-")
    ch2=int(input("Enter your choice:-"))
    if(ch2==1):
        item="Aloo Paratha - 60.00"
        p=int(input("Enter the number of plate:-"))
        amt=60.00*p
    elif(ch2==2):
        item="Malabar Paratha - 80.00"
        p=int(input("Enter the number of plate:-"))
        amt=80.00*p
    elif(ch2==3):
        item="Poori - 50.00"
        p=int(input("Enter the number of plate:-"))
        amt=50.00*p        
    elif(ch2==4):
        item="Appam - 55.00"
        p=int(input("Enter the number of plate:-"))
        amt=55.00*p
    elif(ch2==5):
        item="Roomali Roti - 60.00"
        p=int(input("Enter the number of plate:-"))
        amt=60.00*p
    elif(ch2==6):
        item="Kashmiri Roti -90.00"
        p=int(input("Enter the number of plate:-"))
        amt=90.00*p
     elif(ch2==7):
        item="Tardoori Garlic Naan -85.00"
        p=int(input("Enter the number of plate:-"))
        amt=85.00*p
    elif(ch2==8):
        item="Sheermal -75.00"
        p=int(input("Enter the number of plate:-"))
        amt=75.00*p
    elif(ch2==9):
        item="Amritsari Kulcha -80.00"
        p=int(input("Enter the number of plate:-"))
        amt=80.00*p
    print("Item Id :-",item,"\tPlate :-",p,"\t Amount :-",amt)
    item3.append(item)
    item3.append(p)
    item3.append(amt)
    return item3        
