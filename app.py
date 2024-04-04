from pygame.locals import *
import pygame, json, time

from scanner import Scanner
from client import Client

class App:
    def __init__(self):
        pygame.init()
        path = 'data/'
        self.data = [[['void' for k in range(3)] for j in range(3)] for i in range(2)]
        for floor in json.load(open(path+'properties.json')):
            data = json.load(open(path+floor+'.json'))
            for shop in data:
                x, y, z = data[shop]['coords']
                self.data[z][x][y] = shop
        self.floor = 0
        self.pos = 'Java Coffee House'
        self.travelPath = []
        self.name = 'YESHWANTH'
        self.screen = pygame.display.set_mode((384, 640), RESIZABLE)
        pygame.display.set_caption('NOVA')
        self.introScreen()
    def introScreen(self):
        run, ind = True, 1
        while run:
            self.screen.fill('#3C444B')
            logo = pygame.image.load('new assets/main/logo.png')
            self.screen.blit(logo, (145, 170))
            font = pygame.font.SysFont('voyager', 90)
            self.screen.blit(font.render('NOVA', True, 'white'), (108, 270))
            for i in range(ind):
                pygame.draw.circle(self.screen, 'white', (170+(i*20), 575), 4, 0)
            ind += 1
            if ind == 4:
                run = False
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
            time.sleep(0.5)
        self.homeScreen()
    def homeScreen(self):
        run = True
        while run:
            self.screen.fill('#3C444B')
            logo = pygame.image.load('new assets/main/icon.png')
            self.screen.blit(logo, (155, 100))
            font = pygame.font.SysFont('voyager', 55)
            bfont = pygame.font.SysFont('open sans', 45)
            self.screen.blit(font.render('NOVA', True, 'white'), (147, 177))
            button = pygame.image.load('new assets/main/button.png')
            self.screen.blit(button, (127, 260))
            self.screen.blit(button, (127, 320))
            self.screen.blit(bfont.render('Login', True, '#2A343D'), (160, 272))
            self.screen.blit(bfont.render('Sign up', True, '#2A343D'), (147, 332))
            events = pygame.event.get()
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                tempx, tempy = x, y
                if 127 <= x <=277:
                    if 272 <= y <= 322:
                        option, run = 'Login', False
                    elif 332 <= y <= 382:
                        option, run = 'Sign Up', False
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
        if option == 'Login':
            self.login()
        elif option == 'Sign Up':
            self.signUp()
    def login(self):
        self.homePage()
    def signUp(self):
        self.homePage()
    def homePage(self):
        run, tempx, tempy = True, 0, 0
        while run:
            self.screen.fill('#F5F5F5')
            font = pygame.font.SysFont('voyager', 35)
            cfont = pygame.font.SysFont('voyager', 25)
            self.screen.blit(font.render(self.name, True, '#222222'), (10, 15))
            notification = pygame.image.load('new assets/main/notification.png')
            self.screen.blit(notification, (355, 15))
            pygame.draw.rect(self.screen, '#949494', (0, 585, 384, 680))
            arr = [('Brooksfield', 'Coimbatore'), ('Fun Mall', 'Kerala'), ('Lulu Mall', 'Coimbatore'), ('Prozone', 'Coimbatore')]
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/'+arr[i][0]+'.png'), (30, 100+115*i))
                self.screen.blit(font.render(arr[i][0], True, '#222222'), (200, 130+115*i))
                self.screen.blit(cfont.render(arr[i][1], True, '#222222'), (200, 155+115*i))
            arr = ['home', 'love', 'qr', 'user']
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/main/'+arr[i]+'.png'), (43+90*i, 600))
            events = pygame.event.get()
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                tempx, tempy = x, y
                if 600 <= y <= 624:
                    if 133 <= x <= 157:
                        option, run = 'Wish List', False
                    elif 223 <= x <= 247:
                        option, run = 'Scan QR', False
                    elif 313 <= x <= 337:
                        option, run = 'Profile', False
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
        #print(option)
        if option == 'Scan QR':
            self.scanQR()
        elif option == 'Profile':
            self.profile()
        elif option == 'Wish List':
            self.wishList()
    def scanQR(self):
        ip = Scanner()
        ip = ip.data
        print(ip)
        time.sleep(2)
        obj = Client(self.name, self.viewShop)
    def profile(self):
        run, tempx, tempy = True, 0, 0
        while run:
            self.screen.fill('#F5F5F5')
            font = pygame.font.SysFont('voyager', 35)
            cfont = pygame.font.SysFont('voyager', 25)
            self.screen.blit(font.render(self.name, True, '#222222'), (10, 15))
            notification = pygame.image.load('new assets/main/notification.png')
            self.screen.blit(notification, (355, 15))
            pygame.draw.rect(self.screen, '#949494', (0, 585, 384, 680))
            arr = [('Brooksfield', 'Coimbatore'), ('Fun Mall', 'Kerala'), ('Lulu Mall', 'Coimbatore')]
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/'+arr[i][0]+'.png'), (30, 130+125*i))
                self.screen.blit(font.render(arr[i][0], True, '#222222'), (200, 155+125*i))
                self.screen.blit(cfont.render(arr[i][1], True, '#222222'), (200, 180+125*i))
            arr = ['home', 'love', 'qr', 'user']
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/main/'+arr[i]+'.png'), (43+90*i, 600))
            events = pygame.event.get()
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                tempx, tempy = x, y
                if 600 <= y <= 624:
                    if 133 <= x <= 157:
                        option, run = 'Wish List', False
                    elif 223 <= x <= 247:
                        option, run = 'Scan QR', False
                    elif 313 <= x <= 337:
                        option, run = 'Profile', False
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
    def wishList(self):
        run, tempx, tempy = True, 0, 0
        while run:
            self.screen.fill('#F5F5F5')
            font = pygame.font.SysFont('voyager', 35)
            cfont = pygame.font.SysFont('voyager', 25)
            self.screen.blit(font.render('Wish List', True, '#222222'), (10, 15))
            notification = pygame.image.load('new assets/main/notification.png')
            self.screen.blit(notification, (355, 15))
            pygame.draw.rect(self.screen, '#949494', (0, 585, 384, 680))
            arr = [('Donuts', 'Price: 270'), ('Hoodies (x7)', 'Price: 699'), ('Shoes', 'Price: 349'), ('Lipstick', 'Price: 254'), ('Mobiles', 'Price: 7999')]
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/'+arr[i][0]+'.png'), (30, 80+100*i))
                self.screen.blit(font.render(arr[i][0], True, '#222222'), (170, 95+100*i))
                self.screen.blit(cfont.render(arr[i][1], True, '#222222'), (170, 120+100*i))
                self.screen.blit(pygame.image.load('assets/main/cart.png'), (270, 122+100*i))
            arr = ['home', 'love', 'qr', 'user']
            for i in range(len(arr)):
                self.screen.blit(pygame.image.load('assets/main/'+arr[i]+'.png'), (43+90*i, 600))
            events = pygame.event.get()
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                tempx, tempy = x, y
                if 600 <= y <= 624:
                    if 133 <= x <= 157:
                        option, run = 'Wish List', False
                    elif 223 <= x <= 247:
                        option, run = 'Scan QR', False
                    elif 313 <= x <= 337:
                        option, run = 'Profile', False
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
        if option == 'Scan QR':
            self.scanQR()

        elif option == 'Profile':
            self.profile()
        elif option == 'Wish List':
            self.wishList()
    def wallet(self):
        pass
    def displayMap(self):
        run, tempx, tempy = True, 0, 0
        while run:
            self.screen.fill('#3C444B')
            for x in range(len(self.data[self.floor])):
                for y in range(len(self.data[self.floor][x])):
                    shop = self.data[self.floor][x][y]
                    shop = shop[:-4] if '-' in shop else shop
                    if shop != 'void':
                        image = pygame.image.load('new assets/'+shop+'/'+shop+'.png')
                        self.screen.blit(image, (37+120*y, 60+150*x))
            if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos() != (tempx, tempy):
                x, y = pygame.mouse.get_pos()
                tempx, tempy = x, y
                if 37 <= x <=587 and 60 <= y <= 560:
                    x, y = (y-60)//120, (x-37)//135
                    shop = self.data[self.floor][x][y]
                    print(shop)
                    self.viewShop(shop)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    run = False
            pygame.display.update()
    def viewShop(self, shop):
        data = json.load(open('data/properties.json'))
        floors = [floor for floor in data]
        data = 'data/'+floors[self.floor]+'/'+shop+'.json'
        data = json.load(open(data))
        products = [(product, data[product]['cost']) for product in data]
        run, tempx, tempy = True, 0, 0
        self.screen.fill('white')
        font = pygame.font.SysFont('voyager', 50)
        nfont = pygame.font.SysFont('voyager', 40)
        pfont = pygame.font.SysFont('voyager', 30)
        self.screen.blit(font.render(shop, True, '#222222'), (40, 40))
        for i in range(len(products)):
            image = pygame.image.load('assets/'+shop+'/'+products[i][0]+'.png')
            self.screen.blit(image, (40, 125+120*i))
            self.screen.blit(nfont.render(products[i][0], True, '#222222'), (180, 135+120*i))
            self.screen.blit(pfont.render('Price: '+str(products[i][1]), True, '#222222'), (180, 170+120*i))
        pygame.display.update()    

App()
