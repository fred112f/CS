n= input("Write a number: ")
n= int(n)
count= 1
for i in range (10):
	print (str(count) + "x" + str(n) + "=" + str ((count*n)))
	count=count+1
	