inp=int(input("Enter size of array"))
list=[]
list1=[]
sumlist=[]
sum=0
i=0
for j in range(0,inp):
    list.append(int(input("Enter array elemets")))
print(list)
for j in range(inp):
    for k in range(1,inp):
        list1.append([list[j],list[k]])
        sumlist.append(abs(list[j]+list[k]))
print(min(sumlist))
#print(list1)
for i,j in list1:
    if i+j==min(sumlist):
        print(i,j)
