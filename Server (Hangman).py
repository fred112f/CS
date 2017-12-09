import socket
word=input("Enter a word: ")
sock = socket.socket()
host = input('Enter an ip: ')
port = 50007
sock.bind((host, port))
print ("I am thinking of the word "+str(word))

sock.listen(5)
conn = None

while True:
	if conn is None:
		print ('[Waiting for connection...]')
		conn, addr = sock.accept()
		print('Got connection from', addr)
	else:
		msg= str(word)
		conn.send(msg.encode('UTF-8'))
		
		