from socket import *
import random

# Numero de porta na qual o servidor estara esperando conexoes.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_STREAM indicam TCP.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('localhost', serverPort))

serverSocket.listen(1)

listaResposta = ["Sim", "Não", "Talvez"]

# Loop infinito: servidor eh capaz de tratar multiplas conexoes
while 1:
        print("Aguardando conexão")
        
        # Aguarda conexão do cliente
        conexaoSocket, end = serverSocket.accept()
    
        # Aguardar novo pacote
        print ('Aguardando pacote de', end, "...")
        pergunta = conexaoSocket.recv(1024)

        # Processamento
        print(pergunta.decode("utf-8"))

        resposta = random.randint(0, 2)

        # Envio. Repare que o endereco do destinatario eh necessario.
        print ('Realizando envio...')
        conexaoSocket.send(listaResposta[resposta].encode("utf-8"))
        
        # Fecha a conexão
        conexaoSocket.close()

# Fechamento
print ('Fechando socket...')
serverSocket.close()