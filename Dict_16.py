test_string=input("Enter String::")
l=[]
l=test_string.split( )
word_count=[l.count(p) for p in l]
print(dict(1,word_count))