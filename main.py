import pygame
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

BK_COLOR = (68,132,88)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game ")

bk_image = pygame.image.load("background.jpg")
ship_image = pygame.image.load("ship.png")
ship_image = pygame.transform.scale(ship_image,(75,150))
clock = pygame.time.Clock()

circle_x=10
circle_y=WINDOW_H/2
x_step=10

play = True
ship_x= WINDOW_W/2
ship_y= WINDOW_H-150

while play:
  # screen.fill(BK_COLOR)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         play=False
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            ship_x -= 10
         if event.key == pygame.K_RIGHT:
            ship_x += 10

   screen.blit(bk_image,(0,0))
   screen.blit(ship_image,(ship_x,ship_y))


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