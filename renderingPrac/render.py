import pygame
pygame.init()

white = (255,255,255) #define some colors
black = (0,0,0)
red = (255,0,0)

#returns a pygame surface
gameDisplay = pygame.display.set_mode((800,600))
#sets the title
pygame.display.set_caption('Starlings')
#updates the changes to the screen
pygame.display.update()
gameExit = False

#DEFINING FRAMES PER SECOND
clock = pygame.time.Clock()

#display message on screen
font = pygame.font.SysFont(None,25)
def message_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text,[300,400])
#main loop
while not gameExit:
	for event in pygame.event.get():
		# print (event)
		#quitting the game
		if event.type == pygame.QUIT:
			gameExit = True
	#fill the screen with this color
	gameDisplay.fill(white)
	#draw a rectange x,y,width,height | 2 methods
	pygame.draw.rect(gameDisplay,black,[400,300,200,100])
	gameDisplay.fill(red,rect=[200,200,50,50])
	message_to_screen("welcome",black)
	
	pygame.display.update()

	#30 fps, does a sleep kind of thing
	clock.tick(30)
pygame.quit()
quit()