integer= input ("What integer?: ")
integer= int(integer)
li=[]
for i in range (integer):
	i=i+1
	i=i*i
	li.append(i)
print (li[-5:])	
