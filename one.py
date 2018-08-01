inp=int(input("Enter the number"))
count=0
mul=0
if inp<11:
    print(2*inp-1)
elif inp==11:
    print('2')
elif inp>11 and inp<121:
    print("hi")
    eleven=int(inp/11)
    ones=inp%11
    plus=(2*eleven-1+ones-1)+1
    total=eleven+ones+plus
else:
    n=inp
    while(n>=11):
        count=count+2
        mul=mul+1
        n=int(n/11)
    multiplication=count+mul-1
    product=int(inp/121)
    ones=int(inp%121)
    plus=ones
    eleven=4*product
    total=multiplication+ones+plus
print(product)
print(eleven)
print(ones)
print(plus)
print(total)
