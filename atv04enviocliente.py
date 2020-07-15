import socket
import os

sock     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12000))
filename = 'C:\\Users\\debor\\Documents\\arq.txt'
file     = open(filename, 'wb')
print('Iniciando...')

file.write(sock.recv(6053))
file.close()
sock.close()
print('Arquivo enviado!')