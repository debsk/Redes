from socket import *
import struct
import pickle
def listaDivisores(N):
    lista = [1]
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            lista.append(i)
    if not N in lista:
        lista.append(N)
    return(lista)
# Numero de porta na qual o servidor estara esperando conexoes.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_DGRAM indicam UDP.
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('localhost', serverPort))

# Loop infinito: servidor eh capaz de tratar multiplas conexoes
while 1:
        # Aguardar novo pacote
        print ('Aguardando pacote...')
        N_byte, addr = serverSocket.recvfrom(8)

        # Processamento
        (N, ) = struct.unpack("i", N_byte)
        lista = listaDivisores(N)

        lista_bytes = pickle.dumps(lista)

        # Envio. Repare que o endereco do destinatario eh necessario.
        print ('Realizando envio...')
        serverSocket.sendto(lista_bytes, addr)

# Fechamento
print ('Fechando socket...')
serverSocket.close()
