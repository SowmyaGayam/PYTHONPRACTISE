mixture=[]
my_list=[]
my_list_len=int(input("Enter length of the list:: "))
for i in range(0,my_list_len):
	my_list_ele=input("Enter List elements:: ")
	my_list.append(my_list_ele)
list_range=int(input("Enter List range from 0 to n:: "))
for i in my_list:
	for j in (1,list_range):
		mixture.append((i,j))
print(my_list)
print(list_range)
print(mixture)
