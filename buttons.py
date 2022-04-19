import pygame
from constants import USA, WHITE, GREY, RED, TESLA, BLUE, BLACK, DOLLAR, ORANGE, ARMY
font = pygame.font.SysFont("comicsans", 20)

class Button:

    def __init__(self, picture, x, y, radius, color1, color2, deltax, deltay, dinamic):
        self.picture = picture
        self.x = x
        self.y = y
        self.radius = radius
        self.pressed = False
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.deltax = deltax
        self.deltay = deltay
        self.dinamic = dinamic + deltay

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.dinamic))
        self.clicked()

    def clicked(self):
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    print("pressed")
                    self.pressed = False
        else:
            self.color = self.color1


class Work(Button):

    def clicked(self):
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print("pressed 1")
                    self.pressed = False
        elif self.pressed is True:
            print("pressed 1")
            self.pressed = False
        else:
            self.color = self.color1


class AutoMoney(Button):

    def __init__(self, picture, x, y, radius, color1, color2, deltax, deltay, dinamic, text, cost):
        self.picture = picture
        self.x = x # координаты центров кругов
        self.y = y
        self.radius = radius
        self.pressed = False
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.deltax = deltax
        self.deltay = deltay
        self.dinamic = dinamic + deltay
        self.cost = cost
        self.text = text
        self.buy = False

    def draw(self, win, price):

        txt = font.render(self.text + '(' + str(f'{price:.2f}') + " $" + ')', True, ORANGE)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(win, self.color,
                         [self.x + self.radius + 20, self.y - self.radius,   txt.get_width() + 15, txt.get_height() + 20])
        pygame.draw.rect(win, BLACK,
                         [self.x + self.radius + 25, self.y - self.radius + 5, txt.get_width() + 7, txt.get_height() + 10])
        win.blit(txt, (self.x + self.radius + 30, self.y - 30))
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.dinamic))
        self.clicked()

    def clicked(self):
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0] and self.buy:
                self.pressed = True
            else:
                if self.pressed is True:
                    print("pressed")
                    self.pressed = False
        else:
            self.color = self.color1

class Upgrade(AutoMoney):

    def draw(self, win, price):

        txt = font.render(self.text + '(' + str(f'{price:.2f}') + " $" + ')', True, ORANGE)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(win, self.color,
                         [self.x - self.radius - 35 - txt.get_width(), self.y - self.radius, txt.get_width() + 15, txt.get_height() + 20])
        pygame.draw.rect(win, BLACK,
                         [self.x - self.radius - 30 - txt.get_width(), self.y - self.radius + 5, txt.get_width() + 7, txt.get_height() + 10])
        win.blit(txt, (self.x - self.radius - 30 - txt.get_width(), self.y - 30))
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - 1.3 * self.deltax, self.y - self.dinamic))
        self.clicked()

