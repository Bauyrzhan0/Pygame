import pygame
import random
import time

pygame.init()
font = pygame.font.Font(None, 36)
width=800
height=600
screen = pygame.display.set_mode((width, height))
fruit=pygame.image.load('apple.png')


class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5  # right
        self.dy = 0
        self.d=5
        self.is_add = False
        self.score=0

    def draw(self):
        for i in range(len(self.elements)):
            pygame.draw.circle(screen, (255, 0, 0), self.elements[i], self.radius)

    def add_to_snake(self):
        self.size += 1
        for i in range (5):
            self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x=random.randint(75,700)
        self.y=random.randint(75,500)
        self.onscreen=True

    def draw(self):    
        screen.blit(fruit, (self.x,self.y))


def collision():
    if (food.x in range(snake.elements[0][0] - 28, snake.elements[0][0])) and  (food.y  in range(snake.elements[0][1] - 28, snake.elements[0][1])) :
        snake.is_add = True 
        if snake.is_add == True:
            food.x = random.randint(50, width - 50)
            food.y = random.randint(50, height - 50)
            snake.d+=1
            snake.score+=1
            
    if  (770<=snake.elements[0][0]or snake.elements[0][0]<=30) or (570<=snake.elements[0][1]or snake.elements[0][1]<=30):
        game_over()

def game_over():
    
    screen.fill((0, 255, 127))
    res = font.render('G A M E   O V E R!', True, (0, 90, 255))
    res1 = font.render('total score: ' + str(snake.score), True, (0, 90, 255))
    screen.blit(res, (250,150))
    screen.blit(res1, (270,250))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    

snake = Snake()
food=Food()
running = True

FPS = 30

clock = pygame.time.Clock()

k1_pressed = False
cnt=0
while running:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = snake.d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -snake.d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -snake.d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = snake.d

    collision()
    screen.fill((3,192,60))
    wallsurface=pygame.draw.rect(screen,(11,255,81),(0,0,800,600),50)
    snake.move()
    snake.draw()
    food.draw()
    res2 = font.render('score: ' + str(snake.score), True, (0, 90, 255))
    screen.blit(res2,(700,0))


    pygame.display.flip()
