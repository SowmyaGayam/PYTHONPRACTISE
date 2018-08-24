print("Enter 10 Integer values.... ")
a= list(map(int, input (). split (',')))
print(a)
t=0
for i in a:
	t=a[i]+t
	print(t)




