##Given two inputs: the first input contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.
##Hint: You can use string.split() function to convert each line of text to a list of words. 



##step1
number_of_lines=int(input("How many lines do u want to enter::"))
list_of_words=[]
for line in range(number_of_lines):
	words=input("")
	list_of_words=list_of_words+words.split()
print("The list of all words entered are:"+str(list_of_words))
words_count_dict={word:list_of_words.count(word) for word in list_of_words}
print(words_count_dict)
max_count_words=[]
for word,word_count in words_count_dict.items():
	if word_count==max(words_count_dict.values()):
		max_count_words.append(word)
print("The words with maximum count are: "+str(max_count_words))
max_count_words.sort()
print("The word sorted alphabetically with max count is: "+max_count_words[0])

	
