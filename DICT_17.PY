##Given a sequence of numbers, determine if the next number has already been encountered. For each number, print the word YES (in a ##separate line) if this number has already been encountered, and print NO, if it has not already been encountered.
my_list=[]
my_list_len=int(input("Enter length of the list:: "))
for i in range(0,my_list_len):
 	my_list_ele=input("Enter List Element::")
	my_list.append(my_list_ele)
	if(my_list_ele in my_list):
		print(my_list_ele)
		print("NO")
	else:
		print(my_list_ele)
		#my_list.append(my_list_ele)
		print("YES")
print(my_list)
 	