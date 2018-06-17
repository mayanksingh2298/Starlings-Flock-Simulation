import multiprocessing
class A:
	def __init__(self):
		self.x=1
def foo(q):
	tmp = q.get()
	print tmp
	


a1 = A()
a2 = A()
a3 = A()
a4 = A()

manager = multiprocessing.Manager()
l = manager.list()
l.append([a1,a2])
l.append([a3,a4])

queue = multiprocessing.Queue()
a1.x=1
a2.x=2
queue.put([a1,a2])
queue.put([a3,a4])





t1 = multiprocessing.Process(target=foo,args=(queue,))
t1.start()
t1.join()


# foo()
queue.get()
print queue.get()