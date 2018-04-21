import pygame
import hyperparameters as hp

pygame.init()

mainDisplay = pygame.display.set_mode((hp.window_width,hp.window_height))
pygame.display.set_caption('Starlings')
mainDisplay.fill(hp.colorwhite)
pygame.display.update()
clock = pygame.time.Clock()

def drawbird(r):
	r=[int(r[0]),int(r[1])]
	pygame.draw.circle(mainDisplay,hp.colorblack,r,3)
	pygame.draw.circle(mainDisplay,hp.colorgreen,r,hp.R,3)
	pygame.draw.circle(mainDisplay,hp.colorred,r,hp.r,3)


def updateDisplay():
	pygame.display.update()
