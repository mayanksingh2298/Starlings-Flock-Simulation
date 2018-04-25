import math
import physics
import copy
import hyperparameters as hp
import hyperparameters as hp
import math
import sys
import initialize

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
mainDisplay = pygame.display.set_mode((hp.window_width,hp.window_height),DOUBLEBUF|OPENGL)
pygame.display.set_caption('Starlings')
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
glClearColor(1, 1, 1, 0)
pygame.display.flip()
clock = pygame.time.Clock()

#getting the list of initialized birds
listOfBirds = initialize.listOfBirds

vertices = ((hp.x_max, hp.y_min, hp.z_min),(hp.x_max, hp.y_max, hp.z_min),(hp.x_min, hp.y_max, hp.z_min),(hp.x_min, hp.y_min, hp.z_min),(hp.x_max, hp.y_min, hp.z_max),(hp.x_max, hp.y_max, hp.z_max),(hp.x_min, hp.y_min, hp.z_max),(hp.x_min, hp.y_max, hp.z_max),)
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7),)
def Draw_Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glColor3fv((0.8,0.8,0.8))
			glVertex3fv(vertices[vertex])
	glEnd()
def drawbird(r):
	# glBegin(GL_LINES)
	head = r.position
	tailCentre = (r.position[0]-20*r.direction[0],r.position[1]-20*r.direction[1],r.position[2]-20*r.direction[2])
	tmpDir1=[]
	tmpDir2=[]
	if r.direction[2]!=0:
		tmpDir1=[1,1,(-r.direction[0]-r.direction[1])/r.direction[2]]
		
	elif r.direction[1]!=0:
		tmpDir1=[1,1,(-r.direction[0]-r.direction[2])/r.direction[1]]
	else:
		tmpDir1=[1,1,(-r.direction[1]-r.direction[2])/r.direction[0]]

	D = math.sqrt(tmpDir1[0]**2+tmpDir1[1]**2+tmpDir1[2]**2)
	tmpDir1=[tmpDir1[0]/D,tmpDir1[1]/D,tmpDir1[2]/D]
	tmpDir2=[tmpDir1[1]*r.direction[2]-tmpDir1[2]*r.direction[1],tmpDir1[2]*r.direction[0]-tmpDir1[0]*r.direction[2],tmpDir1[0]*r.direction[1]-tmpDir1[1]*r.direction[0]]
	D = math.sqrt(tmpDir2[0]**2+tmpDir2[1]**2+tmpDir2[2]**2)
	tmpDir2=[tmpDir2[0]/D,tmpDir2[1]/D,tmpDir2[2]/D]

	tailSq1 = (tailCentre[0]-8*tmpDir1[0],tailCentre[1]-8*tmpDir1[1],tailCentre[2]-8*tmpDir1[2])
	tailSq2 = (tailCentre[0]+8*tmpDir1[0],tailCentre[1]+8*tmpDir1[1],tailCentre[2]+8*tmpDir1[2])  
	tailSq3 = (tailCentre[0]-8*tmpDir2[0],tailCentre[1]-8*tmpDir2[1],tailCentre[2]-8*tmpDir2[2])
	tailSq4 = (tailCentre[0]+8*tmpDir2[0],tailCentre[1]+8*tmpDir2[1],tailCentre[2]+8*tmpDir2[2])
	

	glBegin(GL_TRIANGLES)
	glColor3fv((0.5,0.5,0.5))
	glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	glEnd()
	glBegin(GL_TRIANGLES)
	glColor3fv((0.7,0.7,0.7))
	glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	glEnd()
	glBegin(GL_TRIANGLES)
	glColor3fv((0.5,0.5,0.5)) 
	glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	glEnd()
	glBegin(GL_TRIANGLES)
	glColor3fv((0.7,0.7,0.7))
	glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	glEnd()
	glBegin(GL_QUADS)
	glColor3fv((0.4,0.4,0.4))
	glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	glEnd()
	
	# glBegin(GL_LINES)
	# glColor4f(255,255,255,0) 
	# glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	# glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	# glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	# glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	# glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	# glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	# glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
	# glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	# glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	# glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	# glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	# glVertex3fv((int(tailSq3[0]),int(tailSq3[1]),int(tailSq3[2])))
	# glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	# glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
	# glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	# glVertex3fv((int(tailSq4[0]),int(tailSq4[1]),int(tailSq4[2])))
	# glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
	# glEnd()



	# glVertex3fv((int(tailCentre[0]),int(tailCentre[1]),int(tailCentre[2])))

	# glEnd()

gluPerspective(45.0,(hp.window_width/hp.window_height),1,10000.0)

#moving back
glTranslatef(0,0,-2000.0)
rotateX=0
rotateY=0
rotateZ=0
clock = pygame.time.Clock()
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
	# print listOfBirds[0]
	# print "---Force---"
	# print force
	# print "---angularmomentum---"
	# print angularmomentum
	# print "---Power---"
	# print power


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print  event
			print event.button
			if event.button ==4:
				glTranslatef(0.0,0.0,10.0)
			elif event.button ==5:
				glTranslatef(0.0,0.0,-10.0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

			if event.key == pygame.K_w:
				rotateX = 5
			if event.key == pygame.K_s:
				rotateX = -5
			if event.key == pygame.K_a:
				rotateY = 5
			if event.key == pygame.K_d:
				rotateY = -5
			if event.key == pygame.K_q:
				rotateZ = 5
			if event.key == pygame.K_e:
				rotateZ = -5
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				rotateX = 0
			if event.key == pygame.K_s:
				rotateX = 0
			if event.key == pygame.K_a:
				rotateY = 0
			if event.key == pygame.K_d:
				rotateY = 0
			if event.key == pygame.K_q:
				rotateZ = 0
			if event.key == pygame.K_e:
				rotateZ = 0



	glRotatef(rotateX,1,0,0)
	glRotatef(rotateY,0,1,0)
	glRotatef(rotateZ,0,0,1)

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glClearColor(1, 1, 1, 0)

	Draw_Cube()
	for b in listOfBirds:
		drawbird(b)

	# displayPoints()
	pygame.display.flip()
	# ch = raw_input()
	pygame.time.wait(hp.fps)