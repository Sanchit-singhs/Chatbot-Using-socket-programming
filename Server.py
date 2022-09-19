from socket import *
from time import *

server = socket(AF_INET,SOCK_STREAM)
print('socket created')
server.bind(('192.168.96.170',9996))
server.listen()
print('waiting for connections')
connection,address = server.accept()
print("connected to client")
while True:
	data = input('Server: ')
	connection.send(bytes(data +ctime(), 'utf-8'))

	recdata = connection.recv(1024).decode()
	print('client :', recdata)
connection.close
