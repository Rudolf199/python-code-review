import pygame
import consts



class Button:
    # main button class, representing their common characteristics
    def __init__(self, picture, x, y, radius, color1, color2, deltax, deltay, dinamic):
        # initialization with their picture, coordinates, color, and the dinamic coordinates for moving ,
        # animation
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
        # drawing the button icon, and its "shadow"
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.dinamic))
        self.clicked()

    def clicked(self):
        # checking if mouse is clicked in the buttons area
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius \
           and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    # print("pressed")
                    self.pressed = False
        else:
            self.color = self.color1


class Work(Button):
    '''
    class of the main click button, "coockie", can also be pressed by space key, so the clicked method
    needs to be changed
    '''
    def clicked(self):
        # click animation method
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius \
           and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    # print("pressed 1")
                    self.pressed = False
        elif self.pressed is True:
            # print("pressed 1")
            self.pressed = False
        else:
            self.color = self.color1


class AutoMoney(Button):
    # autocollectors class, has additional initialization parameters, so some  methods are redefined
    def __init__(self, picture, x, y, radius, color1, color2, deltax,
                 deltay, dinamic, text, cost, sound, income, overprice):
        self.picture = picture
        self.x = x  # координаты центров кругов
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
        self.income = income
        self.sound = sound
        self.over = overprice

    def draw(self, win, price):
        # besides icon, it also needs a rectangle to be drawn on its right side, for its price representation
        txt = consts.font.render(self.text + '(' + str(f'{price:.2f}') + " $" + ')', True, consts.ORANGE)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(win, self.color,
                         [self.x + self.radius + consts.rect_delta_y1, self.y - self.radius, txt.get_width()
                          + consts.rect_delta_x2, txt.get_height() + consts.rect_delta_y1])
        pygame.draw.rect(win, consts.BLACK,
                         [self.x + self.radius + consts.rect_delta_y22, self.y - self.radius + consts.rect_delta,
                          txt.get_width() + consts.rect_delta_x22, txt.get_height() + consts.rect_delta_y2])
        win.blit(txt, (self.x + self.radius + consts.rect_delta_x11, self.y - consts.rect_delta_x11))
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.dinamic))
        self.clicked()

    def clicked(self):
        # this buttons can be clicked, if user has enough money to buy this boosts
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius \
           and n >= self.y - self.radius and n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0] and self.buy:
                self.pressed = True
            else:
                if self.pressed is True:
                    # print("pressed")
                    self.pressed = False
        else:
            self.color = self.color1

    def play(self, score, automoney, x, y):
        # button gameplay logic
        if x >= self.x - self.radius and x <= self.x + self.radius and \
                y >= self.y - self.radius and y <= self.y + self.radius:
            # print(x1, y1)
            if score >= self.cost:
                self.sound.play()
                self.buy = True
                score -= self.cost
                self.cost *= self.over
                automoney += self.income
                self.cost = round(self.cost, 0)
            else:
                self.buy = False
        return automoney, score


class Upgrade(AutoMoney):
    # class of click boosts, inherited clicking logic, and init method from Automoney class
    def draw(self, win, price):
        # they draw the price rectangle on its icons left side
        txt = consts.font.render(self.text + '(' + str(f'{price:.2f}') + " $" + ')', True, consts.ORANGE)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(win, self.color,
                         [self.x - self.radius - consts.rect_delta_x1 -
                          txt.get_width(), self.y - self.radius,
                          txt.get_width() + consts.rect_delta_x2,
                          txt.get_height() + consts.rect_delta_y1])
        pygame.draw.rect(win, consts.BLACK,
                         [self.x - self.radius - consts.rect_delta_x11 -
                          txt.get_width(), self.y - self.radius + consts.rect_delta,
                          txt.get_width() + consts.rect_delta_x22,
                          txt.get_height() + consts.rect_delta_y2])
        win.blit(txt, (self.x - self.radius - consts.rect_delta_x11 -
                       txt.get_width(), self.y - consts.rect_delta_x11))
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - consts.rect_corr * self.deltax, self.y - self.dinamic))
        self.clicked()

    def play(self, score, click, x, y):
        # button gameplay logic
        if x >= self.x - self.radius and x <= self.x + self.radius and \
                y >= self.y - self.radius and y <= self.y + self.radius:
            # print(x1, y1)
            if score >= self.cost:
                self.sound.play()
                self.buy = True
                score -= self.cost
                self.cost *= self.over
                click *= self.income
                self.cost = round(self.cost, 0)
            else:
                self.buy = False
        return click, score
