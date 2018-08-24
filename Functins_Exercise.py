#def say_hi():
#	print("Hi! ")

#say_hi()




#	"""Sample function write hello"""
#	return "hello"


#print(say_hello.__doc__)


#def addItem(listParam):
#	listParam+=[1]
#	mylist=[1,2,3,4]
#	addItem(mylist)
#	print(len(mylist))


#a=[1,2,3,None,(),[]]
#print(len(a))


#nums = set([1,1,2,3,3,3,4])
#print(len(nums))


#i=0
#def change(i):
#	i=i+1
#	return i
#change(1)
#print(i)



#collect_args(*args)
#return collect_args


#collect_args(2,4,6,8)


#def greetPerson(*name):
#	print('Hello',name)


#greetPerson('Venkat','Sowmya')

#a=3
#b=7
#def swap(a,b):
#	temp=a
#	a=b
#	b=temp

#swap(a,b)

#print(a,b)



#confusion={}
#confusion[1]=1
#confusion['1']=2
#confusion[1.0]=4
#sum=0
#for k in confusion:
#	sum+=confusion[k]
#print(sum)


#boxes={}
#jars={}
#crates={}
#boxes['cereal']=1
#boxes['candy']=2
#jars['honey']=4
#crates['boxes']=boxes
#crates['jars']=jars
#print(len(crates[boxes]))


#numberGames={}
#numberGames[(1,2,4)]=8
#numberGames[(4,2,1)]=10
#numberGames[(1,2)]=12
#sum=0
#for k in numberGames:
#	sum+=numberGames[k]
#print(len(numberGames)+sum)



#my_tuple=(1,2,3,4)
#my_tuple.append((5,6,7))
#print(len(my_tuple))


#kvps={'1':1,'2':2,'3':3,'4':4,'5':5}
#newData={'1':10,'3':30}
#kvps.update(newData)
#x=sum(kvps.values())
#print(x)



#a=('check',)
#n=2
#for i in range(int(n)):
#	a=(a,)
#	print(a)



#a=(2,3,1,5)
#a.sort()
#a



#a={5,6,7,8}
#print(len(a))
#print(min(a))
#a.remove(5)
#a[2]=45



#a={5,6,7,8}
#b={7,5,6,8}
#a==b


a={i:'A'+str(i) for i in range(5)}
print(a)