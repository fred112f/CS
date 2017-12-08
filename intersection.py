def intersection(a,b):
	retur=""
	lista=[]
	listb=[]
	lista.append(a)
	listb.append(b)
	if len(lista)==len(listb):
		for i in range(len(lista)):
			if lista[i]==listb:
				retur=retur+str(lista[i])
	print (retur)
count=0
while count==0:
	a=input("Type something: ")
	b=input ("Type something else: ")
	
