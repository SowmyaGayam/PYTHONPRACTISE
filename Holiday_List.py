import datetime
input_date = input("Enter your required date in 'YYYY-MM-DD' FORMAT...")
YEAR,MONTH,DAY=input_date.split('/')
isValidDate=TRUE
if(datetime.datetime(int(YEAR),int(MONTH),int(DAY))):
	print(input_date)
else:
	print('Entered wrong input format......')