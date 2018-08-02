num=int(input("Enter number of zombies"))
zombie=[]
count=0
for i in range(0,num):
    zombie.append(int(input("Enter energy of the zombie")))
bob=int(input("Enter bob's energy"))
for i in zombie:
    if bob>i:
        bob=bob-((i%2)+(i/2))
        count=count+1
print(bob)
if count==num:
    print("TO the next level")
else:
    print("Not to the next level")
