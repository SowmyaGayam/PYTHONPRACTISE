names=['gowri','nanda','sitara']
names_upper=[name[0].upper() for name in names]
print(names_upper)



numbers=[1,2,3,4,5,6]
evens=[num for num in numbers if(num%2)==0]
odds=[num for num in numbers if(num%2)!=0]
print(evens)
print(odds)







numbers=[1,2,3,4]
print(f(numbers{-1}))




names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)






numbers=[1,2,3,4]
print(numbers[1:3])
