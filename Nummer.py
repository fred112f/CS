print ("Try to guess the number I am thinking of. You can try 5 times.")
print ("Guess a number from 1-100")
for i in range (5):
	number = input("Number: ")
	if (number == "63"):
		print ("That is correct!")
		quit()
	else:
		if i == 3:
			print ("Last try!")
		else:
			if i ==4:
				print ("So close! Better luck next time!")
			else:
				print ("That is incorrect!")