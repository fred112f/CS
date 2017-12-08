def caesar(word):
	retur=""
	for i in range(len(word)):
		t=word[i]
		a=ord(t)
		if a >96:
			if 32<a>32:
				if mode==("encode"):
					c=a+(rotation)
				else:
					c=a-(rotation)
				if c>122:
					c=c-26
				if c<97:
					c=c+26
				d=chr(c)
				retur=retur+d
			else:
				retur=retur+" "
		else:
			if 32<a>32:
				if mode==("encode"):
					c=a+(rotation)
				else:
					c=a-(rotation)
				if c>90:
					c=c-26
				if c<65:
					c=c+26
				d=chr(c)
				retur=retur+d
			else:
				retur=retur+" "
	return (retur)
rotation= int(input("Rotation: "))
mode= input ("Type encode or decode: ")
word= input ("Enter a plain text: ")
print (caesar(word))
