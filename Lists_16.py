###Write a Python program to get the smallest number from a list

len_list=int(input("Enter length of the list::"))
my_list=[]
for i in range(0,len_list):
	list_ele=int(input("Enter an integer value into list::"))
	my_list.append(list_ele)
print(my_list)
print(min(my_list))
