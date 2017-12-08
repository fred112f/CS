def integerN(t):
	retur=""
	li=[]
	for i in range (2,t):
			if (i % 2)== 0:
				li.append(i)
		if i>5:
			if i[-0]==5:
				li.remove(i)
	return (li)
t=int(input("Write an integer: "))
print (integerN(t))