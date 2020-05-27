import socket 
ip   = '192.168.128.5'
port = 7000 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM$
client_socket.connect(addr) 

while True: #add um while 
    mensagem = input("digite uma mensagem para enviar ao servidor:")
    client_socket.send(mensagem.encode('utf-8')) 
    print ("mensagem enviada")
    client_socket.close()
    client_socket.connect(addr) 


