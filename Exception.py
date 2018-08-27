#num1=int(input("Enter an integer"))
#num2=int(input("Enter another integer"))
#def divide_numbers(num1,num2):
#	try:
#		result=num1/num2
#		return result

#	except Exception as e:
#		raise
#	else:
#		pass
#	finally:
#		pass





while True:
	try:
		num=int(input("Enter a number....!: "))
	except ValueError:
		print('This is not a number....')
	else:
		print("Good Job")
	finally:
		print("Runs No matter")
print("Rest of game run")
