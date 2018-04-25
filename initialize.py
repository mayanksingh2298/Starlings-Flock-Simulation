import bird
import hyperparameters as hp
import random
import math

listOfBirds = []
for i in xrange(hp.numberOfBirds):
	pos = [random.randint(hp.x_min+hp.boundaryThreshold,hp.x_max-hp.boundaryThreshold),random.randint(hp.y_min+hp.boundaryThreshold,hp.y_max-hp.boundaryThreshold),random.randint(hp.z_min+hp.boundaryThreshold,hp.z_max-hp.boundaryThreshold)]
	# pos[2]=0

	speed = random.randint(hp.v_min,hp.v_max)

	u_x = random.random()
	plusMinusRandom = random.random()
	if plusMinusRandom>0.5:
		u_x *= -1

	u_y = random.random()
	plusMinusRandom = random.random()
	if plusMinusRandom>0.5:
		u_y *= -1

	while u_y**2 + u_x**2 >= 1:
		u_y = random.random()
	u_z = math.sqrt(1 - u_x**2 - u_y**2)
	plusMinusRandom = random.random()
	if plusMinusRandom>0.5:
		u_z *= -1
	
	# u_z=0
	direction = [u_x,u_y,u_z]

	listOfBirds.append(bird.Bird(i,pos,speed,direction,20))

