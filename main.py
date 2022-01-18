import pygame
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

BK_COLOR = (68,132,88)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

bk_image = pygame.image.load("background.jpg")

clock = pygame.time.Clock()

circle_x=10
circle_y=WINDOW_H/2
x_step=10

play = True
while play:
  # screen.fill(BK_COLOR)
   screen.blit(bk_image,(0,0))
   # for i in range():

   pygame.draw.circle(screen,(0,0,0),(circle_x,circle_y), 30)
   circle_x +=x_step
   if circle_x>WINDOW_W:
      x_step =-10
   elif circle_x<0:
      x_step=10


   pygame.display.flip()


   for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
   clock.tick(50)


# for i in range():
#   pygame.draw.line(screen,(204,154,255),[100,80],[400,80], 10)
#   pygame.draw.line(screen,(204,154,255),[100,80],[100,250], 10)
#   pygame.draw.line(screen,(204,154,255),[100,250],[400,250],10)
#   pygame.draw.line(screen,(204,154,255),[400,80],[400,250], 10)
#   pygame.display.flip()
#   print (i)

pygame.quit()


   #   pygame.draw.line(screen,(0,0,0),[0,i],[WINDOW_W,i], 10)
#   for i in range(0,WINDOW_W,30):
#      pygame.draw.circle(screen,(0,0,0),[WINDOW_W,i], 30)
   #   pygame.draw.line(screen,(0,0,0),[i,0],[i,WINDOW_H], 10)
#   pygame.display.flip()