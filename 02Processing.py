import multiprocessing

def meu_thread_01(w): 
    for i in range (10):
        v[i] += 1  

v = [1] * 10 

if __name__ == '__main__':
    t1 = multiprocessing.Process(target = meu_thread_01, args = (1,))
    t1.start()

print(v)
