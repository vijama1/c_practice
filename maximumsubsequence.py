inp=int(input("Enter number of elements in tha array"))
array=[]
sum_list=[]
my_list=[]
for i in range(0,inp):
    array.append(int(input("Enter array elements")))

# for ele in range(1,len(array)):
#     while(i<len(array)):
#         first=array[i]
#         if array[ele]>first:
#             sum=sum+array[ele]+first
#         sum_list.append(sum)
#         sum=0
#         i=i+1
# print(sum_list)
# for i in range(0,len(array)):
#     for j in range(i+1,len(array)):
#         if array[j]>array[i]:
#             my_list.append([array[i],array[j]])
#             sum=sum+array[i]+array[j]
#             sum_list.append(sum)
#             sum=0
# print(my_list)
# print(sum_list)
sum=array[0]
max=array[0]
for i in range(1,inp):
    if array[i]>array[i-1]:
        sum=sum+array[i]
    else:
        sum=array[i]
    if sum>max:
        max=sum
print(max)
