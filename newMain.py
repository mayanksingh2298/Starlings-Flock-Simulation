import math
import physics
import copy
import hyperparameters as hp
import math
import sys
import initialize
import multiprocessing
import bird
import time

import logging
import sys
import os

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
manager = multiprocessing.Manager()


pygame.init()
mainDisplay = pygame.display.set_mode((hp.window_width,hp.window_height),DOUBLEBUF|OPENGL)
pygame.display.set_caption('Starlings')
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
glClearColor(1, 1, 1, 0)
pygame.display.flip()
clock = pygame.time.Clock()

#getting the list of initialized birds
listOfBirdsTmp = []
for b in initialize.getRandomList():
	listOfBirdsTmp.append(copy.deepcopy(b))
listOfBirds=manager.list()
listOfBirds.extend(listOfBirdsTmp)

vertices = ((hp.x_max, hp.y_min, hp.z_min),(hp.x_max, hp.y_max, hp.z_min),(hp.x_min, hp.y_max, hp.z_min),(hp.x_min, hp.y_min, hp.z_min),(hp.x_max, hp.y_min, hp.z_max),(hp.x_max, hp.y_max, hp.z_max),(hp.x_min, hp.y_min, hp.z_max),(hp.x_min, hp.y_max, hp.z_max),)
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7),)
def Draw_Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glColor3fv((0.8,0.8,0.8))
			glVertex3fv(vertices[vertex])
	glEnd()
def drawbirds(listOfBirds):
	# glBegin(GL_LINES)
	rotateX=0
	rotateY=0
	rotateZ=0
	copyListOfBirds = (listOfBirds)
	while True:
		force=[]
		angularmomentum=[]
		power=[]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button ==4:
					glTranslatef(0.0,0.0,10.0)
				elif event.button ==5:
					glTranslatef(0.0,0.0,-10.0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
				if event.key == pygame.K_r: #RESET
					ct=0
					for b in initialize.getRandomList():
						listOfBirds[ct]=b
						ct+=1
				if event.key == pygame.K_p: #get physical parameters
					for b in copyListOfBirds:
						force.append(physics.force(hp.mass,[x*b.speed for x in b.direction],b.prevVelocity,hp.deltaT))
						angularmomentum.append(physics.angularMomentum(hp.mass,b.position,[x*b.speed for x in b.direction]))
						power.append(physics.power(force[-1],[x*b.speed for x in b.direction]))
					print force[0]
					print power[0]
					print angularmomentum[0]
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
		time1 = time.time()*1000
		time2 = time.time()*1000
		# print time2-time1
		# copyListOfBirds = initialize.getRandomList()
		time1 = time.time()*1000
		for r in copyListOfBirds:
			head = r.position
			tailCentre = (r.position[0]-12*r.direction[0],r.position[1]-12*r.direction[1],r.position[2]-12*r.direction[2])
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

			tailSq1 = (tailCentre[0]-4*tmpDir1[0],tailCentre[1]-4*tmpDir1[1],tailCentre[2]-4*tmpDir1[2])
			tailSq2 = (tailCentre[0]+4*tmpDir1[0],tailCentre[1]+4*tmpDir1[1],tailCentre[2]+4*tmpDir1[2])  
			# tailSq3 = (tailCentre[0]-8*tmpDir2[0],tailCentre[1]-8*tmpDir2[1],tailCentre[2]-8*tmpDir2[2])
			# tailSq4 = (tailCentre[0]+8*tmpDir2[0],tailCentre[1]+8*tmpDir2[1],tailCentre[2]+8*tmpDir2[2])
			
			if r.pred==-1:
				glBegin(GL_TRIANGLES)
				glColor3fv((0,0,0))
				glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
				glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
				glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
				glEnd()
			else:
				glBegin(GL_TRIANGLES)
				glColor3fv((0.5,0.5,0.5))
				glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
				glVertex3fv((int(tailSq1[0]),int(tailSq1[1]),int(tailSq1[2])))
				glVertex3fv((int(tailSq2[0]),int(tailSq2[1]),int(tailSq2[2])))
				glEnd()
			
		pygame.display.flip()
		time2 = time.time()*1000
		# print time2-time1
		clock.tick(hp.fps)
		# ch=input()

gluPerspective(45.0,(hp.window_width/hp.window_height),1,10000.0)

#moving back
glTranslatef(0,0,-2000.0)

clock = pygame.time.Clock()

#rendering process

# p2.join()
def updateBirds(listOfBirds,neighbours_R,neighbours_r):
	while True:
		# print os.getpid()
		# print "updateBirds"
		force=[]
		angularmomentum=[]
		power=[]
		copyNeighbours_R = list(neighbours_R)
		copyNeighbours_r = list(neighbours_r)
		copyListOfBirds=list(listOfBirds)
		i=0
		for	b in copyListOfBirds:
			if b.pred==-1:
				continue
			b.update(copyNeighbours_R[b.index],copyNeighbours_r[b.index])
			listOfBirds[i]=b
			i+=1
		# pipeConnection.send(listOfBirds)
			# force.append(physics.force(hp.mass,[x*b.speed for x in b.direction],[x*copyListOfBirds[b.index].speed for x in copyListOfBirds[b.index].direction],hp.deltaT))
			# angularmomentum.append(physics.angularMomentum(hp.mass,b.position,[x*b.speed for x in b.direction]))
			# power.append(physics.power(force[-1],[x*b.speed for x in b.direction]))
		# print listOfBirds[0]
		# print "---Force---"
		# print force
		# print "---angularmomentum---"
		# print angularmomentum
		# print "---Power---"
		# print power
		
def updateNeighbours(listOfBirds,neighbours_R,neighbours_r):
	while True:
		# print "updateNeighbours"
		copyListOfBirds=list(listOfBirds)
		for ind in range(hp.numberOfBirds):
			# print ind
			atmp=[]
			btmp=[]
			for b in copyListOfBirds:
				if b.index==ind or(b.position[0]==copyListOfBirds[ind].position[0] and b.position[1]==copyListOfBirds[ind].position[1] and b.position[2]==copyListOfBirds[ind].position[2]):
					continue
				if(math.sqrt((copyListOfBirds[ind].position[0]-b.position[0])**2+(copyListOfBirds[ind].position[1]-b.position[1])**2+(copyListOfBirds[ind].position[2]-b.position[2])**2)<hp.r):
					btmp.append(b)
				if(math.sqrt((copyListOfBirds[ind].position[0]-b.position[0])**2+(copyListOfBirds[ind].position[1]-b.position[1])**2+(copyListOfBirds[ind].position[2]-b.position[2])**2)<hp.R):
					atmp.append(b)
			neighbours_R[ind]=atmp
			neighbours_r[ind]=btmp

if __name__ == '__main__':
	# multiprocessing.log_to_stderr(logging.DEBUG)
	neighbours_R=manager.list()
	neighbours_r=manager.list()
	for i in range(hp.numberOfBirds):
		neighbours_R.append([])
		neighbours_r.append([])
	# birdGet, birdPut = multiprocessing.Pipe()
	p1 = multiprocessing.Process(target=updateBirds,args=(listOfBirds,neighbours_R,neighbours_r,))
	p2 = multiprocessing.Process(target=drawbirds,args=(listOfBirds,))
	p3 = multiprocessing.Process(target=updateNeighbours,args=(listOfBirds,neighbours_R,neighbours_r))


	p3.start()
	p2.start()
	p1.start()

	p3.join()
	p2.join()
	p1.join()