import socket, threading

def clientwhile_msg(con):
        print ("aguardando conexao") 
        print ("conectado") 
        print ("aguardando mensagem") 
        recebe = con.recv(1024) 
        print ("mensagem recebida:", recebe.decode('utf-8'))
        while recebe.decode('utf-8') != '0':
                recebe = con.recv(1024) 
                print ("mensagem recebida:", recebe.decode('utf-8'))
        con.close()
        print('conexao fechada')
        return recebe

host = '' 
port = 7000 
addr = (host, port)   
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10) 
while True:
        con, cliente = serv_socket.accept() 
        print(cliente)
        t1 = threading.Thread(target = clientwhile_msg, args = (con,))
        t1.start()
        clientwhile_msg(con)
        con.close()
serv_socket.close()

