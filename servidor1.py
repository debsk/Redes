import socket 
host = "192.168.128.5"
port = "1001"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn,addr = s.accept()
print(addr,"Now Connected")
conn.send("HELLO IM DEBORA!")
conn.close()
