item2=[]
def Mutton():
    print("\n\t\t 1.Mutton Kosha(F)-350/- \n\t\t 2.Mutton Kosha(H)-280/-  \n\t\t 3.Mutton Curry-200/- \n\t\t 4.Mutton Chap-80/- \n\t\t 5.Mutton Rogan Josh-250/- \n\t\t 6.Mutton Rezala-220/- \n\t\t 7.Mutton KOrma-260/-")
    ch2=int(input("Enter your choice:-"))
    if(ch2==1):
        item="Mutton Kosha(F)-350.00"
        p=int(input("Enter the number of plate:-"))
        amt=350.00*p
    elif(ch2==2):
        item="mutton Kosha(H)-280.00"
        p=int(input("Enter the number of plate:-"))
        amt=280.00*p
    elif(ch2==3):
        item="Mutton Curry-200.00"
        p=int(input("Enter the number of plate:-"))
        amt=200.00*p
    elif(ch2==4):
        item=" Mutton Chap-80.00"
        p=int(input("Enter the number of plate:-"))
        amt=80.00*p
    elif(ch2==5):
        item="Mutton Rogan Josh-250.00"
        p=int(input("Enter the number of plate:-"))
        amt=250.00*p
    elif(ch2==6):
        item="Mutton Rezala-220.00"
        p=int(input("Enter the number of plate:-"))
        amt=220.00*p
    elif(ch2==7):
        item="Mutton Korma-260.00"
        p=int(input("Enter the number of plate:-"))
        amt=260.00*p
    print("Item Id :-",item,"\tPlate :-",p,"\t Amount :-",amt)
    item2.append(item)
    item2.append(p)
    item2.append(amt)
    return item2
