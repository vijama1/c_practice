start=int(input("Enter starting range"))
end=int(input("Enter ending range"))
primes_list=[]
count=0
for i in range(start,end):
    for j in range(2,i):
        if i%j==0:
            count=count+1
        else:
            continue
    print(count)
    if count>0:
        print("hello")
    else:
        print("Not prime")
        primes_list.append(i)
    count=0
print(primes_list)
