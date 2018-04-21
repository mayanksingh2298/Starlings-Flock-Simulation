import math
import physics
import copy
import hyperparameters as hp
import rendering
def distanceOfEach():
	global listOfBirds
	for i in listOfBirds:
		print i," ->",
		for j in listOfBirds:
			d = math.sqrt((i.position[0]-j.position[0])**2+(i.position[1]-j.position[1])**2+(i.position[2]-j.position[2])**2)
			print d,
		print ""
import initialize

#getting the list of initialized birds
listOfBirds = initialize.listOfBirds
# print listOfBirds
while True:
	
	force=[]
	angularmomentum=[]
	power=[]

	copyListOfBirds=[]
	for b in listOfBirds:
		copyListOfBirds.append(copy.deepcopy(b))

	for	b in listOfBirds:
		b.update(copyListOfBirds)
		force.append(physics.force(hp.mass,[x*b.speed for x in b.direction],[x*copyListOfBirds[b.index].speed for x in copyListOfBirds[b.index].direction],hp.deltaT))
		angularmomentum.append(physics.angularMomentum(hp.mass,b.position,[x*b.speed for x in b.direction]))
		power.append(physics.power(force[-1],[x*b.speed for x in b.direction]))
	print listOfBirds[0]
	# print "---Force---"
	# print force
	# print "---angularmomentum---"
	# print angularmomentum
	# print "---Power---"
	# print power
	rendering.mainDisplay.fill(hp.colorwhite)
	for b in listOfBirds:
		rendering.drawbird(b.position)

	rendering.updateDisplay()
	
	rendering.clock.tick(hp.fps)
	# ch = raw_input()