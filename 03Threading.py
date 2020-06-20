import threading
# atividade 03 , v eh divisivel, 2 (ini, fim ) formulas em funcao de id 
def unknow_threading(t, id):
    tamanho = len(v)//t
    if id < len(v) % t :
        tamanho += 1 
        desl = 0 
    else: 
        desl = len(v) % t
    ini     =  id * tamanho + desl
    fim     =  (id + 1) * tamanho + desl 
    for i in range (ini, fim):
        v[i] += 1
            
    

v1 = []    
t  = int(input('threadings:')) 
n  = int(input("tamanho do vetor: "))
v  = [0] *n  

for i in range (t):
    a = threading.Thread(target=unknow_threading, args = (t, i,))
    v1.append(a)
    a.start()

for j in v1:
    j.join()

print(v)



