list1 = []
size = int(input("Enter size of the list:"))
for i in range(size):
    lst = []
    for j in range(2):
        elements = input("Enter elements in each tuple one after other of the list:")
        lst.append(elements)
    list1.append(lst)
print("the values in list are",list1)

tup_list=[]
for i in list1:
    tup_list.append(tuple(i))
print("Tuple list is:",tup_list)

for i in range(len(tup_list)):
    for j in range(len(tup_list)-i-1):
        if tup_list[j][-1]>tup_list[j+1][-1]:
            temp=tup_list[j]
            tup_list[j]=tup_list[j+1]
            tup_list[j+1]=temp
print("Output:",tup_list)






