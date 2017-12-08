def test (word):
	if (word[0]=="a" or "e" or "i" or "o" or "u"):
		return True
	return False
	
word= input("Type a word: ")
if test(word):
	print ("Starts with a vowel")
else:
	print ("Does not start with a vowel")
	