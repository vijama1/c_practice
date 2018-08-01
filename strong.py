import math
sum=0
number=input("Enter the number")
list=[]
for i in number:
    list.append(i)

for i in list:
    sum=sum+math.factorial(int(i))
print(sum)
if sum==int(number):
    print("It's a strong number")
else:
    print("It's not a strong number")    
