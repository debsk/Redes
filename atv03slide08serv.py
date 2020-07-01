from socket import *
import struct

def listaDivisores(N):
    
    lista = [1]
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            lista.append(i)
    if not N in lista:
        lista.append(N)
    return(lista)

serverPort   = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('localhost', serverPort))

serverSocket.listen(1)

while True:

    print("Piscou enviei!")
    conexaoSocket, end = serverSocket.accept()
    N_bytes            = conexaoSocket.recv(8)
    (N, )              = struct.unpack("i", N_bytes)
    X                  = listaDivisores(N)

    for i in range (len(X)):
        
        conexaoSocket.send(struct.pack("i",X[i]))

    conexaoSocket.close()







