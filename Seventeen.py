x=int(input('Enter x value'))
y=int(input('Enter y value'))
z=int(input('Enter z value'))
if(x<y):
	if(x<z):
		print('x is less than y and z')
	else:
		print('z is less than x and y')
else:
	if(y<z):
		print('y is less than x and z')
	else:
		print('z is less than x and y')
