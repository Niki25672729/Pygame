# coding: utf-8
import pygame
from pygame.locals import *
import numpy.random as rn

clock = pygame.time.Clock()
screensize = (640, 480)
Fullscreen = False
minimap = True
gameover = False
timesup = False
victory = False
screenbit = 32
time = 10        #遊戲時間 (min)
maxHP = 250     #人物最大血量
rollHP = 200    #人物初始血量
speed = 300     #人物速度
hpBarLength = 500    #血條長度
key_image = "object/k3.png"
map_image = "object/map.png"
back_image = "object/background.jpg"
minimap_image = "object/minimap.jpg"
victory_image = "ending/victory.png"
gameover_image = "ending/gameover.png"
timesup_image = "ending/timesup.png"
keynumber = 18
mapnumber = 4

def load_image(file, width=None, number=None):
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if width == None:
        return surface
    height = surface.get_height()

    return [surface.subsurface(
        Rect((i * width, 0), (width, height))
        ) for i in xrange(number)]

def load_image2(file, height=None, number=None):
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if height == None:
        return surface
    width = surface.get_width()

    return [surface.subsurface(
        Rect((0, i*height), (width, height))
        ) for i in xrange(number)]

class Step():
    def __init__(self, (x, y), (width, height)):
        self.x = float(x)
        self.y = float(y)
        self.width = width
        self.height = height

    def collidepoint(self, x, y):
        if (self.x <= x <= (self.x + self.width)) & (self.y <= y <= (self.y + self.height)):
            return True
        else:
            return False

class Keys():
    __image = None
    def __init__(self, image):
        if Keys.__image == None:
            Keys.__image = image
            
        self.image = Keys.__image
    
    def opening(self, world, screen):
        global Fullscreen
        x, y = 110, 0.3
        font = pygame.font.SysFont("simhei", 20)
        event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
        time_passed = clock.tick()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                            world.render(screen)
                        else:
                            screen = pygame.display.set_mode(screensize, 0, screenbit)
                            world.render(screen)
            
            time_passed = clock.tick()
            x, y = flashBottonB(x, y, time_passed)
            text = font.render("Enter", True, (x, x, x))
            
            screen.blit(self.image, (230, 105))
            screen.blit(text, (357, 352))
            
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    world.roll.item['keys'] += 1
                    for i in world.roll.move.keys():
                        world.roll.move[i] = 0
                    world.roll.state = "Stop"
                    world.roll.direc = 'U'
                    time_passed = clock.tick()
                    break
            
            pygame.display.update()
        
class Maps():
    __image = None
    def __init__(self, image):
        if Maps.__image == None:
            Maps.__image = image
            
        self.image = Maps.__image
    
    def opening(self, world, screen):
        global Fullscreen, victory
        x, y = 110, 0.3
        font = pygame.font.SysFont("simhei", 20)
        event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
        time_passed = clock.tick()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                            world.render(screen)
                        else:
                            screen = pygame.display.set_mode(screensize, 0, screenbit)
                            world.render(screen)
            
            time_passed = clock.tick()
            x, y = flashBottonB(x, y, time_passed)
            text = font.render("Enter", True, (x, x, x))
            
            screen.blit(self.image, (230, 105))
            screen.blit(text, (357, 352))
            
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    world.roll.item['maps'] += 1
                    if world.roll.item['maps'] == mapnumber:
                        victory = True
                    for i in world.roll.move.keys():
                        world.roll.move[i] = 0
                    world.roll.state = "Stop"
                    world.roll.direc = 'U'
                    time_passed = clock.tick()
                    break
            
            pygame.display.update()
            
class charEvent():
    def __init__(self, image, changeHP = 0):
        self.image = image
        self.changeHP = changeHP
    
    def opening(self, world, screen):
        global Fullscreen
        x, y = 180, 0.2
        font = pygame.font.SysFont("simhei", 20)
        event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
        time_passed = clock.tick()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                            world.render(screen)
                        else:
                            screen = pygame.display.set_mode(screensize, 0, screenbit)
                            world.render(screen)
            
            time_passed = clock.tick()
            x, y = flashBottonW(x, y, time_passed)
            text = font.render("Enter", True, (x, x, x))
            
            screen.blit(self.image, (230, 105))
            screen.blit(text, (357, 352))
            
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    if world.roll.item['HP'] + self.changeHP > maxHP:
                        world.roll.item['HP'] = maxHP
                    elif world.roll.item['HP'] + self.changeHP <= 0:
                        world.roll.item['HP'] = 0
                        world.roll.state = "Dead"
                    else:
                        world.roll.item['HP'] += self.changeHP
                    for i in world.roll.move.keys():
                        world.roll.move[i] = 0
                    world.roll.state = "Stop"
                    world.roll.direc = 'U'
                    time_passed = clock.tick()
                    break
            
            pygame.display.update()
            
class objects():
    def __init__(self, (x, y), image, foot):
        #foot = [(x, y), (width, height)]
        self.image = image
        self.x = float(x)
        self.y = float(y)
        self.step = Step(foot[0], foot[1])
        
    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
        
    def update(self, time_passed, world, screen):
        return None
      
class topobjs():
    def __init__(self, image, (x, y)):
        self.image = image
        self.x = float(x)
        self.y = float(y)
        
    def moves(self, x, y):
        self.x += x
        self.y += y
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def update(self):
        return None

        
class trees(objects):
    __tree_image = None
    __leaf_image = None
    
    def __init__(self, (x, y)):
        if trees.__tree_image == None:
            trees.__tree_image = pygame.image.load("object/tree.png").convert_alpha()
        if trees.__leaf_image == None:
            trees.__leaf_image = pygame.image.load("object/leaf.png").convert_alpha()
        objects.__init__(self, (x, y), trees.__tree_image, foot = [(x+51, y+137), (27, 19)])
        self.leaf = topobjs(trees.__leaf_image, (x, y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))   
        
class bigtrees(objects):
    __tree_image = None
    __leaf_image = None
    
    def __init__(self, (x, y)):
        if bigtrees.__tree_image == None:
            bigtrees.__tree_image = pygame.image.load("object/bigtree.png").convert_alpha()
        if bigtrees.__leaf_image == None:
            bigtrees.__leaf_image = pygame.image.load("object/bigtree-leaf.png").convert_alpha()
        objects.__init__(self, (x, y), bigtrees.__tree_image, foot = [(x+71, y+124), (48, 21)])
        self.leaf = topobjs(bigtrees.__leaf_image, (x, y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))   
        
class deadtrees(objects):
    __image = None
    
    def __init__(self, (x, y)):
        if deadtrees.__image == None:
            deadtrees.__image = pygame.image.load("object/deadtree.png").convert_alpha()
        objects.__init__(self, (x, y), deadtrees.__image, foot = [(x+34, y+90), (13, 19)])

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  
        
class cactus(objects):
    __image = None
    
    def __init__(self, (x, y)):
        if cactus.__image == None:
            cactus.__image = pygame.image.load("object/cactus.png").convert_alpha()
        objects.__init__(self, (x, y), cactus.__image, foot = [(x+11, y+51), (13, 8)])

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) 
        
class stones(objects):
    __image = None
    
    def __init__(self, (x, y)):
        if stones.__image == None:
            stones.__image = pygame.image.load("object/stone.png").convert_alpha()
        objects.__init__(self, (x, y), stones.__image, foot = [(x, y+29), (40, 15)])

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) 
        
class graveA(objects):
    __image = None
    
    def __init__(self, (x, y)):
        if graveA.__image == None:
            graveA.__image = pygame.image.load("object/graveA.png").convert_alpha()
        objects.__init__(self, (x, y), graveA.__image, foot = [(x+2, y+34), (50, 20)])

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) 
        
class graveB(objects):
    __image = None
    
    def __init__(self, (x, y)):
        if graveB.__image == None:
            graveB.__image = pygame.image.load("object/graveB.png").convert_alpha()
        objects.__init__(self, (x, y), graveB.__image, foot = [(x+2, y+34), (50, 20)])

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) 

class treasureBoxes(objects):
    __rate = 40
    __width = 32
    __height = 32
    __number = 4
    __images = list()
    __cannotOpen_image = None
            
    def __init__(self, (x, y), content = None):
        objects.__init__(self, (x, y), "object/treasurebox.png", foot = [(x, y+13), (32, 19)])
        self.order = 0
        if len(treasureBoxes.__images) == 0:
            treasureBoxes.__images = load_image("object/treasurebox.png", self.__width, self.__number)
        if treasureBoxes.__cannotOpen_image == None:
            treasureBoxes.__cannotOpen_image = pygame.image.load("object/nokey.png").convert_alpha()
        
        self.image = self.__images[self.order]
        self.passed_time = 0
        self.opening = False
        self.cannotOpen = False
        self.content = content
        
    def changeState(self, event, world):
        if self.opening == False:
            if self.x-20 <= world.roll.step.x <= self.x+40:
                if self.y+30 <= world.roll.step.y <= self.y+70:
                    if world.roll.direc == 'U':
                        if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                            if world.roll.item['keys'] <> 0:
                                self.opening = True
                            else:
                                self.cannotOpen = True
                                
        
                            
    def setContent(self, content):
        self.content = content
                
    def update(self, passed_time, world, screen):
        if self.opening:
            if self.order < 3:
                self.passed_time += passed_time
                self.order = ( self.passed_time / self.__rate ) % self.__number
                if self.passed_time >= 120:
                    self.order = 3
                self.image = self.__images[self.order]
                if self.order == 3:
                    world.render(screen)
                    world.roll.item['keys'] -= 1
                    self.content.opening(world, screen)
                    self.image = self.__images[self.order]     
        elif self.cannotOpen:
            global Fullscreen
            self.cannotOpen = False
            x, y = 110, 0.3
            font = pygame.font.SysFont("simhei", 20)
            event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
            time_passed = clock.tick()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit() 
                    if event.type == KEYDOWN:
                        if event.key == K_f:
                            Fullscreen = not Fullscreen
                            if Fullscreen:
                                screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                                world.render(screen)
                            else:
                                screen = pygame.display.set_mode(screensize, 0, screenbit)
                                world.render(screen)
                        if event.key == K_ESCAPE: 
                            pygame.quit() 

                time_passed = clock.tick()
                x, y = flashBottonB(x, y, time_passed)
                text = font.render("Enter", True, (x, x, x))

                screen.blit(self.__cannotOpen_image, (207, 140))
                screen.blit(text, (373, 310))
                
                if event.type == KEYDOWN:
                    if (event.key == K_z) | (event.key == K_RETURN):
                        for i in world.roll.move.keys():
                            world.roll.move[i] = 0
                        world.roll.state = "Stop"
                        world.roll.direc = 'U'
                        time_passed = clock.tick()
                        break

                pygame.display.update()
         
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class Rocks(objects):
    __rate = 40
    __width = 73
    __height = 49
    __number = 4
    __images = list()
            
    def __init__(self, (x, y), content = None):
        objects.__init__(self, (x, y), "object/rock.png", foot = [(x+13, y+24), (43, 23)])
        self.order = 0
        if len(Rocks.__images) == 0:
            Rocks.__images = load_image("object/rock.png", self.__width, self.__number)
        
        self.image = self.__images[self.order]
        self.passed_time = 0
        self.opening = False
        self.content = content
        
    def changeState(self, event, world):
        if self.opening == False:
            if self.x-20 <= world.roll.step.x <= self.x+90:
                if self.y+40 <= world.roll.step.y <= self.y+100:
                    if world.roll.direc == 'U':
                        if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                            self.opening = True
                            
    def setContent(self, content):
        self.content = content
                
    def update(self, passed_time, world, screen):
        if self.opening:
            if self.order < 3:
                self.passed_time += passed_time
                self.order = ( self.passed_time / self.__rate ) % self.__number
                if self.passed_time >= 120:
                    self.order = 3
                self.image = self.__images[self.order]
                if self.order == 3:
                    world.render(screen)
                    self.content.opening(world, screen)
                    self.image = self.__images[self.order]
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class lake(objects):
    __rate = 150
    __width = 1056
    __height = 379
    __number = 30
    __images = list()
            
    def __init__(self, (x, y), content = None):
        objects.__init__(self, (x, y), "object/lake.png", foot = [(x, y), (1056, 379)])
        self.order = 0
        if len(lake.__images) == 0:
            lake.__images = load_image2("object/lake.png", self.__height, self.__number)
        
        self.image = self.__images[self.order]
        self.passed_time = 0
        self.opening = False
        self.content = content
        
    def changeState(self, event, world):
        if self.opening == False:
            if world.roll.step.x <= self.x+1056:
                if self.y-50 <= world.roll.step.y <= self.y+10:
                    if world.roll.direc == 'D':
                        if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                            self.opening = True
                
    def update(self, passed_time, world, screen):
        self.passed_time += passed_time
        self.order = ( self.passed_time / self.__rate ) % self.__number
        self.image = self.__images[self.order]
        if (self.opening) & (self.content <> None):
            world.render(screen)
            self.content.opening(world, screen)
            self.content = None
         
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class Background():
    def __init__(self, (x, y)):
        self.image = pygame.image.load(back_image).convert()
        self.x = -2180
        self.y = -2260
        self.cannotWalk = list([Step((3444+self.x, 4775+self.y), (83, 260)), Step((3527+self.x, 4751+self.y), (53, 41)),
                                Step((3576+self.x, 4740+self.y), (40, 19)), Step((3600+self.x, 4728+self.y), (27, 13)),
                                Step((3617+self.x, 4712+self.y), (68, 26)), Step((3669+self.x, 4625+self.y), (84, 95)),
                                Step((3738+self.x, 4609+self.y), (89, 31)), Step((3814+self.x, 4597+self.y), (22, 20)),
                                Step((3826+self.x, 4590+self.y), (23, 14)), Step((3840+self.x, 4584+self.y), (19, 14)),
                                Step((3853+self.x, 4574+self.y), (29, 22)), Step((3868+self.x, 4562+self.y), (67, 25)),
                                Step((3916+self.x, 4473+self.y), (83, 112)), Step((3982+self.x, 4459+self.y), (94, 20)),
                                Step((4058+self.x, 4446+self.y), (24, 19)), Step((4067+self.x, 4436+self.y), (30, 21)),
                                Step((4090+self.x, 4426+self.y), (26, 17)), Step((4108+self.x, 4410+self.y), (72, 31)),
                                Step((4159+self.x, 4256+self.y), (79, 164)), Step((4226+self.x, 4240+self.y), (96, 24)),
                                Step((4303+self.x, 4223+self.y), (34, 22)), Step((4328+self.x, 4211+self.y), (33, 17)),
                                Step((4348+self.x, 4194+self.y), (133, 27)), Step((4468+self.x, 4175+self.y), (30, 25)),
                                Step((4494+self.x, 4159+self.y), (31, 22)), Step((4556+self.x, 4116+self.y), (10, 31)),
                                Step((4518+self.x, 4147+self.y), (48, 17)), Step((3916+self.x, 4473+self.y), (83, 112)),
                                Step((3982+self.x, 4459+self.y), (94, 20)), Step((4550+self.x, 4174+self.y), (8, 312)),
                                Step((4488+self.x, 4440+self.y), (70, 36)), Step((4468+self.x, 4475+self.y), (30, 23)),
                                Step((4454+self.x, 4497+self.y), (19, 54)), Step((4471+self.x, 4536+self.y), (35, 82)),
                                Step((4506+self.x, 4602+self.y), (258, 14)), Step((4757+self.x, 4510+self.y), (11, 95)),
                                Step((4734+self.x, 4491+self.y), (30, 24)), Step((4734+self.x, 4446+self.y), (15, 46)),
                                Step((4605+self.x, 4440+self.y), (120, 14)), Step((4614+self.x, 4124+self.y), (8, 354)),
                                Step((4607+self.x, 4143+self.y), (139, 13)), Step((4723+self.x, 4126+self.y), (130, 17)),
                                Step((4808+self.x, 4107+self.y), (200, 20)), Step((182+self.x, 261+self.y), (9, 53)),
                                Step((187+self.x, 267+self.y), (9, 49)), Step((202+self.x, 281+self.y), (235, 47)), 
                                Step((502+self.x, 281+self.y), (91, 47)), Step((588+self.x, 268+self.y), (14, 48)),
                                Step((604+self.x, 263+self.y), (13, 52)), Step((614+self.x, 45+self.y), (7, 225)),
                                Step((182+self.x, 42+self.y), (7, 218)), Step((185+self.x, 42+self.y), (425, 7)),
                                Step((724+self.x, -10+self.y), (7, 520)), Step((865+self.x, -5+self.y), (7, 690)),
                                Step((-5+self.x, 464+self.y), (220, 50)), Step((269+self.x, 464+self.y), (430, 50)),
                                Step((703+self.x, 464+self.y), (11, 50)), Step((708+self.x, 464+self.y), (10, 50)),
                                Step((727+self.x, 644+self.y), (126, 50)), Step((-3+self.x, 644+self.y), (670, 50)),
                                Step((857+self.x, 638+self.y), (16, 52)), Step((-2+self.x, 2650+self.y), (175, 55)),
                                Step((118+self.x, 2707+self.y), (55, 182)), Step((170+self.x, 2834+self.y), (220, 55)),
                                Step((334+self.x, 2886+self.y), (55, 163)), Step((387+self.x, 3000+self.y), (190, 55)),
                                Step((522+self.x, 3048+self.y), (55, 158)), Step((568+self.x, 3147+self.y), (1379, 55)), 
                                Step((1423+self.x, 2979+self.y), (370, 180)), Step((1583+self.x, 3202+self.y), (367, 152))])
        
    def moves(self, x, y):
        self.x += x
        self.y += y
        for i in self.cannotWalk:
            i.x += x
            i.y += y
    
    def update(self, passed_time, world, screen):
        return None
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #for i in self.cannotWalk:
            #screen.fill((0, 0, 0), ((i.x, i.y), (i.width, i.height)))

class roll(pygame.sprite.Sprite):
    __rate = 80
    __width = 32
    __height = 48
    __number = 5
    imageDict = dict({'U':"roll/run-u-simple.png", 
                      'D':"roll/run-d-simple.png", 
                      'L':"roll/run-l-simple.png", 
                      'LU':"roll/run-lu-simple.png", 
                      'LD':"roll/run-ld-simple.png", 
                      'R':"roll/run-r-simple.png", 
                      'RU':"roll/run-ru-simple.png", 
                      'RD':"roll/run-rd-simple.png"})
    hurtDict = dict({'U':"roll/run-u-hurt.png", 
                     'D':"roll/run-d-hurt.png", 
                     'L':"roll/run-l-hurt.png", 
                     'LU':"roll/run-lu-hurt.png", 
                     'LD':"roll/run-ld-hurt.png", 
                     'R':"roll/run-r-hurt.png", 
                     'RU':"roll/run-ru-hurt.png", 
                     'RD':"roll/run-rd-hurt.png"})
    images = dict()
    hurtimages = dict()
    deadimages = list()
    
    def __init__(self, (x, y), foot, speed, hp):
        #foot = [(x, y), (width, height)]
        self.order = 1
        pygame.sprite.Sprite.__init__(self)
        if len(roll.images) == 0:
            for i in roll.imageDict.keys():
                roll.images[i] = load_image(roll.imageDict[i], roll.__width, roll.__number)
        if len(roll.hurtimages) == 0:
            for i in roll.hurtDict.keys():
                roll.hurtimages[i] = load_image(roll.hurtDict[i], roll.__width, roll.__number)
        if len(roll.deadimages) == 0:
            roll.deadimages = load_image("roll/dead.png", 32, 28)
        self.image = roll.images['D'][self.order]
        self.x = float(x)
        self.y = float(y)
        self.passed_time = 0
        self.hurtCount = 0
        self.speed = speed
        self.direc = 'D'
        self.state = "Stop"   #"Stop", "Run", "Dead"
        self.getHurt = False
        self.move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
        self.step = Step(foot[0], foot[1])
        self.item = dict({'HP':hp, 'keys':0, 'maps':0})
        self.rect = pygame.Rect(self.x, self.y, 32, 48)
 
    def storeMoving(self, event):
        if (victory <> True) & (self.state <> "Dead") & (timesup <> True):
            if event.type == KEYDOWN:
                if event.key in self.move:
                    self.move[event.key] = 1
            if event.type == KEYUP:
                self.move[event.key] = 0
        else:
            for i in self.move.keys():
                self.move[i] = 0

    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
    
    def changeDirection(self):
        if self.move[K_LEFT] == 1:
            if self.move[K_UP] == 1:
                self.direc = 'LU'
            elif self.move[K_DOWN] == 1:
                self.direc = 'LD'
            else:
                self.direc = 'L'
        elif self.move[K_RIGHT] == 1:
            if self.move[K_UP] == 1:
                self.direc = 'RU'
            elif self.move[K_DOWN] == 1:
                self.direc = 'RD'
            else:
                self.direc = 'R'
        else:
            if self.move[K_UP] == 1:
                self.direc = 'U'
            elif self.move[K_DOWN] == 1:
                self.direc = 'D'

                
    def changeState(self):
        if self.item['HP'] == 0:
            self.state = "Dead"
        if self.state <> "Dead":
            num = 0
            for i in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
                num += self.move[i]
            if num > 0:
                self.state = "Run"
            else:
                self.state = "Stop"
    
    def update(self, passed_time):
        global gameover
        self.changeDirection()
        self.changeState()
        self.rect = pygame.Rect(self.x, self.y, 32, 48)
        if self.state <> "Dead":
            if self.getHurt:
                self.hurtCount += passed_time
                if self.state == "Stop":
                    self.image = self.hurtimages[self.direc][0]
                else:
                    self.passed_time += passed_time
                    self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
                    if self.order == 1 and self.passed_time > self.__rate:
                        self.passed_time = 0
                    self.image = self.hurtimages[self.direc][self.order]
                if self.hurtCount > 120:
                    self.getHurt = False
                    self.hurtCount = 0
            else:
                if self.state == "Stop":
                    self.image = self.images[self.direc][0]
                else:
                    self.passed_time += passed_time
                    self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
                    if self.order == 1 and self.passed_time > self.__rate:
                        self.passed_time = 0
                    self.image = self.images[self.direc][self.order]
        else:
            if self.order <> 27:
                self.passed_time += passed_time
                self.order = ( self.passed_time / 40 ) % 28
                if self.passed_time >= 1080:
                    self.order = 27
                self.image = self.deadimages[self.order]
            else:
                gameover = True
            
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class flowerR(pygame.sprite.Sprite):
    __rate = 150
    __width = 32
    __height = 36
    __number = 4
    imageDict = dict({'U':"monster/r_flower_up.png", 
                      'D':"monster/r_flower_down.png", 
                      'L':"monster/r_flower_left.png", 
                      'R':"monster/r_flower_right.png"})
    images = dict()
    
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        if len(flowerR.images) == 0:
            for i in flowerR.imageDict.keys():
                flowerR.images[i] = load_image(flowerR.imageDict[i], flowerR.__width, flowerR.__number)
        self.order = 1
        self.direc = 'D'
        self.image = flowerR.images[self.direc][self.order]
        self.x = x
        self.y = y
        self.speed = 250
        self.passed_time = 0
        self.attackCount = 0
        self.move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
        self.state = ""    #"", "targeted"
        self.walkState = "Stop"
        self.step = Step((self.x+7,self.y+30), (17, 6))
        self.rect = pygame.Rect(self.x, self.y, 32, 36)
    
    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
        
    def changeState(self, roll):
        if (abs(roll.step.x - self.step.x) < 200) & (abs(roll.step.y - self.step.y) < 200):
            self.state = "targeted"
        else:
            self.state = ""
        
    def changeDirection(self):
        if self.move[K_LEFT] == 1:
            self.direc = 'L'
        elif self.move[K_RIGHT] == 1:
            self.direc = 'R'
        elif self.move[K_UP] == 1:
            self.direc = 'U'
        elif self.move[K_DOWN] == 1:
            self.direc = 'D'
                
    def changeWalkState(self):
        num = 0
        for i in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
            num += self.move[i]
        if num > 0:
            self.walkState = "Run"
        else:
            self.walkState = "Stop"
            
    def walk(self, world, back, roll, time_passed):
        for i in self.move.keys():
            self.move[i] = 0
        if (not victory) & (not timesup):
            distance = self.speed*time_passed/1000.0
            tol = distance*1.5
            if self.state == "targeted":
                for i in self.move.keys():
                    self.move[i] = 0
                if self.step.x - roll.step.x > tol:
                    self.move[K_LEFT] = 1
                elif self.step.x - roll.step.x < -tol:
                    self.move[K_RIGHT] = 1
                if self.move[K_LEFT] + self.move[K_RIGHT] > 0:
                    pass
                else:
                    if self.step.y - roll.step.y > tol:
                        self.move[K_UP] = 1
                    elif self.step.y - roll.step.y < -tol:
                        self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
            
    def attack(self, time_passed, roll):
        self.rect = pygame.Rect(self.x, self.y, 32, 36)
        if not timesup:
            if pygame.sprite.collide_rect(self, roll):
                if self.attackCount == 0:
                    roll.getHurt = True
                    roll.item['HP'] -= 10
                    if roll.item['HP'] < 0:
                        roll.item['HP'] = 0
                    self.attackCount += time_passed
                elif self.attackCount > 500:
                    self.attackCount = 0
                else:
                    self.attackCount += time_passed
            else:
                self.attackCount = 0
            
    def update(self, time_passed, world):
        self.changeState(world.roll)
        self.walk(world, world.background, world.roll, time_passed)
        self.changeWalkState()
        self.changeDirection()
        self.attack(time_passed, world.roll)
        if self.walkState == "Stop":
            self.image = self.images['D'][0]
        else:
            self.passed_time += time_passed
            self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
            if self.order == 1 and self.passed_time > self.__rate:
                self.passed_time = 0
            self.image = self.images[self.direc][self.order]
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class flowerB(pygame.sprite.Sprite):
    __rate = 150
    __width = 32
    __height = 36
    __number = 4
    imageDict = dict({'U':"monster/b_flower_up.png", 
                      'D':"monster/b_flower_down.png", 
                      'L':"monster/b_flower_left.png", 
                      'R':"monster/b_flower_right.png"})
    images = dict()
    
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        if len(flowerB.images) == 0:
            for i in flowerB.imageDict.keys():
                flowerB.images[i] = load_image(flowerB.imageDict[i], flowerB.__width, flowerB.__number)
        self.order = 1
        self.direc = 'D'
        self.image = flowerB.images[self.direc][self.order]
        self.x = x
        self.y = y
        self.speed = 250
        self.passed_time = 0
        self.attackCount = 0
        self.move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
        self.state = "explore"    #"explore", "targeted"
        self.walkState = "Stop"
        self.step = Step((self.x+7,self.y+30), (17, 6))
        self.rect = pygame.Rect(self.x, self.y, 32, 36)
    
    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
        
    def changeState(self, roll):
        if (abs(roll.step.x - self.step.x) < 200) & (abs(roll.step.y - self.step.y) < 200):
            self.state = "targeted"
            self.speed = 200
        else:
            self.state = "explore"
            self.speed = 50
        
    def changeDirection(self):
        if self.move[K_LEFT] == 1:
            self.direc = 'L'
        elif self.move[K_RIGHT] == 1:
            self.direc = 'R'
        elif self.move[K_UP] == 1:
            self.direc = 'U'
        elif self.move[K_DOWN] == 1:
            self.direc = 'D'
                
    def changeWalkState(self):
        num = 0
        for i in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
            num += self.move[i]
        if num > 0:
            self.walkState = "Run"
        else:
            self.walkState = "Stop"
            
    def walk(self, world, back, roll, time_passed):
        for i in self.move.keys():
            self.move[i] = 0
        if (not victory) & (not timesup):
            distance = self.speed*time_passed/1000.0
            tol = distance*1.5
            if self.state == "targeted":
                for i in self.move.keys():
                    self.move[i] = 0
                if self.step.x - roll.step.x > tol:
                    self.move[K_LEFT] = 1
                elif self.step.x - roll.step.x < -tol:
                    self.move[K_RIGHT] = 1
                if self.move[K_LEFT] + self.move[K_RIGHT] > 0:
                    pass
                else:
                    if self.step.y - roll.step.y > tol:
                        self.move[K_UP] = 1
                    elif self.step.y - roll.step.y < -tol:
                        self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
                    
    def attack(self, time_passed, roll):
        self.rect = pygame.Rect(self.x, self.y, 32, 36)
        if not timesup:
            if pygame.sprite.collide_rect(self, roll):
                if self.attackCount == 0:
                    roll.getHurt = True
                    roll.item['HP'] -= 10
                    if roll.item['HP'] < 0:
                        roll.item['HP'] = 0
                    self.attackCount += time_passed
                elif self.attackCount > 500:
                    self.attackCount = 0
                else:
                    self.attackCount += time_passed
            else:
                self.attackCount = 0
                
    def update(self, time_passed, world):
        self.changeState(world.roll)
        self.walk(world, world.background, world.roll, time_passed)
        self.changeWalkState()
        self.changeDirection()
        self.attack(time_passed, world.roll)
        if self.walkState == "Stop":
            self.image = self.images['D'][0]
        else:
            self.passed_time += time_passed
            self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
            if self.order == 1 and self.passed_time > self.__rate:
                self.passed_time = 0
            self.image = self.images[self.direc][self.order]
                
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class slimeG(pygame.sprite.Sprite):
    __rate = 250
    __width = 32
    __height = 32
    __number = 4
    imageDict = dict({'U':"monster/g_slime_up.png", 
                      'D':"monster/g_slime_down.png", 
                      'L':"monster/g_slime_left.png", 
                      'R':"monster/g_slime_right.png"})
    images = dict()
    
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        if len(slimeG.images) == 0:
            for i in slimeG.imageDict.keys():
                slimeG.images[i] = load_image(slimeG.imageDict[i], slimeG.__width, slimeG.__number)
        self.order = 0
        self.direc = 'D'
        self.image = slimeG.images[self.direc][self.order]
        self.x = x
        self.y = y
        self.speed = 50
        self.passed_time = 0
        self.attackCount = 0
        self.walkCount = 0
        self.move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
        self.state = "explore"    #"explore", "targeted"
        self.walkState = "Stop"
        self.step = Step((self.x+7,self.y+30), (17, 6))
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
    
    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
        
    def changeState(self, roll):
        if (abs(roll.step.x - self.step.x) < 600) & (abs(roll.step.y - self.step.y) < 600):
            self.state = "targeted"
            self.speed = 70
        else:
            self.state = "explore"
            self.speed = 50
        
    def changeDirection(self):
        if self.move[K_LEFT] == 1:
            self.direc = 'L'
        elif self.move[K_RIGHT] == 1:
            self.direc = 'R'
        elif self.move[K_UP] == 1:
            self.direc = 'U'
        elif self.move[K_DOWN] == 1:
            self.direc = 'D'
                
    def changeWalkState(self):
        num = 0
        for i in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
            num += self.move[i]
        if num > 0:
            self.walkState = "Run"
        else:
            self.walkState = "Stop"
            
    def walk(self, world, back, roll, time_passed):
        if timesup:
            for i in self.move.keys():
                self.move[i] = 0
        elif not victory:
            distance = self.speed*time_passed/1000.0
            tol = distance*1.5
            if (self.state == "explore") & (self.walkCount == 0):
                self.walkCount += time_passed
                for i in self.move.keys():
                    self.move[i] = 0
                num = rn.normal()
                if abs(self.x - back.x) > 100:
                    if abs(self.x  - back.x - 4968) > 100:
                        if abs(self.y - back.y) > 100:
                            if abs(self.y - back.y - 4968) > 100:
                                num = rn.randint(7)
                                if num == 0:
                                    self.move[K_LEFT] = 1
                                elif num == 1:
                                    self.move[K_RIGHT] = 1
                                elif num == 2:
                                    self.move[K_UP] = 1
                                elif num == 3:
                                    self.move[K_DOWN] = 1
                                else:
                                    pass
                            else:
                                if -1 <= num <= 1:
                                    self.move[K_UP] = 1
                                elif num < -1:
                                    self.move[K_LEFT] = 1
                                else:
                                    self.move[K_RIGHT] = 1
                        else:
                            if -1 <= num <= 1:
                                self.move[K_DOWN] = 1
                            elif num < -1:
                                self.move[K_LEFT] = 1
                            else:
                                self.move[K_RIGHT] = 1
                    else:
                        if abs(self.y - back.y) > 100:
                            if abs(self.y - back.y - 4968) > 100:
                                if -1 <= num <= 1:
                                    self.move[K_LEFT] = 1
                                elif num < -1:
                                    self.move[K_UP] = 1
                                else:
                                    self.move[K_DOWN] = 1
                            else:
                                if num >= 0:
                                    self.move[K_LEFT] = 1
                                else:
                                    self.move[K_UP] = 1
                        else:
                            if num >= 0:
                                self.move[K_LEFT] = 1
                            else:
                                self.move[K_DOWN] = 1
                else:
                    if abs(self.y - back.y) > 100:
                        if abs(self.y - back.y - 4968) > 100:
                            if -1 <= num <= 1:
                                self.move[K_RIGHT] = 1
                            elif num < -1:
                                self.move[K_UP] = 1
                            else:
                                self.move[K_DOWN] = 1
                        else:
                            if num >= 0:
                                self.move[K_RIGHT] = 1
                            else:
                                self.move[K_UP] = 1
                    else:
                        if num >= 0:
                            self.move[K_RIGHT] = 1
                        else:
                            self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
            elif self.state == "targeted":
                for i in self.move.keys():
                    self.move[i] = 0
                if self.step.x - roll.step.x > tol:
                    self.move[K_LEFT] = 1
                elif self.step.x - roll.step.x < -tol:
                    self.move[K_RIGHT] = 1
                if self.move[K_LEFT] + self.move[K_RIGHT] > 0:
                    pass
                else:
                    if self.step.y - roll.step.y > tol:
                        self.move[K_UP] = 1
                    elif self.step.y - roll.step.y < -tol:
                        self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
            else:
                self.walkCount += time_passed
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
                if self.walkCount > 2000:
                    self.walkCount = 0
    def attack(self, time_passed, roll):
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        if (not victory) & (not timesup):
            if pygame.sprite.collide_rect(self, roll):
                if self.attackCount == 0:
                    roll.getHurt = True
                    roll.item['HP'] -= 50
                    if roll.item['HP'] < 0:
                        roll.item['HP'] = 0
                    self.attackCount += time_passed
                elif self.attackCount > 500:
                    self.attackCount = 0
                else:
                    self.attackCount += time_passed
            else:
                self.attackCount = 0
            
    def update(self, time_passed, world):
        self.changeState(world.roll)
        self.walk(world, world.background, world.roll, time_passed)
        self.changeWalkState()
        self.changeDirection()
        self.attack(time_passed, world.roll)
        if self.walkState == "Stop":
            self.image = self.images[self.direc][0]
        else:
            self.passed_time += time_passed
            self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
            if self.order == 1 and self.passed_time > self.__rate:
                self.passed_time = 0
            self.image = self.images[self.direc][self.order]
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class slimeB(pygame.sprite.Sprite):
    __rate = 250
    __width = 32
    __height = 32
    __number = 4
    imageDict = dict({'U':"monster/b_slime_up.png", 
                      'D':"monster/b_slime_down.png", 
                      'L':"monster/b_slime_left.png", 
                      'R':"monster/b_slime_right.png"})
    images = dict()
    
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        if len(slimeB.images) == 0:
            for i in slimeB.imageDict.keys():
                slimeB.images[i] = load_image(slimeB.imageDict[i], slimeB.__width, slimeB.__number)
        self.order = 0
        self.direc = 'D'
        self.image = slimeB.images[self.direc][self.order]
        self.x = x
        self.y = y
        self.speed = 50
        self.passed_time = 0
        self.attackCount = 0
        self.walkCount = 0
        self.move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
        self.state = "explore"    #"explore", "targeted"
        self.walkState = "Stop"
        self.step = Step((self.x+7,self.y+30), (17, 6))
        self.rect = pygame.Rect(self.x, self.y, 32, 36)
    
    def moves(self, x, y):
        self.x += x
        self.step.x += x
        self.y += y
        self.step.y += y
        
    def changeState(self, roll):
        if (abs(roll.step.x - self.step.x) < 600) & (abs(roll.step.y - self.step.y) < 600):
            self.state = "targeted"
            self.speed = 70
        else:
            self.state = "explore"
            self.speed = 50
        
    def changeDirection(self):
        if self.move[K_LEFT] == 1:
            self.direc = 'L'
        elif self.move[K_RIGHT] == 1:
            self.direc = 'R'
        elif self.move[K_UP] == 1:
            self.direc = 'U'
        elif self.move[K_DOWN] == 1:
            self.direc = 'D'
                
    def changeWalkState(self):
        num = 0
        for i in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
            num += self.move[i]
        if num > 0:
            self.walkState = "Run"
        else:
            self.walkState = "Stop"
            
    def walk(self, world, back, roll, time_passed):
        if timesup:
            for i in self.move.keys():
                self.move[i] = 0
        elif not victory:
            distance = self.speed*time_passed/1000.0
            tol = distance*1.5
            if (self.state == "explore") & (self.walkCount == 0):
                self.walkCount += time_passed
                for i in self.move.keys():
                    self.move[i] = 0
                num = rn.normal()
                if abs(self.x - back.x) > 100:
                    if abs(self.x - back.x - 4968) > 100:
                        if abs(self.y - back.y) > 100:
                            if abs(self.y - back.y - 4964) > 100:
                                num = rn.randint(7)
                                if num == 0:
                                    self.move[K_LEFT] = 1
                                elif num == 1:
                                    self.move[K_RIGHT] = 1
                                elif num == 2:
                                    self.move[K_UP] = 1
                                elif num == 3:
                                    self.move[K_DOWN] = 1
                                else:
                                    pass
                            else:
                                if -1 <= num <= 1:
                                    self.move[K_UP] = 1
                                elif num < -1:
                                    self.move[K_LEFT] = 1
                                else:
                                    self.move[K_RIGHT] = 1
                        else:
                            if -1 <= num <= 1:
                                self.move[K_DOWN] = 1
                            elif num < -1:
                                self.move[K_LEFT] = 1
                            else:
                                self.move[K_RIGHT] = 1
                    else:
                        if abs(self.y - back.y) > 100:
                            if abs(self.y - back.y - 4968) > 100:
                                if -1 <= num <= 1:
                                    self.move[K_LEFT] = 1
                                elif num < -1:
                                    self.move[K_UP] = 1
                                else:
                                    self.move[K_DOWN] = 1
                            else:
                                if num >= 0:
                                    self.move[K_LEFT] = 1
                                else:
                                    self.move[K_UP] = 1
                        else:
                            if num >= 0:
                                self.move[K_LEFT] = 1
                            else:
                                self.move[K_DOWN] = 1
                else:
                    if abs(self.y - back.y) > 100:
                        if abs(self.y - back.y - 4968) > 100:
                            if -1 <= num <= 1:
                                self.move[K_RIGHT] = 1
                            elif num < -1:
                                self.move[K_UP] = 1
                            else:
                                self.move[K_DOWN] = 1
                        else:
                            if num >= 0:
                                self.move[K_RIGHT] = 1
                            else:
                                self.move[K_UP] = 1
                    else:
                        if num >= 0:
                            self.move[K_RIGHT] = 1
                        else:
                            self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
            elif self.state == "targeted":
                for i in self.move.keys():
                    self.move[i] = 0
                if self.step.x - roll.step.x > tol:
                    self.move[K_LEFT] = 1
                elif self.step.x - roll.step.x < -tol:
                    self.move[K_RIGHT] = 1
                if self.move[K_LEFT] + self.move[K_RIGHT] > 0:
                    pass
                else:
                    if self.step.y - roll.step.y > tol:
                        self.move[K_UP] = 1
                    elif self.step.y - roll.step.y < -tol:
                        self.move[K_DOWN] = 1
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
            else:
                self.walkCount += time_passed
                if stop(self, world, distance):
                    self.moves(self.move[K_RIGHT]*distance-self.move[K_LEFT]*distance, self.move[K_DOWN]*distance-self.move[K_UP]*distance)
                if self.walkCount > 2000:
                    self.walkCount = 0
    def attack(self, time_passed, roll):
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        if (not victory) & (not timesup):
            if pygame.sprite.collide_rect(self, roll):
                if self.attackCount == 0:
                    roll.getHurt = True
                    roll.item['HP'] -= 50
                    if roll.item['HP'] < 0:
                        roll.item['HP'] = 0
                    self.attackCount += time_passed
                elif self.attackCount > 500:
                    self.attackCount = 0
                else:
                    self.attackCount += time_passed
            else:
                self.attackCount = 0
            
    def update(self, time_passed, world):
        self.changeState(world.roll)
        self.walk(world, world.background, world.roll, time_passed)
        self.changeWalkState()
        self.changeDirection()
        self.attack(time_passed, world.roll)
        if self.walkState == "Stop":
            self.image = self.images[self.direc][0]
        else:
            self.passed_time += time_passed
            self.order = ( self.passed_time / self.__rate ) % (self.__number-1) + 1
            if self.order == 1 and self.passed_time > self.__rate:
                self.passed_time = 0
            self.image = self.images[self.direc][self.order]
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
      
class World():
    def __init__(self, background, roll, time, maxHP, hpBarLength, mapnumber):
        self.roll = roll
        self.background = background
        self.monsters = list()
        self.objs = list()
        self.treasureboxes = list()
        self.rocks = list()
        self.tops = list()
        self.font = pygame.font.SysFont("simhei", 40)
        self.font2 = pygame.font.SysFont("simhei", 25)
        ##時間
        self.time = time
        self.timecount = 0
        self.timeclock = list([str(time), "00"])
        ##血條
        self.maxHP = float(maxHP)
        self.hpBarLength = float(hpBarLength)
        ##物件
        self.key_image = pygame.image.load(key_image).convert_alpha()
        self.map_image = pygame.image.load(map_image).convert_alpha()
        self.mapnumber = mapnumber
        ##小地圖
        self.minimap_image = pygame.image.load(minimap_image).convert()
        ##結局
        self.victory_image = load_image2(victory_image, 480, 10)
        self.gameover_image = load_image2(gameover_image, 480, 10)
        self.timesup_image = load_image2(timesup_image, 125, 10)
        self.overindex = 0
        self.gameovercount = 0
        self.bottonx = 120
        self.bottony = 0.3
        self.overtext = self.font.render("Enter", True, (self.bottonx, self.bottonx, self.bottonx))
        
    def addmonster(self, monster):
        self.monsters.append(monster)
        
    def addobj(self, obj):
        self.objs.append(obj)
        
    def addbox(self, box):
        self.treasureboxes.append(box)
        
    def addrock(self, rock):
        self.rocks.append(rock)
        
    def addtop(self, top):
        self.tops.append(top)
        
    def moves(self, x, y):
        self.background.moves(x, y)
        for i in self.monsters:
            i.moves(x, y)
        for i in self.objs:
            i.moves(x, y)
        for i in self.treasureboxes:
            i.moves(x, y)
        for i in self.rocks:
            i.moves(x, y)
        for i in self.tops:
            i.moves(x, y)
        
    def update(self, time_passed, screen):
        global gameover, timesup
        self.roll.update(time_passed)
        for monster in self.monsters:
            monster.update(time_passed, self)
        for obj in self.objs:
            obj.update(time_passed, self, screen)
        for box in self.treasureboxes:
            box.update(time_passed, self, screen)
        for box in self.rocks:
            box.update(time_passed, self, screen)
        for obj in self.tops:
            obj.update()
        ##時間
        if not gameover:
            self.timecount += time_passed/1000.0
            remaintime = self.time*60.0+1 - self.timecount
            if remaintime/60 < 0:
                self.timeclock = list(["0", "00"])
                timesup = True
            else:
                if int(remaintime)%60 < 10:
                    self.timeclock = list([str(int(remaintime/60)), "0"+str(int(remaintime)%60)])
                else:
                    self.timeclock = list([str(int(remaintime/60)), str(int(remaintime)%60)])
            if remaintime/60 < 3:
                self.timetext = self.font.render(self.timeclock[0]+":"+self.timeclock[1], True, (255, 0, 0))
            else:
                self.timetext = self.font.render(self.timeclock[0]+":"+self.timeclock[1], True, (255, 255, 255))
        ##血量
        self.HPtext = self.font2.render(str(self.roll.item['HP']), True, (0, 0, 0))
        ##物件
        self.keytext = self.font.render(":"+str(self.roll.item['keys']), True, (0, 0, 0))
        self.maptext = self.font.render(":"+str(self.roll.item['maps'])+"/"+str(self.mapnumber), True, (0, 0, 0))
        ##結局
        if victory:
            if self.overindex <> 9:
                self.overindex = ( self.gameovercount / 150 ) % 10
                self.gameovercount += time_passed
                self.overimage = self.victory_image[self.overindex]
            else:
                self.overtext = self.font.render("Enter", True, (self.bottonx, self.bottonx, self.bottonx))
                self.bottonx, self.bottony = flashBottonB(self.bottonx, self.bottony, time_passed)
                if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                    menu(screen)
        elif gameover:
            if self.overindex <> 9:
                self.overindex = ( self.gameovercount / 150 ) % 10
                self.gameovercount += time_passed
                self.overimage = self.gameover_image[self.overindex]
            else:
                self.overtext = self.font.render("Enter", True, (self.bottonx, self.bottonx, self.bottonx))
                self.bottonx, self.bottony = flashBottonB(self.bottonx, self.bottony, time_passed)
                if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                    menu(screen)
        elif timesup:
            if self.overindex <> 9:
                self.overindex = ( self.gameovercount / 150 ) % 10
                self.gameovercount += time_passed
                self.overimage = self.timesup_image[self.overindex]
            else:
                self.overtext = self.font.render("Enter", True, (self.bottonx, self.bottonx, self.bottonx))
                self.bottonx, self.bottony = flashBottonB(self.bottonx, self.bottony, time_passed)
                if (pygame.key.get_pressed()[K_z]) | (pygame.key.get_pressed()[K_RETURN]):
                    menu(screen)
            
    def render(self, screen):
        item = list()
        self.background.draw(screen)
        item.append(self.roll)
        for i in self.monsters:
            item.append(i)
        for i in self.objs:
            item.append(i)
        for i in self.treasureboxes:
            item.append(i)
        for i in self.rocks:
            item.append(i)
        for i in range(len(item)):
            for j in range(len(item)-i-1):
                if item[j].step.y > item[j+1].step.y:
                    temp = item[j]
                    item[j] = item[j+1]
                    item[j+1] = temp
        for i in range(len(item)):
            item[i].draw(screen)
        for i in self.tops:
            i.draw(screen)
            
        ##時間
        if len(self.timeclock[0]) < 2:
            screen.blit(self.timetext, (531, 2))  
        else:
            screen.blit(self.timetext, (511, 2))  
        ##血條
        bloodBar = pygame.draw.rect(screen, (200, 0, 0), (10, 5, self.hpBarLength*(self.roll.item['HP']/self.maxHP), 20))   
        screen.blit(self.HPtext, (300, 2))
        ##物件
        screen.blit(self.key_image, (520, 46))
        screen.blit(self.keytext, (552, 41))
        screen.blit(self.map_image, (520, 83))
        screen.blit(self.maptext, (552, 77))
        ##小地圖
        if minimap:
            screen.fill((0, 0, 0), pygame.Rect((476, 316), (154, 154)))
            screen.blit(self.minimap_image, (478, 318))
            pygame.draw.circle(screen, (255, 0, 0), (478+int(abs(self.roll.step.x - self.background.x)*0.03), 318+int(abs(self.roll.step.y - self.background.y)*0.03)), 4)
        ##結局
        if victory:
            screen.blit(self.overimage, (0, 0))
            if self.overindex == 9:
                screen.blit(self.overtext, (540, 439))
        elif gameover:
            screen.blit(self.overimage, (0, 0))
            if self.overindex == 9:
                screen.blit(self.overtext, (540, 439))
        elif timesup:
            screen.blit(self.overimage, (21.5, 177.5))
            if self.overindex == 9:
                screen.blit(self.overtext, (540, 439))
                
def stop(roll, world, distance):
    flag = 1
    x_l = roll.step.x-roll.move[K_LEFT]*distance+roll.move[K_RIGHT]*distance
    x_r = roll.step.x-roll.move[K_LEFT]*distance+roll.move[K_RIGHT]*distance+24
    y_u = roll.step.y-roll.move[K_UP]*distance+roll.move[K_DOWN]*distance
    y_d = roll.step.y-roll.move[K_UP]*distance+roll.move[K_DOWN]*distance+13
    A = list([(x_l+i, y_u) for i in range(32)])+list([(x_l, y_u+i) for i in range(1, 13)])+list([(x_l+i, y_d) for i in range(1, 32)])+list([(x_r, y_u+i) for i in range(1, 13)])
    
    for area in world.background.cannotWalk:
        for (x, y) in A:
            if area.collidepoint(x, y):
                flag = 0
                break
    if flag == 0:
        return flag == 1
    else:
        for obj in world.treasureboxes:
            for (x, y) in A:
                if obj.step.collidepoint(x, y):
                    flag = 0
                    break
    if flag == 0:
        return flag == 1
    else:
        for obj in world.rocks:
            for (x, y) in A:
                if obj.step.collidepoint(x, y):
                    flag = 0
                    break
    if flag == 0:
        return flag == 1
    else:
        for obj in world.objs:
            for (x, y) in A:
                if obj.step.collidepoint(x, y):
                    flag = 0
                    break

    return flag == 1
   
def screenmove(screen, world, time_passed):
    time_passed_seconds = time_passed / 1000.0 
    distance = time_passed_seconds * world.roll.speed
    tol = distance*1.5
           
    if (abs(world.roll.x-304) <= tol) & (abs(world.roll.y-216) <= tol):        
        if world.background.x >=0:
            if stop(world.roll, world, distance):
                world.roll.moves(-world.roll.move[K_LEFT]*distance, 0)
        else:
            if stop(world.roll, world, distance):
                world.moves(world.roll.move[K_LEFT]*distance, 0)
        if world.background.x <= -4360:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance, 0)
        else:
            if stop(world.roll, world, distance):
                world.moves(-world.roll.move[K_RIGHT]*distance, 0)
        if world.background.y >= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(0, -world.roll.move[K_UP]*distance)
        else:
            if stop(world.roll, world, distance):
                world.moves(0, world.roll.move[K_UP]*distance)   
        if world.background.y <= -4520:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance)
        else:
            if stop(world.roll, world, distance):
                world.moves(0, -world.roll.move[K_DOWN]*distance)

    elif (abs(world.roll.x-304) > tol) & (abs(world.roll.y-216) <= tol):
        if 0 < world.roll.x < 608:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance-world.roll.move[K_LEFT]*distance, 0)
        elif world.roll.x <= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance, 0)
        elif 608 <= world.roll.x:
            if stop(world.roll, world, distance):
                world.roll.moves(-world.roll.move[K_LEFT]*distance, 0)
        if world.background.y >= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(0, -world.roll.move[K_UP]*distance)
        else:
            if stop(world.roll, world, distance):
                world.moves(0, world.roll.move[K_UP]*distance)
        if world.background.y <= -4520:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance)
        else:
            if stop(world.roll, world, distance):
                world.moves(0, -world.roll.move[K_DOWN]*distance)
            
    elif (abs(world.roll.x-304) <= tol) & (abs(world.roll.y-213) > tol):
        if 0 < world.roll.y < 432:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance-world.roll.move[K_UP]*distance)
        elif world.roll.y <= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance)
        elif 432 <= world.roll.y:
            if stop(world.roll, world, distance):
                world.roll.moves(0, -world.roll.move[K_UP]*distance)
        if world.background.x >= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(-world.roll.move[K_LEFT]*distance, 0)
        else:
            if stop(world.roll, world, distance):
                world.moves(world.roll.move[K_LEFT]*distance, 0)
        if world.background.x <= -4360:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance, 0)
        else:
            if stop(world.roll, world, distance):
                world.moves(-world.roll.move[K_RIGHT]*distance, 0)
            
    else:# (abs(world.roll.x-(640 - 32)/2) > tol) & (abs(world.roll.y-(480 - 48)/2) > tol):
        if 0 < world.roll.x < 608:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance-world.roll.move[K_LEFT]*distance, 0)
        elif world.roll.x <= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(world.roll.move[K_RIGHT]*distance, 0)
        elif world.roll.x >= 608:
            if stop(world.roll, world, distance):
                world.roll.moves(-world.roll.move[K_LEFT]*distance, 0)
        if 0 < world.roll.y < 432:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance-world.roll.move[K_UP]*distance)
        elif world.roll.y <= 0:
            if stop(world.roll, world, distance):
                world.roll.moves(0, world.roll.move[K_DOWN]*distance)
        elif world.roll.y >= 432:
            if stop(world.roll, world, distance):
                world.roll.moves(0, -world.roll.move[K_UP]*distance)
    
    return world
         
def flashBottonW(x, y, passed_time):
    if 170 < x < 255:
        x += y*passed_time
    else:
        y *= -1
        x += y*passed_time
    if x > 255:
        x = 255
    if x < 170:
        x = 170
    return x, y

def flashBottonB(x, y, passed_time):
    if 0 < x < 130:
        x += y*passed_time
    else:
        y *= -1
        x += y*passed_time
    if x > 130:
        x = 130
    if x < 0:
        x = 0
    return x, y

def direction(move, event):
    if event.type == KEYDOWN:
        if event.key in move:
            move[event.key] = 1
    if event.type == KEYUP:
        move[event.key] = 0
        
    return move
     
def menu(screen):
    global Fullscreen
    move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
    font = pygame.font.SysFont("simhei", 40)
    x, y = 180, 0.2
    num = 0
    text = ["Start", "Exit"]
    #pygame.event.clear()
    event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
    pygame.mixer.music.stop()
    time_passed = clock.tick()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                    else:
                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                
            move = direction(move, event)
            if 0 < num < 1:
                num -= move[K_UP]
                num += move[K_DOWN]
            elif num == 0:
                num += move[K_DOWN]
            else:
                num -= move[K_UP]
                
        time_passed = clock.tick()
        if num == 0: 
            x, y = flashBottonW(x, y, time_passed) 
            text_surface1 = font.render(text[0], True, (x, x, x))
            text_surface2 = font.render(text[1], True, (150, 150, 150))
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    main(screen)
        else: 
            x, y = flashBottonW(x, y, time_passed)
            text_surface1 = font.render(text[0], True, (150, 150, 150))
            text_surface2 = font.render(text[1], True, (x, x, x))
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    pygame.quit()
        
        screen.fill((0, 0, 0))
        screen.blit(text_surface1, (270, 80))
        screen.blit(text_surface2, (280, 160))

        pygame.display.update()
            
def option(world, screen):
    global Fullscreen
    b_x, b_y = 110, 0.3
    w_x, w_y = 180, 0.2
    x, y = 165, 152
    num = 0
    move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
    font = pygame.font.SysFont("simhei", 40)
    event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
    main_image = pygame.image.load("menu/submeun.png").convert_alpha()
    control_image = pygame.image.load("menu/control.png").convert_alpha()
    rule_image = pygame.image.load("menu/rule.png").convert_alpha()
    time_passed = clock.tick()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                    else:
                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                        
            move = direction(move, event)
            if 0 < num < 3:
                num -= move[K_UP]
                num += move[K_DOWN]
            elif num == 0:
                num += move[K_DOWN]
            else:
                num -= move[K_UP]
                
        time_passed = clock.tick()
        screen.blit(main_image, (88, 0))
        screen.fill((w_x, 0, 0), ((x, y+num*71),(319, 10)))
        screen.fill((w_x, 0, 0), ((x, y+num*71),(10, 63)))
        screen.fill((w_x, 0, 0), ((x, y+57+num*71),(319, 10)))
        screen.fill((w_x, 0, 0), ((x+309, y+num*71),(10, 63)))
        w_x, w_y = flashBottonW(w_x, w_y, time_passed)
        if num == 0:
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    for i in world.roll.move.keys():
                        world.roll.move[i] = 0
                    world.roll.state = "Stop"
                    world.roll.direc = 'U'
                    time_passed = clock.tick()
                    break
        elif num == 1:
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
                    world.render(screen)
                    time_passed = clock.tick()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit() 
                            if event.type == KEYDOWN:
                                if event.key == K_f:
                                    Fullscreen = not Fullscreen
                                    if Fullscreen:
                                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                                        world.render(screen)
                                    else:
                                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                                        world.render(screen)

                        time_passed = clock.tick()
                        b_x, b_y = flashBottonB(b_x, b_y, time_passed)
                        text = font.render("Quit ", True, (b_x, b_x, b_x))
                        screen.blit(control_image, (66, 0))
                        screen.blit(text, (473, 392))
                        if event.type == KEYDOWN:
                            if (event.key == K_z) | (event.key == K_RETURN):
                                event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
                                world.render(screen)
                                time_passed = clock.tick()
                                break
                        pygame.display.update()
        elif num == 2:
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
                    world.render(screen)
                    time_passed = clock.tick()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit() 
                            if event.type == KEYDOWN:
                                if event.key == K_f:
                                    Fullscreen = not Fullscreen
                                    if Fullscreen:
                                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                                        world.render(screen)
                                    else:
                                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                                        world.render(screen)

                        time_passed = clock.tick()
                        b_x, b_y = flashBottonB(b_x, b_y, time_passed)
                        text = font.render("Quit ", True, (b_x, b_x, b_x))
                        screen.blit(rule_image, (66, 0))
                        screen.blit(text, (473, 392))
                        if event.type == KEYDOWN:
                            if (event.key == K_z) | (event.key == K_RETURN):
                                event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
                                world.render(screen)
                                time_passed = clock.tick()
                                break
                        pygame.display.update()
        else:
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    pygame.quit()
                
        pygame.display.update()
        
def main(screen):
    global Fullscreen, minimap, gameover, timesup, victory
    pygame.event.clear()
    gameover = False
    timesup = False
    victory = False
    Adol = roll((304, 216), [(310, 251), (20, 13)], speed, rollHP)
    background = Background((0, -4520))
    world = World(background, Adol, time, maxHP, hpBarLength, mapnumber)
    tree = list([bigtrees((-1970, -2200)), trees((-223, -568)), trees((-53, 1000)), trees((600, 1000)), trees((-2150, -2100)), 
                 trees((-2045, 650)), trees((-1864, 853)), trees((-700, 2489)), trees((-1400, -563)), trees((-1920, -1856)), 
                 trees((-1023, -630)), trees((-1200, -1648)), trees((-930, -1)), trees((-956, 450)), trees((-820, 600)), 
                 trees((-870, -920)), trees((-520, 321)), trees((153, 765)), trees((-2250, 1980)),trees((-2200, 2000)),
                 trees((-2150, 2010)),trees((-2100, 2005)),trees((-2050, 2000)),trees((-2000, 1995)),trees((-1950, 2000)),
                 trees((-1900, 2005)),trees((-1850, 1995)),trees((-1800, 1990)),trees((-1750, 1985)),trees((-1700, 1981)),
                 trees((-1650, 1980)),trees((-1600, 1975)),trees((-1550, 1977)),trees((-1500, 1980)),trees((-1450, 1983)),
                 trees((-1400, 1990)),trees((-1350, 1995)),trees((-1300, 1995)),trees((-1250, 1990)),trees((-1200, 1985)),
                 trees((-1150, 1990)),trees((-1100, 1980)),trees((-1050, 1960)),trees((-1000, 1960)),trees((-950, 1955)),
                 trees((-900, 1950)),trees((-855, 1945)),trees((-1070, 2150)),trees((-1070, 2175)),trees((-1075, 2200)),
                 trees((-1078, 2225)),trees((-1080, 2250)),trees((-1085, 2275)),trees((-1085, 2300)),trees((-1090, 2325)),
                 trees((-1090, 2350)),trees((-1095, 2375)),trees((-1099, 2400)),trees((-900, 2050)),trees((-880, 2075)),
                 trees((-870, 2050)),trees((-855, 2077)),trees((-838, 2098)),trees((-825, 2133)),trees((-810, 2160)),
                 trees((-800, 2100)),trees((-770, 2125)),trees((-750, 2150)),trees((-738, 2175)),trees((-710, 2200)),
                 trees((-710, 2240)),trees((-700, 2277)),trees((-710, 2311)),trees((-709, 2350)),trees((-689, 2393)),
                 trees((-668, 2430)),trees((-911, 2460)),trees((-911, 2500)),trees((-900, 2388)),trees((-888, 2411)),
                 trees((-850, 2450)),trees((-831, 2493)),trees((-799, 2522)),trees((-777, 2550)),trees((-750, 2580)),
                 trees((-711, 2610)),trees((-700, 2640)),trees((-711, 2670)),trees((-739, 2700)),trees((-725, 2725)),
                 trees((-700, 2750)),trees((-699, 2775)),trees((-666, 2800))])
    monster = list([flowerR((-128, 96)), flowerB((1045, -235)), slimeG((2000, 456)), slimeB((-560, -1258)),
                    flowerR((1000, -1000)),flowerR((800, -800)),flowerB((-1045, 0)),flowerB((0, -1235)),
                    slimeG((300, 1439)), slimeB((-2000, 393))])
    #monster = list([flowerR((100, 100))])
    grave = list([graveA((2440, 2261)), graveB((2500, 2261))])
    cactu = list([cactus((2000,-1500)),cactus((2139,-1393)),cactus((1755,-1688)),cactus((2039,-1747)),
                  cactus((1940,-1031)),cactus((1111,-1411)),cactus((1393,-1310)),cactus((390,-1339)),
                  cactus((2498,-2039))])
    deadtree = list([deadtrees((1900,-1400)),deadtrees((1750,-1031)),deadtrees((2220,-999)),deadtrees((100,-1800)),
                     deadtrees((-1700,0)),deadtrees((2593,-1515))])
    stone = list([stones((1800,-1300)),stones((1700,-1300)),stones((1600,-1300)),stones((1500,-1300)),
                  stones((1580,-1240)),stones((1720,-1240)),stones((1650,-1188)),stones((1650,-1386)),
                  stones((1751,-1145)),stones((1549,-1145)),stones((39,-1987)),stones((2539,-1955))])
    eventImage = load_image("event/event.jpg", 180, 23)
    charevent = list([charEvent(eventImage[0], -20), charEvent(eventImage[1], 10), 
                      charEvent(eventImage[2], -10), charEvent(eventImage[3], -10), 
                      charEvent(eventImage[4], -20), charEvent(eventImage[5], -20), 
                      charEvent(eventImage[6], -10), charEvent(eventImage[7], -20), 
                      charEvent(eventImage[8], 10), charEvent(eventImage[9], -20), 
                      charEvent(eventImage[10], -20), charEvent(eventImage[11], -10), 
                      charEvent(eventImage[12], -20), charEvent(eventImage[13], -50), 
                      charEvent(eventImage[14], -10), charEvent(eventImage[15], 20), 
                      charEvent(eventImage[16], -10), charEvent(eventImage[17], 10), 
                      charEvent(eventImage[18], 20), charEvent(eventImage[19], 10)])
    box = list([treasureBoxes((1600, 200)), treasureBoxes((-2100, -39)), treasureBoxes((140, 300)),
                treasureBoxes((2345, 2260)), treasureBoxes((-1050, 1900)), treasureBoxes((-1270, -2000)),
                treasureBoxes((-2139, 539)), treasureBoxes((428, 2364)), treasureBoxes((-1850, -2100)),
                treasureBoxes((1654, -1268)), treasureBoxes((2045, -426)), treasureBoxes((1064, -1239)),
                treasureBoxes((-520, 2520)), treasureBoxes((1845, 393))])
    rock = list([Rocks((50, -450)), Rocks((-1005, 300)), Rocks((50, 300)), Rocks((898, -356)),
                 Rocks((550, 450)), Rocks((-105, 200)), Rocks((550, 800)), Rocks((2639, -1994)),
                 Rocks((784, -2145)), Rocks((1257, -962)), Rocks((-598, 224)), Rocks((-1845, -1968)),
                 Rocks((-1342, -23)), Rocks((-965, 547)), Rocks((-41, 2068)), Rocks((2684, 1764)),
                 Rocks((1156, 2039)), Rocks((-1390, -2099)), Rocks((375, 2587)), Rocks((-874, 1569)),
                 Rocks((-1094, -2003)), Rocks((2576, -1568)), Rocks((2431, 1698)), Rocks((-1356, 1407)),
                 Rocks((2393, -1555)), Rocks((840, 2640)), Rocks((-301, 1968)), Rocks((1462, -2000))])
    index1 = rn.permutation(len(charevent))
    index2 = rn.permutation(len(box))
    index3 = rn.permutation(len(rock))
    for i in range(mapnumber):
        box[index2[i]].setContent(Maps(eventImage[22]))
        world.addbox(box[index2[i]])
    for i in range(keynumber):
        rock[index3[i]].setContent(Keys(eventImage[21]))
        world.addrock(rock[index3[i]])
    flag = 1
    for i in range(len(charevent)):
        if flag == 1:
            for j in range(len(box)):
                if box[j].content == None:
                    box[j].setContent(charevent[index1[i]])
                    world.addbox(box[j])
                    break
                if j == len(box)-1:
                    flag = 0
        if flag == 0:
            for j in range(len(rock)):
                if rock[j].content == None:
                    rock[j].setContent(charevent[index1[i]])
                    world.addrock(rock[j])
                    break
    for i in range(len(monster)):
        world.addmonster(monster[i])
    for i in range(len(grave)):
        world.addobj(grave[i])
    for i in range(len(tree)):
        world.addobj(tree[i])
        world.addtop(tree[i].leaf)
    for i in range(len(cactu)):
        world.addobj(cactu[i])
    for i in range(len(stone)):
        world.addobj(stone[i])
    for i in range(len(deadtree)):
        world.addobj(deadtree[i])
    world.addrock(lake((-2200, 2380), charEvent(eventImage[20], maxHP)))
    
    b_x, b_y = 110, 0.3
    num, page = 0, 0
    move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
    font = pygame.font.SysFont("simhei", 40)
    text = list(["Next", "Back", "Quit"])
    control_image = pygame.image.load("menu/control.png").convert_alpha()
    rule_image = pygame.image.load("menu/rule.png").convert_alpha()
    time_passed = clock.tick()
    pygame.mixer.music.play(loops=-1)
    time_passed = clock.tick()
    world.update(time_passed, screen)
    while True:
        event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                        world.render(screen)
                    else:
                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                        world.render(screen)
                        
            move = direction(move, event)
            if page == 0:
                num = 0
            else:
                if num == 0:
                    num += move[K_LEFT]
                else:
                    num -= move[K_RIGHT]
        
        time_passed = clock.tick()
        if page == 0:
            world.render(screen)
            screen.blit(control_image, (66, 0))
            text_surface = font.render(text[0], True, (b_x, b_x, b_x))
            screen.blit(text_surface, (473, 392))
            if event.type == KEYDOWN:
                if (event.key == K_z) | (event.key == K_RETURN):
                    page = 1
        elif page == 1:
            if num == 0:
                world.render(screen)
                screen.blit(rule_image, (66, 0))
                text_surface1 = font.render(text[2], True, (b_x, b_x, b_x))
                text_surface2 = font.render(text[1], True, (150, 150, 150))
                screen.blit(text_surface1, (473, 392))
                screen.blit(text_surface2, (90, 392))
                if event.type == KEYDOWN:
                    if (event.key == K_z) | (event.key == K_RETURN):
                        break
            else:
                world.render(screen)
                screen.blit(rule_image, (66, 0))
                text_surface1 = font.render(text[1], True, (b_x, b_x, b_x))
                text_surface2 = font.render(text[2], True, (150, 150, 150))
                screen.blit(text_surface2, (473, 392))
                screen.blit(text_surface1, (90, 392))
                if event.type == KEYDOWN:
                    if (event.key == K_z) | (event.key == K_RETURN):
                        page = 0
        b_x, b_y = flashBottonB(b_x, b_y, time_passed)
                
        pygame.display.update()
    
    time_passed = clock.tick()  
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        screen = pygame.display.set_mode(screensize, FULLSCREEN, screenbit)
                    else:
                        screen = pygame.display.set_mode(screensize, 0, screenbit)
                if event.key == K_ESCAPE: 
                    option(world, screen) 
                    event = pygame.event.Event(KEYUP, {'scancode': 44, 'key': 122, 'mod': 0})
                if event.key == K_m:
                    minimap = not minimap
                for i in world.treasureboxes:
                    i.changeState(event, world)
                for i in world.rocks:
                    i.changeState(event, world)
                    
            Adol.storeMoving(event)
        
        time_passed = clock.tick(50)
        if not timesup:
            world = screenmove(screen, world, time_passed)
        world.update(time_passed, screen)
        
        world.render(screen)
        
        pygame.display.update()

def run():
    pygame.init()
    screen = pygame.display.set_mode(screensize, 0, screenbit)
    pygame.display.set_caption("OMG")
    pygame.mouse.set_visible(False)
    pygame.mixer.music.load("music/Ys6_10.ogg")

    menu(screen)
    #main(screen)
if __name__ == "__main__":
    run()
