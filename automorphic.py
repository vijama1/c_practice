inp=input("Enter the number")
intinp=int(inp)
list=[]
list1=[]
list2=[]
for i in inp:
    list.append(i)
length=len(list)
square=intinp*intinp
strsquare=str(square)
for j in strsquare:
    list1.append(j)
list2=list1[-length:]
num=int(''.join(list2))
if num==intinp:
    print("Automorphic")
else:
    print("Not automorphic")
