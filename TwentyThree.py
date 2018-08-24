x1=int(input("Enter row value of current position of row between 1-8:: "))
y1=int(input("Enter column value of current position of column between 1-8:: "))
x2=int(input("Enter destintation row value 1-8:: "))
y2=int(input("Enter destintation column value 1-8:: "))
if((x1>0 and x1<9) and (y1>0 and y1<9) and(x2>0 and x2<9) and(y2>0 and y2<9)):
	if((x2==x1 or x2==x1+1 or x2==x1-1) and (y2==y1 or y2==y1+1 or y2==y1-1)):
		print("YES! Cary On, The King can move...")
	else:
		print("King can't move")
else:
	print("NO!You CAN'T play..You should enter 1-8 nos Only....")