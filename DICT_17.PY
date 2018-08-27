 ##Given a sequence of numbers, determine if the next number has already been encountered. For each number, print the word YES (in a ##separate line) if this number has already been encountered, and print NO, if it has not already been encountered.
my_list=[]
new_list=[]
my_list_len=int(input("Enter length of the list:: "))
for i in range(0,my_list_len):
	my_list_ele=input("Enter List Element::")
 	my_list.append(my_list_ele)
print(my_list)
for i in range(0,list_len):
 	if(my_list[i]==new_list[i]):
 		print("YES")
 	else:
 		new_list.append(my_list[i])
 		print("NO")
