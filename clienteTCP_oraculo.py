from socket import *

serverName = 'localhost'
serverPort = 12000

# Criacao do socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

pergunta = input('Pergunte ao oráculo: ')

# Conectar ao servidor
clientSocket.connect((serverName, serverPort))

# Envio de bytes. Repare que o endereco do destinatario eh necessario
clientSocket.send(pergunta.encode("utf-8"))

# Recepcao
resposta = clientSocket.recv(1024)
print ("Resposta:", resposta.decode("utf-8"))

# Fechamento
clientSocket.close()
