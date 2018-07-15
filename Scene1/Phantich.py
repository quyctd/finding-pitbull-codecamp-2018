import pygame
import time
from pygame.locals import *


class Scene1:

    def __init__(self):
        self.end = False
        self.pressClose = False

    def update(self, canvas):
        fps = pygame.time.Clock()
        height = 640
        done = False
        const_x_player = 0
        const_x_poop = 2000
        frame = 0
        framexe = 0
        # class Black_hole:
        #      def __init__(self,cord):
        #          self.cord = cord
        #      def draw_water(self):
        #          for pos in self.cord:
        #             water = pygame.image.load('waterfall.png')
        #             canvas.blit(water, (pos, 40))
        #      def draw_hole(self):
        #          if jump_in_black == True:
        #              self.draw_water()
        class Poop:
            def __init__(self, x, y):
                self.x = x
                self.y = y
            def draw(self):
                po = pygame.image.load('Scene1/redbull.png')
                canvas.blit(po,(self.x,self.y+50))
        class Car:
            def __init__(self, x, y):
                self.x = x
                self.y = y
            def draw(self):
                if car_active == True:
                    c1 = pygame.image.load('Scene1/car.png')
                    canvas.blit(c1,(self.x,self.y))
                else:
                    self.x = 0
                    self.y = 0
        class Horse:
            def __init__(self, x, y, framexe):
                self.x = x
                self.y = y
                self.time = framexe
            def draw(self):
                    h = [pygame.image.load('Scene1/xe1.png'),pygame.image.load('Scene1/xe2.png'),pygame.image.load('Scene1/xe3.png'),pygame.image.load('Scene1/xe4.png'),pygame.image.load('Scene1/xe5.png'),pygame.image.load('Scene1/xe6.png')]
                    canvas.blit(h[self.time//3], (self.x, self.y+30))
        class Hearth:
            def __init__(self, n_life):
                self.life1 = n_life
            def draw(self):
                H = pygame.image.load('Scene1/hearth.png')
                for lifetime in range(1,self.life1+1):
                    canvas.blit(H, (10*lifetime, 0))
        # class Brigde:
        #     def __init__(self,x,y):
        #         self.x = x
        #         self.y = y
        #     def draw(self):
        #         b = pygame.image.load('')
        class Player:
            def __init__(self,x,y,frame):
                self.x = x
                self.y = y
                self.time = frame
            def draw(self):
                imager = [pygame.image.load('Scene1/4.png'),pygame.image.load('Scene1/5.png'),pygame.image.load('Scene1/6.png'),pygame.image.load('Scene1/7.png'),pygame.image.load('Scene1/8.png'),pygame.image.load('Scene1/9.png')]
                imagel = [pygame.image.load('Scene1/1.png'),pygame.image.load('Scene1/3.png'),pygame.image.load('Scene1/2.png'),pygame.image.load('Scene1/0.png'),pygame.image.load('Scene1/24.png'),pygame.image.load('Scene1/88.png')]
                if image_stm != 'dead':
                    if x_change > 0:
                        canvas.blit(imager[self.time//3],(self.x,self.y))
                        self.time += 1
                    elif x_change < 0:
                        canvas.blit(imagel[self.time//3],(self.x,self.y))
                        self.time += 1
                else:
                    image = 'Scene1/crash.png'
                    playerl = pygame.image.load(image)
        class Game:
            def __init__(self,Ca,Hearth1,Poo,Horse,Player):
                self.player = Player
                self.car = Ca
                self.hearth = Hearth1
                # self.black_hole = Hole
                self.poop = Poo
                self.horse = Horse
            def draw(self):
                self.car.draw()
                self.hearth.draw()
                # self.black_hole.draw_hole()
                self.poop.draw()
                self.horse.draw()
                self.player.draw()
        image_stm = ''
        life = 1
        move_r = False
        movemap = 0
        x_change = 0
        y_change = 0
        shit_weapon = False
        car_active = True
        x1 = const_x_player
        y1 = height - 150
        xcar = 2000
        ycar = height-260
        xpoop = const_x_poop
        ypoop = height - 150
        xhorse = -200
        yhorse = height - 300
        timer = 1
        timer_dead = 0
        background = pygame.image.load('Scene1/street.png')
        done_name = False
        jump = False
        time_vacham = 0
        tg = 0
        tg2 = 1
        while not done:
            pygame.init()
            Ca = Car(xcar, ycar)
            He = Hearth(life)
            Po = Poop(xpoop, ypoop)
            Hor = Horse(xhorse, yhorse, framexe)
            P = Player(x1, y1,frame)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        self.pressClose = True
                        done = True
                elif event.type == KEYDOWN and done_name == False:
                    if event.key == K_RETURN:
                        done_name = True
                        car_active = True
            if done_name == False:
                done_name = True
            if done_name == True and image_stm != 'dead'and image_stm != 'win':
                #di chuyển nhân vật
                x1 += x_change
                xhorse += 35
                framexe += tg2
                if xhorse >= 800:
                    tg2 = 0
                    framexe += tg2
                    move_r = True
                    xpoop += 15
                if move_r == True and x1 < 720:
                    frame +=1
                    x_change = 2
                    x1 += x_change
                    movemap -= 25
                    xpoop -= 25
                if frame >= 18:
                    frame = 0
                if framexe >= 18:
                    framexe = 0
                if shit_weapon != True and ypoop != y1:
                    ypoop = y1
                if y_change < 0:
                    jump = True
                    tg = 1
                if y_change > 0:
                    jump = False
                    khoa = True
                timer += tg
                if timer >= 7:
                    y_change = 60
                    timer = 0
                    tg = 0
                if y1 >= height - 240:
                    y1 = height - 240
                    khoa = False
                if jump == False:
                    jump_in_black = False
                if xcar-50 <= x1 + 32 <= xcar + 150 and ycar <= y1 + 20 <= ycar + 220 and image_stm != 'dead' and shit_weapon == False: #va cham oto
                    time_vacham +=1
                    y1 -= 20
                    x1 += 10
                    if time_vacham >= 8:
                        y1 += 0
                        x1 += 0
                        time_vacham = 0
                if x1 <= xpoop <= x1+65 and y1 <= ypoop <= y1 + 100 and shit_weapon == False:
                    shit_weapon = True
                    life += 80
                if shit_weapon == True:
                    xpoop = x1 + 30
                    ypoop = y1
                    car_active = False
                if image_stm == 'crashed' or image_stm == 'fall' or image_stm == 'natbet':
                    y_change = -23
                    timer_dead+=1
                    y_poop = y1
                    x_poop = x1
                    shit_weapon = False
                    if timer_dead > 2:
                        y_change = 20
                        life -= 1
                        timer_dead = 0
                    xpoop -= 30
                    image_stm = 'alive'
                y1 += y_change
                if life <= 0:
                    image_stm = 'dead'
                xcar -= 40
                if xcar <= -270:
                    xcar = 2000
                if x1 >= 675:
                    x_change = 0
                    image_stm = 'win'
                canvas.blit(background, (movemap, 0))
                Game(Ca,He,Po,Hor,P).draw()
                pygame.display.update()
                fps.tick(10)
            if image_stm == 'win':
                done = True