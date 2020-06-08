import threading
# atividade 03 
def unknow_threading(id):
    quant = n / nt
    if id <= quant  :
        for i in range (quant):
            v[i] += 1 

n  = int(input('tamanho do vetor:'))
nt = int(input('threadings:'))
v  = [0]*n
t1 = threading.Thread(target = unknow_threading, args = (nt, ))
 
t  = []
for i in range (nt):
    t.append(t1.join())

print(t)


