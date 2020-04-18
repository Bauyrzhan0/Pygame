import pygame
import random
import time
from enum import Enum

pygame.init()
width=800
height=600
screen = pygame.display.set_mode((width, height))
wallImage=pygame.image.load('wall.jpg')
wall_range=20


pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

pulyaSound=pygame.mixer.Sound('pulya.wav')
vzryvSound=pygame.mixer.Sound('vzryv.wav')

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:

    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN,d_pull=pygame.K_KP0):
        self.x = x
        self.y = y
        self.score=3
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction.RIGHT

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

        self.KEYPULL=d_pull

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (
            self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)


    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.draw()
    
class Pulya:
    def __init__(self,x=0,y=0,color=(0,0,0),direction=Direction.LEFT,speed=7):
        self.x=x
        self.y=y
        self.color=color
        self.speed=speed
        self.direction=direction
        self.status=True
        self.distance=0
        self.radius=10

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.distance+=1
        if self.distance>(2*width):
            self.status=False
        self.draw()

    def draw(self):
        if self.status:
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

def give_coordinates(tank):
    if tank.direction == Direction.RIGHT:
        x=tank.x + tank.width + int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.LEFT:
        x=tank.x - int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.UP:
        x=tank.x + int(tank.width / 2)
        y=tank.y - int(tank.width / 2)

    if tank.direction == Direction.DOWN:
        x=tank.x + int(tank.width / 2)
        y=tank.y + tank.width + int(tank.width / 2)

    p=Pulya(x,y,tank.color,tank.direction)
    pulya.append(p)

def collision():
    #столкновение танка со стенкой
    for tank in tanks:
        if (tank.x<-41):
            tank.x=width
        elif tank.x>width:
            tank.x=-40
        if (tank.y<-41):
            tank.y=height
        elif tank.y>height:
            tank.y=-40

    #столкновение пули с танком
    for p in pulya:
        for tank in tanks:
            if (tank.x+tank.width+p.radius > p.x > tank.x - p.radius ) and ((tank.y+tank.width + p.radius > p.y > tank.y - p.radius)) and p.status==True:
                vzryvSound.play()
                p.color=(0,0,0)
                tank.score-=1
                p.status=False
                
                tank.x=random.randint(50,width-70)
                tank.y=random.randint(50,height-70)

    #выход пули  с другой стороны
    for p in pulya:
        if p.x<0:
            p.x=width
        if p.x>width:
            p.x=0
        if p.y>height:
            p.y=0
        if p.y<0:
            p.y=height

def score():
    font = pygame.font.SysFont('Arial', 32) 
    score1=tanks[0].score
    score2=tanks[1].score
    res = font.render(str(score1), True, (255, 123, 100))
    res1 = font.render(str(score2), True, (100, 230, 40))
    screen.blit(res, (30,30))
    screen.blit(res1, (750,30))
    if score1==0 or score==0:
        res = font.render('Game Over',True, (255, 123, 0))
        res1 = font.render(str(score1), True, (255, 123, 100))
        res2 = font.render(str(score2), True, (100, 230, 40))
        screen.fill((0, 0, 0))
        screen.blit(res, (350,250))
        screen.blit(res1, (370,280))
        screen.blit(res2, (390,280))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()



'''def quit():
    score1=tanks[1].score
    score2=tanks[0].score
    screen.fill((210, 160, 190))
    res = font.render('G A M E   O V E R!', True, (0, 90, 255))
    res1 = font.render('total score of GREEN player: ' + str(score1), True, (0, 90, 255))
    res2 = font.render('total score of PINK player: ' + str(score2), True, (0, 90, 255))
    screen.blit(res, (150,150))
    screen.blit(res1, (200,250))
    screen.blit(res2, (200,300))
    time.sleep(3)
    pygame.quit()'''

def fill_edges():
    for i in range(width//wall_range):
        screen.blit(wallImage,(wall_range*i,0))
        screen.blit(wallImage,(wall_range*i,height-wall_range))

    for i in range(height//wall_range):
        screen.blit(wallImage,(0,i*wall_range))
        screen.blit(wallImage,(width-wall_range,i*wall_range))

mainloop = True
tank1 = Tank(300, 300, 3, (255, 123, 100),d_pull=pygame.K_KP_ENTER)
tank2 = Tank(100, 100, 3, (100, 230, 40), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s,pygame.K_SPACE)

pulya1=Pulya()
pulya2=Pulya()

tanks = [tank1, tank2]
pulya = [pulya1,pulya2]

FPS = 30

clock = pygame.time.Clock()

while mainloop:
    mill = clock.tick(FPS)
    screen.fill((0, 0, 0))
    fill_edges()
    score()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                quit()
            pressed = pygame.key.get_pressed()
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
                
                if pressed[tank.KEYPULL]:
                    pulyaSound.play()
                    give_coordinates(tank)
    for tank in tanks:                   
        tank.move()
    collision()

    for p in pulya:
        p.move()
    
    for tank in tanks:
        tank.draw() 
    fill_edges()
    pygame.display.flip()

pygame.quit()
