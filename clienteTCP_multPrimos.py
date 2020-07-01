from socket import *
import struct

serverName = 'localhost'
serverPort = 12000

# Criacao do socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

N = 0
entrada_ok = False
while not entrada_ok:
    try:
        N = int(input('Entre com um número: '))
        entrada_ok = True
    except Exception as texto:
        print("Erro de entrada. Digite um número!")
    
# Conectar ao servidor
clientSocket.connect((serverName, serverPort))

# Envio de bytes. Repare que o endereco do destinatario eh necessario
clientSocket.send(struct.pack("i", N))

# Recepcao
X_bytes = clientSocket.recv(8)

(X, ) = struct.unpack("i", X_bytes)

print ("Resposta:", X)

# Fechamento
clientSocket.close()