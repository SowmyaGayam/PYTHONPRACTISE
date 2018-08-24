A=int(input("Enter any integer:: "))
B=int(input("Enter another integer:: "))
if(A<B):
	for i in range(A,B+1):
		print(i)
elif(B<=A):
	for i in range(A,B):
		print(i)
