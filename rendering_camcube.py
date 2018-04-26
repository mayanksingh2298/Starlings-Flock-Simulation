import pygame
import hyperparameters as hp
import math

def rotate2d(pos,rad):
	x,y = pos
	s,c = math.sin(rad*3.14/180), math.cos(rad*3.14/180)
	return x*c-y*s,y*c+x*s
class Cam:
	def __init__(self,pos=(0,0,0),rot=(0,0)):
		self.pos = list(pos)
		self.rot = list(rot)
	def events(self,event):
		if event.type == pygame.MOUSEMOTION:
			x,y = event.rel
			x/=1
			y/=1
			print x,y

			# self.rot[0] =400
			# self.rot[1] =400

			self.rot[0] +=y
			self.rot[1] +=x
	def update(self,dt,key):
		s = dt*10
		if key[pygame.K_q]: self.pos[1]+=s
		if key[pygame.K_e]: self.pos[1]-=s
		
		x,y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

		if key[pygame.K_w]: self.pos[0]+=x; self.pos[2]+=y
		if key[pygame.K_s]: self.pos[0]-=x; self.pos[2]-=y
		if key[pygame.K_a]: self.pos[0]-=y; self.pos[2]+=x
		if key[pygame.K_d]: self.pos[0]+=y; self.pos[2]-=x



pygame.init()

mainDisplay = pygame.display.set_mode((hp.window_width,hp.window_height))
pygame.display.set_caption('Starlings')
mainDisplay.fill(hp.colorwhite)
pygame.display.update()
clock = pygame.time.Clock()
cam = Cam((0,0,-5))


def drawbird(r):
	# points = []
	x=int(r[0])
	y=int(r[1])
	z=int(r[2])
	x-=cam.pos[0]
	y-=cam.pos[1]
	z-=cam.pos[2]

	x,z = rotate2d((x,z),cam.rot[1])
	y,z = rotate2d((y,z),cam.rot[0])

	f = 200/z
	x,y = x*f,y*f


	# r_xy=[int(r[0]),int(r[1])]
	depthColor = (0,0,int(r[2])*255/(hp.z_max-hp.boundaryThreshold))
	pygame.draw.circle(mainDisplay,depthColor,(int(x),int(y)),5)
	pygame.draw.circle(mainDisplay,hp.colorgreen,(int(x),int(y)),hp.R,3)
	pygame.draw.circle(mainDisplay,hp.colorred,(int(x),int(y)),hp.r,3)


def updateDisplay():
	pygame.display.update()
print ""
