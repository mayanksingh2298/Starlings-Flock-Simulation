import threading
 
# global variable x
x = 0

def thread_task(lock):
    global x
    
    for _ in range(100000):
        lock.acquire()
        x=x+1
        lock.release()
 
def main_task():
    global x
    x = 0
 
    # creating a lock
    lock = threading.Lock()
 
    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
 
    # start threads
    t1.start()
    t2.start()
 
    # wait until threads finish their job
    t1.join()
    t2.join()
 
if __name__ == "__main__":
    main_task()
    print x