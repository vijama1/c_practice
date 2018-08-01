inp=int(input("Enter number of elemets of the array"))
sum=int(input("Enter sum"))
list=[]
n_sum=0
list1=[]
for i in range(0,inp):
    list.append(int(input("Enter array elements")))
k=0
i=0
j=inp-1
while(i<j):
    n_sum=list[i]+list[j]
    if n_sum==sum:
        print(list[i],list[j])
        i=i+1
        j=j-1
        break
    elif n_sum<sum:
        i=i+1
    else:
        j=j-1
