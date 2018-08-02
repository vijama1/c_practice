string1=input("Enter first string: ")
string2=input("Enter second string: ")
list=[]
print(str(len(string1))+" "+str(len(string2)))
print(string1+" "+string2)
concat=string1+string2
print(concat)
for letter in concat:
    list.append(letter)
char=list[0]
list[0]=list[0+len(string1)]
list[0+len(string1)]=char
#print(list)
stringf=''.join(list)
first=stringf[0:len(string1)]
second=stringf[len(string1):len(list)]
print(first+" "+second)
