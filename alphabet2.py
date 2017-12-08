def isalphabetical (word):
	for i in range(len(word)-1):
		if word[i]>word[i+1]:
			return False
	return True
word= input ("Enter a word: ")
if isalphabetical(word):
	print ("Alphabetical order")
else:
	print ("Not in alphabetical order")