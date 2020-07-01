from socket import *
import struct

serverName   = 'localhost'
serverPort   = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

N = int(input('Entre com um número: '))
    
clientSocket.connect((serverName, serverPort))

clientSocket.send(struct.pack("i", N))

for i in range (N):

    X_bytes = clientSocket.recv(4)
    (X, )   = struct.unpack("i", X_bytes)
    print(X)

clientSocket.close()



