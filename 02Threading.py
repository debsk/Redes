import threading
# nao precisa ser o msm thread

def meu_thread_01(id):
    if id == 0 : 
        for i in range (len(v)//2):
            v[i] += 1  
    else: 
        for i in range (len(v)//2 , len(v)):
            v[i] += 1

v = [10] * 10 

t1 = threading.Thread(target=meu_thread_01, args = (0, ))
t1.start()

t2 = threading.Thread(target=meu_thread_01, args = (1, ))
t2.start()

t1.join()
t2.join()
print()
print(v)