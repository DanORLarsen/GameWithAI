import pygame
import neat
import os
##Inspiried by https://nerdparadise.com/programming/pygame and https://www.youtube.com/watch?v=wQWWzBHUJWM&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=6

class Player(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.speed = 7
        self.goalHit = ""
        self.number = 0
        self.distance = []
        self.colidePoints = []
        self.milestonePoints = []
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (self.x, self.y, 30, 30))

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

    def aiMoveUp(self):
        #print("UP")
        self.rect.y -= self.speed
    def aiMoveDown(self):
        #print("DOWN")
        self.rect.y += self.speed
    def aiMoveLeft(self):
        #print("LEFT")
        self.rect.x -= self.speed
    def aiMoveRight(self):
        #print("Right")
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


    def milestoneCollisionMore(self, list):
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
    enemyX = 395
    enemyY = 500
    goal = 1000
    global done
    done = False
    win = False
    speed = 3
    enemyMvoingUp = True
    i = 0
    tick_counter = 0

    
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

        pressed = pygame.key.get_pressed()
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if pressed[pygame.K_ESCAPE]:
                        done = True
            ##TODO: Make this into a class for player, also same with enemy        
        

            for x, player in enumerate(players):
                #Motivation
                ge[x].fitness -= 0.01
                if( tick_counter >= 3):
                    #output = nets[x].activate([abs(player.getNextMilestone().centery - player.rect.centery),abs(player.getNextMilestone().centerx - player.rect.centerx), player.rect.centerx, player.rect.centery])
                    output = nets[x].activate([player.getNextMilestone().centerx - player.rect.centerx , player.getNextMilestone().centery - player.rect.centery, player.rect.centerx, player.rect.centery])

                    if(tick_counter%400 == 0):
                        string_in_string = "player - {} Distance ({}, {}), \nPos ({}, {}) \n({}, {})".format(x,player.getNextMilestone().centerx - player.rect.centerx, player.getNextMilestone().centery - player.rect.centery, player.rect.centerx, player.rect.centery, player.getNextMilestone().centerx, player.getNextMilestone().centery)

                        #print(string_in_string)
                        #print(x, output)

                    #print(output)
                    if (output[0] > 0):
                        ge[x].fitness += 0.0
                        player.aiMoveRight()
                    if (output[1] > 0):
                        ge[x].fitness += 0.0
                        player.aiMoveLeft()
                    if (output[2] > 0):
                        ge[x].fitness += 0.0
                        player.aiMoveUp()
                    if (output[3] > 0):
                        ge[x].fitness += 0.0
                        player.aiMoveDown()
                    
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
            goalWall = pygame.draw.rect(screen, (0,255,0), pygame.Rect(goal + 50, 0, 500, height%4))
            pygame.draw.line(screen, (0,255,0), (goal+100,0), (goal+100,height), 200)

            milestoneColor = (0,220,220)
            #Milesstones for AI (Reinforcement + Survival of the fittest)
            milestone0 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(210, 10, 10, 120))
            milestone1 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(210, 120, 160, 10))
            milestone2 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(210, 220, 160, 10))
            milestone3 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(200, 220, 10, 80))
            milestone4 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(100, 220, 10, 80))
            milestone5 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(10, 300, 90, 10))
            milestone6 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(275, 300, 10, 80))
            milestone7 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(275, 380, 95, 10))
            milestone8 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(275, 510, 95, 10))
            milestone9 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(370, 520, 10, 80))
            milestone10 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(375, 380, 95, 10))
            milestone11 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(470, 170, 10, 100))
            #Adding milestone helpers
            helper0 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(100, 300, 10, 90)) #after milestone5
            helper1 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(375, 510, 95, 10)) #after milestone9
            helper2 = pygame.draw.rect(screen, milestoneColor, pygame.Rect(380, 250, 90, 10)) #after milestone10

            friendlyList.append(milestone0)
            friendlyList.append(milestone1)
            friendlyList.append(milestone2)
            friendlyList.append(milestone3)
            friendlyList.append(milestone4)
            friendlyList.append(milestone5)
            friendlyList.append(helper0)
            friendlyList.append(milestone6)
            friendlyList.append(milestone7)
            friendlyList.append(milestone8)
            friendlyList.append(milestone9)
            friendlyList.append(helper1)
            friendlyList.append(milestone10)
            friendlyList.append(helper2)
            friendlyList.append(milestone11)
            friendlyList.append(goalWall)

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
            deathtext = myfont.render("Dead {0}/1500".format(deaths), 1, (0,0,0))
            screen.blit(deathtext, (40, 700))
            if (win):
                winText = myWinFont.render("YOU WON", 1, (0,0,0))
                screen.blit(winText, (500, 350))
            
            #Enemies
            enemy = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX, enemyY, 60, 60))
                #Collide with this enemy
            hostileList.append(enemy)
            
            for x, player in enumerate(players):
                if(player.milestonePoints == []):
                    player.getMilestones(friendlyList)
                    
                #Collide wall logic + more
                if(player.number <= 22):
                    if(player.rect.colliderect(player.milestonePoints[player.number])):
                        ge[x].fitness += 50
                       # print(ge[x].fitness)
                        player.increaseMilestomeNumber()
                        if(player.number == 15):
                             ge[x].fitness = 2000
                       # print(player.milestonePoints[player.number])

                #Faster Reset
                if(ge[x].fitness <= -0.4):
                    nets.pop(x)
                    ge.pop(x)
                    players.pop(x)
                    deaths += 1

                if(player.createCollisionWithMore(hostileList)):
                    ge[x].fitness -= 5
                    nets.pop(x)
                    ge.pop(x)
                    players.pop(x)
                    deaths += 1
                    if (deaths == 1500): #Number of AI players per generation (So if all are dead = new Generation)
                        done = True
                if (player.createCollisionWith(goalWall)):
                    ge[x].fitness = 2000
                    done = True
                player.draw(screen)
                #To give the AI the goal
                player.getGoal(goalWall)

                #Simple solution to adding milestones to AI.
            if (tick_counter == 350):
                done = True
                print("TIME EXPIRED")

            tick_counter +=1
            pygame.display.update()
            pygame.display.flip()
            clock.tick(400)
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
    winner = p.run(start,200)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)