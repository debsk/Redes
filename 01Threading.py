import threading, time, psutil

def meu_thread_memory(id):
    for i in range (5):
        m = psutil.virtual_memory()
        print("MEMORY", m)
        time.sleep(1)

def meu_thread_cpu(id):
    for i in range (5):
        n = psutil.cpu_percent( interval = 1 )
        print("CPU", n)
        time.sleep(1)


t1 = threading.Thread(target = meu_thread_memory, args = (id, ))
t1.start()
t2 = threading.Thread(target = meu_thread_cpu,    args = (id, ))
t2.start()
print()
print(t1)
print()
print(t2)