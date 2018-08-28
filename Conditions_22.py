x1=int(input("Enter row value of current position of row between 1-8:: "))
y1=int(input("Enter column value of current position of column between 1-8:: "))
x2=int(input("Enter destintation row value 1-8:: "))
y2=int(input("Enter destintation column value 1-8:: "))
if((x1>0 and x1<9) and (y1>0 and y1<9) and(x2>0 and x2<9) and(y2>0 and y2<9)):
	if (((x1+x2)%2==1) and ((y1+y2)%2==1)):
		print(f"{(x1,y1)} and {(x2,y2)} are COLORED as same.....")
	else:
		print(f"{(x1,y1)} and {(x2,y2)} are not colored as same....")
else:
	print("Please check your input....")