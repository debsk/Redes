import threading
# atividade 03 , v eh divisivel, 2 (ini, fim ) formulas em funcao de id 
def unknow_threading(t, id):
    ini   = len(v) // t
    fim   = t
    parte =  id * t  
    for i in range (ini + parte, fim  + parte):
        v[i] += 1
    return v 
    
v  = [0]*20  
v1 = []    
t  = int(input('threadings:'))  

for i in range (t):
    a = threading.Thread(target=unknow_threading, args = (t, i,))
    v1.append(a)
    a.start()

for j in v1:
    j.join()

print(unknow_threading())



