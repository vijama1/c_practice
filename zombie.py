n=1
num=int(input("Enter number of zombies"))
time=int(input("Enter time"))
zom_energy=[]
for i in range(0,num):
    zom_energy.append(int(input("Enter energy of zombie")))
player_energy=int(input("Enter initial energy of the player"))
next_level=int(input("Enter minimum energy required for next level"))
for i in zom_energy:
    if player_energy>i and time>0:
        player_energy=player_energy+(player_energy-i)
        time=time-1
    else:
        print("No")
if player_energy>next_level:
    print("Go to next level")
else:
    print("Do not go to next level")
