apsrtc=print("\t*****APSRTC*****")
ticketno=print("TNO:00065195")
start_point="vijayawada"
destination=input("Enter Destination:: ")
age=int(input("Enter age:: "))
fare=0
if(destination=='kodad'):
	fare=280
elif(destination=='suryapet'):
	fare=340
elif(destination=='hyderabad'):
	fare=520
if(age<5):
	fare=0
elif(5<=age<=13 or age>=60):
	fare=(fare*0.50)
print(f'Your fare is:: {fare}')	
print("Happy Journey...")
print("Thank You...")

