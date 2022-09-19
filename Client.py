from socket import *

client = socket()
client.connect(('localhost',9996))
print("Connected to server")
while True:
    recdata = client.recv(1024).decode()
    print("Server: ",recdata )
    data = input('client: ')
    client.send(bytes(data,'utf-8'))
client.close()
