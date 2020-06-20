from socket import*
import time, psutil, struct
import pickle
porta          = 1200
nomeservidor   = 'localhost'
socketServidor = socket(AF_INET, SOCK_DGRAM)
socketServidor.bind(('localhost', porta))
mensagem_memoria   = []
mensagem_cpu       = []
s_memo = s_cpu = c = 0 

while True:
        # processamento 
        for i in range (60):
                a = psutil.swap_memory()
                m = a.percent
                n = psutil.cpu_percent( interval = 1 )
                print('MEMORY % = ', m)
                print('CPU    % = ', n)
                mensagem_memoria.append(m)
                mensagem_cpu.append(n)
                time.sleep(1)        
        for j in range (49, len(mensagem_cpu)):
                s_cpu += mensagem_cpu[j]
        media_cpu = s_cpu / 10 
        for h in range (49, len(mensagem_memoria)):
                s_memo += mensagem_memoria[h]
        media_memo = s_memo / 10 
        # preparando para eviar os dados para o cliente
        media, endereco = socketServidor.recvfrom(100000)
        result1 = media_memo
        result2 = media_cpu 
        media   = pickle.dumps(result1)
        media1  = pickle.dumps(result2)
        # enviando dados ao cliente
        socketServidor.sendto(media, endereco)
        socketServidor.sendto(media1, endereco)
        c += 1
        if c == 1 : 
                break 
socketServidor.close()
