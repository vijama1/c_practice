inp=input("Enter the string")
list=[]
list2=[]
count=0
flag=0
for i in inp:
    list.append(i)
final=[]
for j in list:
    final.append([list.count(j),ord(j)-96])
print(final)
for i,j in final:
    if i==j:
        #print("Equal")
        flag=flag+1
      
if flag==len(list):
    print("Equal")
