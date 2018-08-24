my_list1=[]
my_list2=[]
list1_len=int(input("Enter list1 length:: "))
for i in range(list1_len):
	ele=int(input('Enter First list values:: '))
	my_list1.append(ele)
list2_len=int(input("Enter list2 length:: "))
for i in range(list2_len):
	ele=int(input('Enter Second list values:: '))
	my_list2.append(ele)
print(my_list1)
print(my_list2)
my_list1[-1:]=my_list2
print(my_list1)