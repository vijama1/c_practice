no=int(input("Enter the Year"))
if ((no%4==0) and (no%100!=0)) or ((no%100==0) and (no%400==0)):
    print("leap")
else:
    print("not leap")
