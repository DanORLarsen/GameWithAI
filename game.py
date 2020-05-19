import pygame as pygame
##Inspiried by https://nerdparadise.com/programming/pygame

#Variables
width = 1200
height = 800
size = [width, height]
deaths = 0
playerx = 30
playery = 30
enemyx = 400
enemyy = 500
goal = 1000
done = False
win = False
speed = 3
enemyMvoingUp = True

pygame.init()
screen = pygame.display.set_mode((size))
myfont = pygame.font.SysFont("monospace", 16)
myWinFont = pygame.font.SysFont("monospace", 45)
WHITE = (255,255,255)
clock = pygame.time.Clock()
pygame.display.set_caption('Game with AI')



#Metgods
def die():
    print("DEAD - Respawning")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        ##TODO: Make this into a class for player, also same with enemy        
        pressed = pygame.key.get_pressed()
        if (not win): 
            if pressed[pygame.K_UP]: 
                playery -= speed
                
            if pressed[pygame.K_DOWN]: 
                playery += speed

            if pressed[pygame.K_LEFT]: 
                playerx -= speed

            if pressed[pygame.K_RIGHT]: 
                playerx += speed
        
        #ENEMY MOVEMENT
        if(enemyMvoingUp):
            enemyy -= 3
        if(enemyy <= 20):
            enemyMvoingUp = False
        if(not enemyMvoingUp):
            enemyy += 3
        if(enemyy >= 720):
            enemyMvoingUp = True

       
        screen.fill((220, 220, 220))
        color = (0, 128, 255)
        
##GRAPHIC + Collition Logic

        #Goal
        goalWall = pygame.draw.rect(screen, (0,255,0), pygame.Rect(goal + 50, 0, 500, height))
        pygame.draw.line(screen, (0,255,0), (goal+100,0), (goal+100,height), 200)
        

        #Obstacles
        #Boarder walls
        wall1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, width, 10))
        wall2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, height-10, width, 10))
        wall3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 10, height))
        wall4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(width-10, 0, 10, height))

        #Before middle
        wall5 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 120, 200, 10))
        wall6 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(200, 120, 10, 100))
        wall7 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(100, 300, 275, 10))
        wall8 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 380, 275, 10))
        wall9 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 600, 370, 10))

        #Middle pillars
        wall10 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(370, 0, 10, 520))
        wall11 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(370, 600, 10, 200))
        wall12 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(470, 250, 10, 600))
        wall13 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(470, 0, 10, 175))

        ##TODO: Create score that counts down along with time = faster = higher score
        #Deaths
        deathtext = myfont.render("Deaths {0}".format(deaths), 1, (0,0,0))
        screen.blit(deathtext, (12, 10))
        if (win):
            winText = myWinFont.render("YOU WON", 1, (0,0,0))
            screen.blit(winText, (500, 350))
        
        #Enemies
        enemy = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyx, enemyy, 50, 50))
            #Collide with this enemy

       #Player
        player = pygame.draw.rect(screen, color, pygame.Rect(playerx, playery, 40, 40))
        #Collide wall logic
        ##TODO: Make this into method - Or find a way to use collide list
        if (player.colliderect(wall1)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall2)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall3)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall4)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall5)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall6)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall7)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall8)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall9)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall10)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall11)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall12)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(wall13)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(enemy)):
            die()
            deaths += 1
            playerx = 30
            playery = 30
            enemyx = 400
            enemyy = 500
        if (player.colliderect(goalWall)):
            win = True
        pygame.display.flip()
        clock.tick(60)
        pygame.display.flip()