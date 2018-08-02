inp=input("Enter the number")
num=int(inp)
lis=[]
list_odd=[]
list_even=[]
odd_count=0
even_count=0
for i in inp:
    lis.append(i)
for j in range(0,len(lis),2):
    list_odd.append(lis[j])
for k in range(1,len(lis),2):
    list_even.append(lis[k])
print(lis)
print("Odd",list_odd)
print("Even",list_even)
odd=int(''.join(list_odd))
even=int(''.join(list_even))
print(odd)
print(even)
for i in range(2,odd):
    if(odd%i==0):
        odd_count=odd_count+1
for i in range(2,even):
    if(even%i==0):
        even_count=even_count+1
if odd_count==0:
    print("Number at odd position is prime")
else:
    print("Number at odd position is not prime")
if even_count>0:
    print("Number at even position is composite")
else:
    print("Number at even position is not composite")    
