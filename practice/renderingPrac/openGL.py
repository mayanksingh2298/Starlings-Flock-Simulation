import pygame
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1),
	)
edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
	)

def Draw_Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glColor4f(0,0,0,0)   
			glVertex3fv(vertices[vertex])
	glEnd()

def displayPoints():
	points=[(0.5,0.5,0.5),(0.5,0.5,0.75),(0.5,0.75,0.65),(-0.5,-0.5,-0.5),(-0.5,-0.5,-0.75),(-0.5,-0.75,-0.65)]
	glBegin(GL_TRIANGLES)
	for point in points:
		glColor4f(0,0,0,0)   
		glVertex3fv(point)
	glEnd()


def main():
	pygame.init()
	display = (800,400)
	
	mainDisplay = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	
	gluPerspective(45.0,(display[0]/display[1]),1,50.0)

	#moving back
	glTranslatef(0.0,0.0,-5.0)

	# where we might be
	glRotatef(0,0,0,0)
	rotateX=0
	rotateY=0
	rotateZ=0

	while True:
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				print  event
				print event.button
				if event.button ==4:
					glTranslatef(0.0,0.0,1.0)
				elif event.button ==5:
					glTranslatef(0.0,0.0,-1.0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

				if event.key == pygame.K_w:
					rotateX = 1
				if event.key == pygame.K_s:
					rotateX = -1
				if event.key == pygame.K_a:
					rotateY = 1
				if event.key == pygame.K_d:
					rotateY = -1
				if event.key == pygame.K_q:
					rotateZ = 1
				if event.key == pygame.K_e:
					rotateZ = -1
				
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
		displayPoints()
		pygame.display.flip()
		pygame.time.wait(10)
main()