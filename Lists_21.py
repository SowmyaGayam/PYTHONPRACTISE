 ### Write a double list comprehension over the lists ['A','B','C'] and [1,2,3]
###whose value is the list of all possible two-element lists [letter, number]

combo=[]
list1_len=int(input("Enter First list length:: "))
list1=[]
for i in range(0,list1_len):
	list1_ele=input("Enter First List Values:: ")
	list1.append(list1_ele)
list2_len=int(input("Enter Second list Length:: "))
list2=[]
for i in range(0,list2_len):
	list2_ele=input("Enter Second List Values:: ")
	list2.append(list2_ele)
print(list1)
print(list2)
for x in list1:
	for y in list2:
		#if x!=y:
			combo.append((x,y))
print(combo)
