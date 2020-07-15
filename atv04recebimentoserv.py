import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 12000))
print ('Socket criado!')
sock.listen(5)
print ('Esperando conexão...')

conn, addr = sock.accept()
filename   = 'C:\\Users\\debor\\Desktop\\arq.txt'
file       = open(filename, 'rb')
kar        = file.read(6053)
conn.send(kar)
print ('Arquivo enviado!')
file.close()
conn.close()
sock.close()