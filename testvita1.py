inp=int(input("Enter number of test cases"))
modules=int(input("Enter number of modules"))
list1=[]
list2=[]
hours=[]
list3=[]
dependency=[]
res=[]
sum=0
for i in range(0,modules):
    list1.append([int(input("Enter serial number")),int(input("Enter hours")),int(input("Enter dependency"))])
for k in range(0,len(list1)):
    hours.append(list1[k][1])
    dependency.append(list1[k][2])
print(hours)
print(dependency)
for i in range(0,len(dependency)):
    while dependency.count(dependency[i])<2:
        sum=sum+hours[i]
        list3.append(hours[i])
        #dependency.remove(dependency[i])
        break
res = list(set(hours)^set(list3))
sum=sum+max(res)
print(res)
print(hours)
#print(hours-list3)
print(sum)
# for i in range(0,len(list1)):
#     while list1[i][3]!=list1[i+1][3]:
#         sum=sum+list[i][2]
