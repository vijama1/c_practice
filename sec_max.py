inp=int(input("Enter number of elemets"))
l=[]
i=0
while i<inp:
    l.append(int(input("Enter elemets")))
    i=i+1
max1=max(l)
l.remove(max1)
print(l)
sec=max(l)
print(sec)
