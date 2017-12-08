def vowel(word):
	if word[0] in("a", "e", "i", "o", "u","æ","ø","å"):
		return True
	return False
word= input("Type a word: ")
if vowel(word):
	print ("Starts with a vowel")
else:
	print ("Does not start with a vowel")
	