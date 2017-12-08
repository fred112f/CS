import random
print("I'm thinking of a number between 0 and 100")
target=random.randrange(1,101)
count= 0
wrong=0
score=100
while count==0 :
	number= input ("Is it: ")
	number= int(number)
	if (number<target):
		print("No, that's too low")
		wrong= wrong+1
		score=score-5
	elif (number>target):
		print("No,that's too high")
		wrong= wrong+1
		score= score-5
	elif (number==target) and (wrong==0):
		print("First try! Nice one!")
		print ("Score: "+ str(score))
		count=count+1
	elif (number==target):
		print ("That's correct!")
		print ("Amount of tries: "+ str(wrong))
		print ("Score: "+ str(score))
		count=count+1
					