word= input ("Enter a word: ")
for i in range(len(word)-1):
	if word[i]<word[i+1]:
		print ("Alphabetical order")
print ("Not in alphabetical order")
		