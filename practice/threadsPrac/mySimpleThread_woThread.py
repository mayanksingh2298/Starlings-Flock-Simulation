import threading
import time
lis = range(1000)
time1 = time.time()*1000000

for i in range(0,1000):
    total = sum(lis) - lis[i]
    lis[i] = total/1000

print lis
time2 = time.time()*1000000

print time2-time1