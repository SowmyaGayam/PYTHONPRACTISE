annual_salary=int(input("Hi, Please Enter ur annual_salary:: "))
rent_paid=int(input("Enter the amount u paid as rent for year:: "))
donation=int(input("Enter donation u paid in this year:: "))
taxable_amount=0
tax=0
if(annual_salary<=250000):
	print("Hi, You are tax free..Enjoy...")
else:
	taxable_amount=annual_salary-250000
if(rent_paid>0 and rent_paid<=100000):
	taxable_amount=taxable_amount-rent_paid
elif rent_paid>100000:
	taxable_amount=taxable_amount-100000
if(donation>0 and donation<=80000):
	taxable_amount=taxable_amount-donation
elif donation>80000:
	taxable_amount=taxable_amount-80000
if taxable_amount>0:
	tax=taxable_amount*(10/100)
	print(f"Your tax amount is: "{tax})
else:
	print("You need not to pay any tax..")

