import pygame
import random,time
pygame.init()


#Загружаю все картинки и создаю нужные переменные
screen = pygame.display.set_mode((800, 600))

backgroundImage = pygame.image.load("week9/back.jpg")
playerImage = pygame.image.load("week9/player.png")
player_x = 200
player_y = 536

enemyImage = pygame.image.load("week9/enemy.png")
enemy_x = [random.randint(0, 736)]
enemy_y = [random.randint(20, 50)]

bullshitImage = pygame.image.load("week9/bullshit.jpg")
bullshit_x = [200]
bullshit_y = [436]

enemy_dx = [3]     #Скорость врага по х и у
enemy_dy = 30

def score_text():
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Score: "+str(score), 1, (180, 180, 0))
    screen.blit(text1, (650, 10))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullshit(x, y):
    screen.blit(bullshitImage, (x, y))

f=[False]
i=0
g=1
score=0


#GAME loop
done = False
while not done:
    f1 = pygame.font.Font(None, 36)


    #Все команды на нажатия
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT : 
            done = True
        if  pressed[pygame.K_SPACE]:
            bullshit_x[i]= player_x
            bullshit_x.append(player_x)
            bullshit_y[i]=536
            bullshit_y.append(536)
            f[i]=True           
            f.append(False)
            i+=1
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: player_x -= 3
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: player_x += 3
    
    
        if pressed[pygame.K_ESCAPE]:
            done = True
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: player_x -= 3
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: player_x += 3

    #Геометрия
    for k in range (0,g):
        enemy_x[k] += enemy_dx[k]
        enemy_dx.append(3)
        if enemy_x[k] < 0 or enemy_x[k] > 736:
            enemy_dx[k] = -enemy_dx[k]
            enemy_y[k] += enemy_dy
        if player_x < 0:
            player_x += 3
        if player_x >736:
            player_x -= 3

        if enemy_y[k]>550:
            enemy_y[k]=False
            

    #Вывод на экран
    screen.blit(backgroundImage, (0, 0)) 
    player(player_x, player_y)
    for k in range (0,g):
        if enemy_y[k]:
            enemy(enemy_x[k], enemy_y[k])    
    score_text()
    for j in range (0,i):
        if f[j]:
            if bullshit_y[j]<0:
                f[j]=False
            bullshit_y[j] -= 1
            for k in range(0,g):
                if (enemy_x[k] + 50 >= bullshit_x[j]>=enemy_x[k]-50) and (enemy_y[k] + 50 >= bullshit_y[j]>=enemy_y[k]):
                    if score<5:
                        enemy_y[k] = False
                        #enemy_y[k] = random.randint(20, 5)
                        enemy_y.append(random.randint(0, 100))
                        enemy_x.append(random.randint(0, 736))
                        g+=1
                    else: 
                        numm=score//50
                        enemy_y[k]=False
                        for y in range (0,numm):
                            #enemy_x[k] = random.randint(0, 736)
                            #enemy_y[k] = random.randint(20, 50)
                            enemy_y.append(random.randint(0, 100))
                            enemy_x.append(random.randint(0, 736))
                            g+=1
                    score+=1
                    f[j]=False

                bullshit(bullshit_x[j]+8, bullshit_y[j])
                bullshit(bullshit_x[j]+52, bullshit_y[j])

    for k in range(0,g):
        if (player_x + 50 >=enemy_x[k]>=player_x-50)and(enemy_y[k]>=486):
          pygame.quit()

    pygame.display.flip()
