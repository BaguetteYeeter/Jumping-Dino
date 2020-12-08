import pygame
#import the pygame library

#--------------VARIABLES----------------
x = 32
#x of the player
y = 398
#y of the player
height = 50
#height of the player
width = 50
#width of the player
vel = 5
#idk velocity maybe?

pygame.init()
#initialize pygame
mainScreen = pygame.display.set_mode((640, 480))
#set display resolution

pygame.display.set_caption("Jumping Dino")
#change the title

run = True
#should the loop run?

while run:
    pygame.time.delay(100)
    #set the delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #close the program if the window closes

    mainScreen.fill((0,0,0))
    #fill the screen

    pygame.draw.rect(mainScreen, (255,0,0), (x, y, width, height))
    #draw the player

    pygame.display.update()
    #update the display
pygame.quit()
#quit pygame
