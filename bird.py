import hyperparameters as hp
import math
class Bird:
	"""The structure of the atomic bird"""
	birdCount = 0
	def __init__(self, ind, pos, speed, direction):
		Bird.birdCount += 1
		self.index=ind
		self.position = pos
		self.speed = speed
		self.direction = direction

	""" returns the bird count"""
	def displayCount(self):
		return Bird.birdCount

	""" these two functions help in printing the bird"""
	def __repr__(self):
		return str(self.index)+" "+str(self.position)+" "+str(self.speed)+" "+str(self.direction)
	def __str__(self):
		return str(self.index)+" "+str(self.position)+" "+str(self.speed)+" "+str(self.direction)

	"""overload the == operator"""
	def __eq__(self,other):
		return self.index==other.index

	"""update position"""
	def updatePosition(self,dt):
		self.position[0] = self.position[0]+self.speed*self.direction[0]*dt
		self.position[1] = self.position[1]+self.speed*self.direction[1]*dt
		self.position[2] = self.position[2]+self.speed*self.direction[2]*dt
	
	"""update speed"""
	def updateSpeed(self,F1,F3,dt):
		spd = self.speed + (hp.v_min + (hp.v_max-hp.v_min)*2*(F1+F3-0.5))*dt
		if spd>hp.v_max:
			self.speed = hp.v_max
		elif spd<hp.v_min:
			self.speed = hp.v_min
		else:
			self.speed = spd

	"""update direction by position of other birds"""
	def directionByOthersPosition(self,neighboursList):
		if len(neighboursList)!= 0:
			x_avg = 0
			y_avg = 0
			z_avg = 0
			for b in neighboursList:
				x_avg += b.position[0]
				y_avg += b.position[1]
				z_avg += b.position[2]
			x_avg/=float(len(neighboursList))
			y_avg/=float(len(neighboursList))
			z_avg/=float(len(neighboursList))
			# print self
			# print neighboursList
			denominator = math.sqrt((x_avg-self.position[0])**2+(y_avg-self.position[1])**2+(z_avg-self.position[2])**2)
			return [(x_avg-self.position[0])/denominator,(y_avg-self.position[1])/denominator,(z_avg-self.position[2])/denominator]
		else:
			return self.direction
	"""direction by other birds' direction"""
	def directionByOthersDirection(self,neighboursList):
		if len(neighboursList)!=0:
			ux_avg = 0
			uy_avg = 0
			uz_avg = 0
			for b in neighboursList:
				ux_avg += b.direction[0]
				uy_avg += b.direction[1]
				uz_avg += b.direction[2]
			ux_avg/= float(len(neighboursList))
			uy_avg/= float(len(neighboursList))
			uz_avg/= float(len(neighboursList))

			denominator = math.sqrt(ux_avg**2+uy_avg**2+uz_avg**2)
			return [ux_avg,uy_avg,uz_avg]
		else:
			return self.direction

	"""repulsion due to very close neighbours"""
	def repulsionByTooCloseNeighbours(self,neighboursList):
		if len(neighboursList)!=0:
			num_x=0
			num_y=0
			num_z=0
			den=0
			for b in neighboursList:
				d_k=[self.position[0]-b.position[0],self.position[1]-b.position[1],self.position[2]-b.position[2]]
				w_k=hp.r-math.sqrt(d_k[0]**2+d_k[1]**2+d_k[2]**2)

				den+=w_k
				num_x+=w_k*d_k[0]
				num_y+=w_k*d_k[1]
				num_z+=w_k*d_k[2]

			num_x = num_x/den
			num_y = num_y/den
			num_z = num_z/den
			# print self
			# print neighboursList
			den = math.sqrt(num_x**2+num_y**2+num_z**2)
			return [num_x/den,num_y/den,num_z/den]
		else:
			return self.direction

	"""update direcection due to boundary problem"""
	def repulsionDueToBoundary(self):
		return [-1*(self.direction[0]),-1*(self.direction[1]),-1*(self.direction[2])]

	"""update considering all factors"""
	def update(self,allBirds):
		neighbours_R=[]
		neighbours_r=[]

		for b in allBirds:
			if b==self or (b.position[0]==self.position[0] and b.position[1]==self.position[1] and b.position[2]==self.position[2]):
				continue
			if(math.sqrt((self.position[0]-b.position[0])**2+(self.position[1]-b.position[1])**2+(self.position[2]-b.position[2])**2)<hp.r):
				neighbours_r.append(b)
			if(math.sqrt((self.position[0]-b.position[0])**2+(self.position[1]-b.position[1])**2+(self.position[2]-b.position[2])**2)<hp.R):
				neighbours_R.append(b)
		dir1=self.directionByOthersPosition(neighbours_R)
		dir2=self.directionByOthersDirection(neighbours_R)
		dir3=self.repulsionByTooCloseNeighbours(neighbours_r)
		dir4=self.repulsionDueToBoundary()
		F1=0
		F2=0
		F3=0
		F4=0
		if(self.position[0]<hp.boundaryThreshold or self.position[1]<hp.boundaryThreshold or self.position[2]<hp.boundaryThreshold or self.position[0]>hp.x_max-hp.boundaryThreshold or self.position[1]>hp.y_max-hp.boundaryThreshold or self.position[2]>hp.z_max-hp.boundaryThreshold):
			F1=0
			F2=0
			F3=0
			F4=1
		elif(len(neighbours_r)!=0):
			F1=hp.F1whentooclose
			F2=hp.F2whentooclose
			F3=hp.F3whentooclose
			F4=0
		else:
			if(len(neighbours_R)!=0):
				x_avg = 0
				y_avg = 0
				z_avg = 0
				for b in neighbours_R:
					x_avg += b.position[0]
					y_avg += b.position[1]
					z_avg += b.position[2]
				x_avg/=float(len(neighbours_R))
				y_avg/=float(len(neighbours_R))
				z_avg/=float(len(neighbours_R))
				D=math.sqrt((self.position[0]-x_avg)**2+(self.position[1]-y_avg)**2+(self.position[2]-z_avg)**2)
				F1=D/hp.R
				F2=1-D/hp.R
			else:
				F1=1
				F2=0
			F3=0
			F4=0
		newDir=[F1*dir1[0]+F2*dir2[0]+F3*dir3[0]+F4*dir4[0],F1*dir1[1]+F2*dir2[1]+F3*dir3[1]+F4*dir4[1],F1*dir1[2]+F2*dir2[2]+F3*dir3[2]+F4*dir4[2]]
		D=math.sqrt(newDir[0]**2+newDir[1]**2+newDir[2]**2)
		print F1,F2,F3,F4
		self.direction=[newDir[0]/D,newDir[1]/D,newDir[2]/D]
		self.updatePosition(hp.deltaT)
		self.updateSpeed(F1,F3,hp.deltaT)
