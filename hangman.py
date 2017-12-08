def hangman (word): #The function hangman is the game itself. Word is the word to guess.
	progress=["_"]*len(word) #Progress is the length of the word in underscore. The variable contains all correct letters guessed by user.
	cont= 1 #This variable is used to breakout of the while loop.
	winc=0 #This variable is the number of correct guesses.
	winh=0 #This variable is the number of incorrect guesses.
	already="" #This varible is used to "contain" letter.
	while cont==1: #Infinite loop until cont is different from 1.
		while True: #Infinite loop until break.
			letter=input("Enter a letter: ")
			if letter in already: #Check if letter was previously typed by user.
				print ("Already typed")
			else:
				break #If letter is not typed by user before, it will break out of the loop.
		already=already+letter #Already stores letter typed by user.
		count=0 #Is the start position to search for letter in word
		while word.find(letter,count)>-1: #Remains in a while loop as long as letter typed by user is found in word.
			position= word.find(letter,count) #The variable position contains the first occurrence of letter in word.
			progress[position]=letter #The variable progress is updated with letter at the correct position.
			count=position+1 #Count contains the new position to search for new occurrence of letter in word.
			winc=winc+1 #Update with number of correct guesses.
		if letter in word: #If the letter is in word user is informed.
			print ("Correct")
		else:
			winh=winh+1 #Update with number of incorrect guesses.
			print ("Incorrect") #If letter is not in the word user is informed
			if winh==1: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 9 tries left!")
				print ("/ \ ")
				print (" ")
			elif winh==2: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 8 tries left!")
				print (" :  ")
				print (" :  ")
				print (" :  ")
				print (" :  ")
				print (" :  ")
				print ("/ \ ")
				print (" ")
			elif winh==3: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 7 tries left!")
				print (" __________")
				print (" :         ")
				print (" :         ")
				print (" :         ")
				print (" :         ")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==4: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 6 tries left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :         ")
				print (" :         ")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==5: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 5 tries left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :        ☺")
				print (" :         ")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==6: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 4 tries left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :        ☺")
				print (" :        ▐")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==7: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 3 tries left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :        ☺")
				print (" :       -▐")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==8: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 2 tries left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :        ☺")
				print (" :       -▐-")
				print (" :         ")
				print ("/ \ ")
				print (" ")
			elif winh==9: #Output drawing of hangman and amount of tries left.
				print (" ")
				print ("You have 1 try left!")
				print (" __________")
				print (" :        :")
				print (" :        :")
				print (" :        ☺")
				print (" :       -▐-")
				print (" :       / ")
				print ("/ \ ")
				print (" ")
		if winh<10: #This will keep the user informed of how many correct letters are guessed as long as less than 10 tries have been used.
			tempfinal=" ".join(progress)
			print (tempfinal)
		if winh==10 or winc==len(word): #If the user guesses the word or the users uses 10 tries, cont is equal to 0 and the game stops.
			cont=0
		if winh==10: #If the user lost the final state of the hangman will be drawn and the user will be informed, that the user lost, what the correct word was and how many correct guesses.
			print (" __________")
			print (" :        :")
			print (" :        :")
			print (" :        ☺")
			print (" :       -▐-")
			print (" :       / \ ")
			print ("/ \ ")
			print (" ")
			print ("You lost!")
			print ("The word was "+"'"+word+"'")
			final="Correct letters: "+str(progress) #The variable final is "Correct letters:" and the list progress is converted to a string to be able to print it.
			print (final)
		if winc==len(word): #If users guesses the word the user will be informed with a message and the correct word.
			print("You guessed the word which was "+"'"+word+"'")
	return ("")
print("▄▄ ▄▄ ▒█░▒█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ▄▄ ▄▄" )
print("▄▄ ▄▄ ▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▄▄ ▄▄")
print("░░ ░░ ▒█░▒█ ▒█░▒█ ▒█░░▀█ ▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▒█░░▀█ ░░ ░░")
print ("")
print("Welcome to Hangman The Game! You have to guess the word you input.")
print("Amount of tries: 10")
print ("")
word=input ("Enter a word: ") #User inputs a word to guess.
print (hangman(word))
 