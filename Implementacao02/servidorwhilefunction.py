import socket
def clientwhile_msg():
    global recebe 
    print ("aguardando conexao") 
    con, cliente = serv_socket.accept()  
    print ("conectado") 
    print ("aguardando mensagem") 
    recebe = con.recv(1024) 
    print ("mensagem recebida:", recebe.decode('utf-8'))
    con.close()

host = '' 
port = 7000 
addr = (host, port)   
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
l = True
while l:
    clientwhile_msg()
    while l: 
	clientwhile_msg()   
        if recebe.decode('utf-8') == '0': #problema, nao esta reconhecendo a str
            print("PROXIMO!")
            l = False
    l = True  
    serv_socket.close()
    serv_socket.bind(addr)
    serv_socket.listen(10)
