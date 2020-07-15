from socket import *
import struct, pickle

serverName   = 'localhost'
serverPort   = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

N = int(input('Entre com um número: '))
    
clientSocket.connect((serverName, serverPort))

clientSocket.send(struct.pack("i", N))
'''
tamanho_b   = clientSocket.recv(8)
(tamanho, ) = struct.unpack('i', tamanho_b)

for i in range (tamanho):

    X_bytes = clientSocket.recv(4)
    (X, )   = struct.unpack("i", X_bytes)
    print(X)
'''
X_bytes = clientSocket.recv(100000)
XX      = pickle.loads(X_bytes)
print(XX)

clientSocket.close()



