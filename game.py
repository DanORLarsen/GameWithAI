import pygame as pygame
import neat
##Inspiried by https://nerdparadise.com/programming/pygame


class Player(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colidePoints = []
        self.alive = True
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (self.x, self.y, 40, 40))

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)
    def createCollisionWith(self, something):#WORKS
        return self.rect.colliderect(something)
    
    def die(self):
        self.alive = False

    def isAlive(self):
        return self.alive

    def get_data(self):
        

#Creates collision and stores points for AI
    def createCollisionWithMore(self, list):#WORKS
        for each in list:
            self.colidePoints.append(each)
            if(self.rect.colliderect(each)):
                return True
    
    def get_reward(self):
        return self.x


#Variables
width = 1200
height = 800
size = [width, height]
deaths = 0
playerx = 30
playery = 30
enemyX = 400
enemyY = 500
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

def start(genomes, config):

    #Variables
    width = 1200
    height = 800
    size = [width, height]
    deaths = 0
    playerx = 30
    playery = 30
    enemyX = 400
    enemyY = 500
    goal = 1000
    done = False
    win = False
    speed = 3
    enemyMvoingUp = True


    # NEAT
    nets = []
    rect = []
    player1 = Player(playerx, playery)
    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        
        rect.append(player1)
    
        


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
                enemyY -= 3
            if(enemyY <= 20):
                enemyMvoingUp = False
            if(not enemyMvoingUp):
                enemyY += 3
            if(enemyY >= 720):
                enemyMvoingUp = True

        
            screen.fill((220, 220, 220))
            color = (0, 128, 255)
            




    ##GRAPHIC + Collition Logic

            hostileList = []
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
            hostileList.append(wall1)
            hostileList.append(wall2)
            hostileList.append(wall3)
            hostileList.append(wall4)
            hostileList.append(wall5)
            hostileList.append(wall6)
            hostileList.append(wall7)
            hostileList.append(wall8)
            hostileList.append(wall9)
            hostileList.append(wall10)
            hostileList.append(wall11)
            hostileList.append(wall12)
            hostileList.append(wall13)
            

            ##TODO: Create score that counts down along with time = faster = higher score
            #Deaths
            deathtext = myfont.render("Deaths {0}".format(deaths), 1, (0,0,0))
            screen.blit(deathtext, (12, 10))
            if (win):
                winText = myWinFont.render("YOU WON", 1, (0,0,0))
                screen.blit(winText, (500, 350))
            
            #Enemies
            enemy = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX, enemyY, 50, 50))
                #Collide with this enemy
            hostileList.append(enemy)
            print(enemy.top)
        #Player
            #player = pygame.draw.rect(screen, color, pygame.Rect(playerx, playery, 40, 40))
            
            #Collide wall logic
            ##TODO: Make this into method - Or find a way to use collide list
            
            if(player1.createCollisionWithMore(hostileList)):
                print("This works!")
                player1.die()
                break
            if (player1.createCollisionWith(goalWall)):
                win = True
            player1.draw(screen)
            
            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    # Set configuration file
    config_path = './config-feedforward.txt'
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(start, 1)