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
laser_image = pygame.image.load("laser2.png")
laser_image = pygame.transform.scale(laser_image, (10, 20))


SOUND1= "piu.mp3"
SOUND2= "sound.org.mp3"
pygame.mixer.init()
pygame.mixer.music.load(SOUND2)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(SOUND2))
pygame.mixer.music.load(SOUND1)
pygame.mixer.Channel(1).play(pygame.mixer.Sound(SOUND1))

pygame.mixer.music.play()


clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
ship_x = WINDOW_W /2
ship_y = WINDOW_H - 150

circle_x_step = 10
x_step = 10
laser_list = []



play = True



def print_lasers():
  for i in range(len(laser_list)):
    l = laser_list[i]
    screen.blit(laser_image,(l[0],l[1]))
    laser_list[i] = [l[0],l[1]-10]

  if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])

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
         if event.key == pygame.K_SPACE:
            laser_list.append([ship_x+30,ship_y])
            laser_list.append([ship_x+30,ship_y-20])
            pygame.mixer.music.play()
            

   screen.blit(bk_image,(0,0))
   screen.blit(ship_image,(ship_x,ship_y))
   print_lasers()

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