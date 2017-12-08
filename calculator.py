count= 0
while count ==0:
	fahrenheit= input ("Enter fahrenheit: ")
	if fahrenheit==str('x'):
		count=count+1
	else:
		fahrenheit=int(fahrenheit)
		celsius= (fahrenheit-32)*5/9
		print (str(celsius) + " celsius")