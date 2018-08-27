# Write a Python program to replace the last element in a list with another list. Go to the editor
#Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

my_list1_len=int(input("Enter First List length:: "))
my_list1=[]
for i in range(0,my_list1_len):
	list1_ele=int(input("Enter First list elements..... "))
	my_list1.append(list1_ele)
my_list2_len=int(input("Enter Second List length:: "))
my_list2=[]
for i in range(0,my_list2_len):
	list2_ele=int(input("Enter Second list elements....."))
	my_list2.append(list2_ele)
##Poping Last element in First List.....
my_list1.pop()
##Appending Second List to First List....
my_list1.append(my_list2)
print("First List")
print(my_list1)
print("Second List")
print(my_list2)


