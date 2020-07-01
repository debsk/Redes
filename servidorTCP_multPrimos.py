from socket import *
import struct
import math

def ehprimo(N):
    
    retorno = True
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            retorno = False
            break

    return retorno
        

# Numero de porta na qual o servidor estara esperando conexoes.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_STREAM indicam TCP.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('localhost', serverPort))

serverSocket.listen(1)

while True:
    print("Aguardando conexão")
        
    # Aguarda conexão do cliente
    conexaoSocket, end = serverSocket.accept()
    
    # Recebe N em bytes
    N_bytes = conexaoSocket.recv(8)
    
    (N, ) = struct.unpack("i", N_bytes)
    
    menor = 1
    
    if N > 1:
        menor = N
        
        while not ehprimo(menor):
            menor = menor - 1
    
    maior = N + 1
    
    while not ehprimo(maior):
        maior = maior + 1
    
    X = menor * maior
    
    conexaoSocket.send(struct.pack("i", X))
    
    conexaoSocket.close()
