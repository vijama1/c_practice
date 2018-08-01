no=input("Enter the number")
l=[]
for i in no:
    l.append(i)
if(int(no)==int(no[::-1])):
    print("palindrome",max(l))
else:
    print("Not palindrome",min(l))
