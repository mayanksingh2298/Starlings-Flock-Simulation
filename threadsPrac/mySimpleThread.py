import threading
import time
lis = range(0,1000)
time1 = time.time()*1000000

def thread_task(lock,i):
    global lis
    # lock.acquire()
    total = sum(lis) - lis[i]
    lis[i] = total/1000
    # lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=thread_task,args=(lock,0,))
t2 = threading.Thread(target=thread_task,args=(lock,1,))
t3 = threading.Thread(target=thread_task,args=(lock,2,))
t4 = threading.Thread(target=thread_task,args=(lock,3,))

threadsList=[]
for i in range(1000):
	threadsList.append(threading.Thread(target=thread_task,args=(lock,i,)))
for i in range(1000):
	threadsList[i].start()
for i in range(1000):
	threadsList[i].join()


print lis
time2 = time.time()*1000000

print time2-time1