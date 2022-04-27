import pygame 
import time

# screen size 
WINDOW_W = 1000 #הגדרת רוחב מסך
WINDOW_H = 600 #הגדרת גובה מסך
WINDOW_SIZE = (WINDOW_W, WINDOW_H) #טאפל של גודל המסך

pygame.init() #התחלה
screen = pygame.display.set_mode(WINDOW_SIZE) #הצגת המסך שהגדרנו
pygame.display.set_caption("My First Game ") #הצגת כותרת המשחק

bk_image = pygame.image.load("background.jpg") #העלאת הרקע ושמירה במשתנה
ship_image = pygame.image.load("ship.png") #העלאת החללית ושמירה במשתנה
ship_image = pygame.transform.scale(ship_image,(75,150))  #שמירת החללית בגודל הרצוי
laser_image = pygame.image.load("laser2.png") #העלאת הלייזר ושמירה במשתנה
laser_image = pygame.transform.scale(laser_image, (10, 20)) #שמירת הלייזר בגודל הרצוי

SOUND1= "piu.mp3" #שמירת הסאונד במשתנה
SOUND2= "sound.org.mp3" #שמירת הסאונד במשתנה
pygame.mixer.init() #התחלת סאונד
pygame.mixer.music.load(SOUND2) #העלאה של הסאונד
pygame.mixer.Channel(0).play(pygame.mixer.Sound(SOUND2))
pygame.mixer.music.load(SOUND1) #העלאה של הסאונד
# pygame.mixer.Channel(1).play(pygame.mixer.Sound(SOUND1))

pygame.mixer.music.play()


clock = pygame.time.Clock() #הגדרת שעון  

def is_laser_hit(laser_pos):
  return abs(laser_pos[0]-circle_x) <30 and abs(laser_pos[1]-circle_y) <30  
    


laser_list = []
def print_lasers():
   for i in range(len(laser_list)):
      l = laser_list[i]
      screen.blit(laser_image,(l[0],l[1]))
      laser_list[i] = [l[0],l[1]-10]
      if is_laser_hit(l): 
         return True
    
 # remove lazer that our outside of the window
   if len(laser_list) > 0 and laser_list[0][1] < 0:
      laser_list.remove(laser_list[0])

pygame.font.init() 

counter= 0
circle_x = 10 #ציר האיקס של הכדור
circle_y = 50 #ציר וואי של הכדור
x_step = 10 #צעדים בציר האיקס של הכדור
ship_x = WINDOW_W / 2 #ציר האיקס של החללית (רוחב המסך/ 2)
ship_y = WINDOW_H - 150 #ציר הווי של החללית (גובה המסך - גובה החללית)
laser_x= -100  #הגדרת ציר האיקס של הלייזר כך שלא יראו אותו
laser_y= -100  #הגדרת ציר האיקס של הלייזר כך שלא יראו אותו

play = True

hold= 0

while play:
   #ציור עיגול (מסך, צבע לבן, מיקום שהגדרנו, רדיוס)
   pygame.draw.circle(screen,(0,0,0),(circle_x,circle_y), 30) 
   pygame.display.flip() #הצגת הכדור על המסך
   circle_x +=x_step #הגדלת ציר האיקס של הכדור כדי שיזוז לפי הצעדים שהגדרנו
   if circle_x>WINDOW_W: #אם ציר האיקס של הכדור גדול מרוחב המסך
      circle_y += 60
      x_step =-10 #הקטנת ציר האיקס של הכדור כל פעם ב10
   elif circle_x<0: #אם ציר האיקס של הכדור קטן מ0
      circle_y += 60
      x_step=10 #הגדלת ציר האיקס של הכדור כל פעם ב10
   if circle_y > ship_y :
      play=False
      red = (150, 0, 0) 
      font = pygame.font.SysFont(None, 50)
      img = font.render('you loser', True, red)
      screen.blit(img, (20, 20))
   for event in pygame.event.get(): #לולאה של כל האירועים שיכולים לקרות על המסך
      if event.type == pygame.QUIT: #אם סוג האירוע הוא לחיצה על יציאה
         play=False #שינוי המשתנה לשקר ויציאה מהלולאה כך שהתוכנית תיסגר
      elif event.type == pygame.KEYDOWN: #אם סוג האירוע הוא לחיצה על מקש
         if event.key == pygame.K_LEFT:  #אם הלחיצה היא על המקש שמאלה
            # ship_x -= 10 #ציר האיקס של החללית יקטן ב10
            hold= -1
         if event.key == pygame.K_RIGHT: #אם הלחיצה היא על המקש ימינה
            # ship_x += 10 #ציר האיקס של החללית יגדל ב10
            hold= 1
      elif event.type == pygame.KEYUP:
         hold= 0
         if event.key == pygame.K_SPACE: #אם הלחיצה היא על מקש הרווח
            laser_list.append([ship_x+30,ship_y])
            laser_list.append([ship_x+30,ship_y-20])
            pygame.mixer.music.play()
   screen.blit(bk_image,(0,0)) #הצגת הרקע
            
   ship_x += hold * 10         
            

   
   screen.blit(ship_image,(ship_x,ship_y)) #הצגת החללית במיקום שהגדרנו

   if print_lasers():
      circle_x= 10
      pygame.mixer.Channel(1).play(pygame.mixer.Sound(SOUND1))
      counter+=10


   red = (150, 0, 0)
   font = pygame.font.SysFont(None, 50)
   img = font.render('score: '+ str(counter), True, red)
   screen.blit(img, (20, 20))

   clock.tick(50) #קצב החזרה של הלולאה

pygame.quit()