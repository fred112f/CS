import random
print("I'm thinking of a number between 0 and 100")
target=random.randrange(1,3)
number= input ("Is it: ")
number= int(number)
count= 0
while count < target:
	print("No, that's too low")
	count=count+1
	number=input ("Is it: ")

