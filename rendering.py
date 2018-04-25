import pygame
import hyperparameters as hp
import math

pygame.init()

mainDisplay = pygame.display.set_mode((hp.window_width,hp.window_height))
pygame.display.set_caption('Starlings')
mainDisplay.fill(hp.colorwhite)
pygame.display.update()
clock = pygame.time.Clock()

def drawbird(r):
	r_xy=[int(r[0]),int(r[1])]
	depthColor = (0,0,int(r[2])*255/(hp.z_max-hp.boundaryThreshold))
	pygame.draw.circle(mainDisplay,depthColor,r_xy,5)
	pygame.draw.circle(mainDisplay,hp.colorgreen,r_xy,hp.R,3)
	pygame.draw.circle(mainDisplay,hp.colorred,r_xy,hp.r,3)


def updateDisplay():
	pygame.display.update()
