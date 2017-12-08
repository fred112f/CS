name=input("Enter a name: ")
li=[]
while name!="x":
	li.append(name)
	name=input("Enter a name: ")
print ("The names you entered were: ")
for names in li:
	print(names)
	