import socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.128.5"
port = 7000
s.connect((host,port))
print (s.recv(1024))
s.send("ola servidor1!")
s.close()
