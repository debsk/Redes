from socket import *
import struct
import pickle

porta        = 1200
nomeServidor = 'localhost'

socketClient = socket(AF_INET, SOCK_DGRAM)

# enviando requisicao ao servidor 
mensagem     = 1
socketClient.sendto(struct.pack('i', mensagem), (nomeServidor, porta))

# recendo a media de memoria do servidor 
media, endereço = socketClient.recvfrom(1000)
med = pickle.loads(media)
print('media de memoria dos 10 ultimos = ', med)

# recebebdo informacoes da media de cpu dp servidor 
media1, endereco = socketClient.recvfrom(1000)
med1 = pickle.loads(media1)
print("media de cpu dos 10 ultimos     = ",med1)