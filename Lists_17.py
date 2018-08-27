### Write an interactive program that prints the smaller value among the three given  integers.


my_list=[]
for i in range(3):
	ele=int(input("Enter a value into my_list:: "))
	my_list.append(ele)
print("Your input is::")
print(my_list)
print("The smallest element in your list is.....")
print(min(my_list))