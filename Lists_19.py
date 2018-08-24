my_list=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
print(my_list)
for i in range(len(my_list)-1):
	while(my_list[i]!=my_list[i+1]):
		#print("Not match")
		print(my_list[i])
		i=i+2
#print("Matched List")
#	print(my_list(i))


