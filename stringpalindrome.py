from itertools import permutations
inp=input("Enter your string")
list1=[]
list2=[]
permutation=[]
for i in inp:
    list1.append(i)
# perm=permutations(list)
# for char in list:
#     permutation.append(permutations(char))
# print(permutation)
perms=[''.join(p) for p in permutations(inp)]
for words in perms:
    if words==words[::-1]:
        list2.append(words)
print(list(set(list2)))
