import pygame
import neat
import os
##Inspiried by https://nerdparadise.com/programming/pygame and https://www.youtube.com/watch?v=wQWWzBHUJWM&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=6

class Player(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.speed = 3
        self.goalHit = ""
        self.number = 0
        self.distance = []
        self.colidePoints = []
        self.milestonePoints = []
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (self.x, self.y, 40, 40))

    def moveSet(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            self.rect.y -= self.speed

        if pressed[pygame.K_DOWN]: 
            self.rect.y += self.speed

        if pressed[pygame.K_LEFT]: 
            self.rect.x -= self.speed

        if pressed[pygame.K_RIGHT]: 
            self.rect.x += self.speed


    def getGoal(self, something):
        self.goalHit = something.left

    def printPoints(self):
        print(self.colidePoints)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)
        
    def createCollisionWith(self, something):#WORKS
        self.goalRect = something.left
        return self.rect.colliderect(something)

    def increaseMilestomeNumber(self):
        self.number += 1


    def milestoleCollisionMore(self, list):
        for each in list:
            if(self.rect.colliderect(each)):
                return True
    
    def getNextMilestone(self):
        return self.milestonePoints[self.number]

    def getMilestones(self, list):
        for each in list:
            self.milestonePoints.append(each)

    def createCollisionWithMore(self, list):#WORKS
        for each in list:
            if(self.rect.colliderect(each)):
                return True
    def getColidePoints(self, list):
        for each in list:
            self.colidePoints.append(each)

    
    

    pygame.init()
    
def start(genomes, config):
    
#Variables
    width = 1200
    height = 800
    size = [width, height]
    screen = pygame.display.set_mode((size))
    myfont = pygame.font.SysFont("monospace", 16)
    myWinFont = pygame.font.SysFont("monospace", 45)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Game with AI')

    deaths = 0
    enemyX = 400
    enemyY = 500
    goal = 1000
    global done
    done = False
    win = False
    speed = 3
    enemyMvoingUp = True
    i = 0

    
    #NEAT - TODO: CREATE SO THEY CAN FIND THE Milestones (Use center)

    nets = []
    ge = []
    players = []
    
    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        players.append(Player(30,30, screen))
        ge.append(genome)

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
            ##TODO: Make this into a class for player, also same with enemy        
        

            for x, player in enumerate(players):
                player.moveSet()
                ge[x].fitness += 0.01
                if(i == 1):
                    output = nets[x].activate((player.x, player.y))

                    output
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
            friendlyList = []
            #Goal
            goalWall = pygame.draw.rect(screen, (0,255,0), pygame.Rect(goal + 50, 0, 500, height))
            pygame.draw.line(screen, (0,255,0), (goal+100,0), (goal+100,height), 200)

            milestoneColor = (220,220,220)
            #Milesstones for AI (Reinforcement + Survival of the fittest)
            milestone1 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(210, 120, 160, 10))
            milestone2 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(200, 220, 10, 80))
            milestone3 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(10, 300, 90, 10))
            milestone4 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(275, 380, 95, 10))
            milestone5 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(370, 520, 10, 80))
            milestone6 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(470, 170, 10, 80))
            friendlyList.append(milestone1)
            friendlyList.append(milestone2)
            friendlyList.append(milestone3)
            friendlyList.append(milestone4)
            friendlyList.append(milestone5)
            friendlyList.append(milestone6)


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
            
            for x, player in enumerate(players):
                #Collide wall logic + more
                if(player.number <= 5):
                    if(player.rect.colliderect(friendlyList[player.number])):
                        ge[x].fitness += 10
                        print(ge[x].fitness)
                        player.increaseMilestomeNumber()

                if(player.createCollisionWithMore(hostileList)):
                    ge[x].fitness -= 1
                    nets.pop(players.index(player))
                    ge.pop(players.index(player))
                    players.pop(players.index(player))
                    deaths += 1
                    enemyX = 400
                    enemyY = 500
                    if (deaths == 20): #Number of AI players per generation (So if all are dead = new Generation)
                        done = True
                if (player.createCollisionWith(goalWall)):
                    ge[x].fitness = 2000
                    done = True
                player.draw(screen)
                #To give the AI the goal
                player.getGoal(goalWall)

                #Simple solution to adding milestones to AI.
                
                if (i == 0):
                    player.getMilestones(friendlyList)
                    i+=1
                    

            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)
            pygame.display.flip()



def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    
    p = neat.Population(config)


    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))
    winner = p.run(start,1)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)