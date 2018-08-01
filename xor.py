inp=int(input("Enter number of elemets of array"))
list=[]

for j in range(0,inp):
    list.append(int(input("Enter array elements")))
kvalue=int(input("Enter the value of k"))
res=list[0]
for j in range(1,len(list)):
    res=res^list[j]
print("res",res)
res=res^kvalue
print(res)
