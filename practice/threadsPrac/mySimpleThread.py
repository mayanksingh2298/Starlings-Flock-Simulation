import threading
import time
lis = range(0,1000)
time1 = time.time()*1000000

def thread_task(lock,i):
    global lis
    # lock.acquire()
    for i in range(i,i+250):
	    total = sum(lis) - lis[i]
	    lis[i] = total/1000
    # lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=thread_task,args=(lock,0,))
t2 = threading.Thread(target=thread_task,args=(lock,250,))
t3 = threading.Thread(target=thread_task,args=(lock,500,))
t4 = threading.Thread(target=thread_task,args=(lock,750,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


print "threaded"
time2 = time.time()*1000000

print time2-time1