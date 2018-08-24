len_list=int(input("Enter length of the list::"))
my_list=[]
for i in range(0,len_list):
	list_ele=int(input("Enter an integer value into list::"))
	my_list.append(list_ele)
print(my_list)
print(min(my_list))
#min=my_list[0]
#or i in range(1,len_list):
#	if(my_list[i]<min):
#		min=my_list[i]
#	return min:
#print(f"Smallest number in list is::{min}")
