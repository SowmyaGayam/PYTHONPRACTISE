len_list=int(input("Enter the length of the list:: "))
my_list=[]
for i in range(0,len_list):
	number=int(input('Please enter a number: '))
	my_list.append(number)
print(my_list)
print(sum(my_list))
#sum=0
#for i in range(0,len_list):
#	sum=my_list[i]+sum
