import pygame
import consts
from src.buttons import Work, AutoMoney, Upgrade
from src.saver import Saver
import time


class Game:
    # This class represents an instance of the game
    def __init__(self, nick):
        # initializing all data it needs to run the game
        self.font = pygame.font.SysFont("comicsans", consts.mainfont)
        self.win = pygame.display.set_mode([consts.width, consts.height])
        self.Army = Upgrade(consts.army, consts.right, consts.first_height, consts.small_radius,
                            consts.olive, consts.light_olive, consts.small_radius, consts.small_delta,
                            consts.din, "Army sales ", consts.army_price, consts.asound,
                            consts.b1, consts.ob1)
        self.Tech = AutoMoney(consts.tech, consts.left, consts.first_height, consts.small_radius,
                              consts.orange, consts.light_orange, consts.small_radius,
                              consts.small_delta, consts.din, "Invest in IT ", consts.it_price, consts.tsound,
                              consts.i1, consts.oi1)
        self.Dollar = AutoMoney(consts.dollar, consts.left, consts.second_height, consts.small_radius,
                                consts.light, consts.green, consts.small_radius, consts.small_delta,
                                consts.din, "Dollar expansion", consts.dollar_price, consts.dsound,
                                consts.i2, consts.oi2)
        self.Nato = Upgrade(consts.demo, consts.right, consts.second_height, consts.small_radius,
                            consts.dark_blue, consts.blue, consts.small_radius, consts.small_delta,
                            consts.din, "Democracy ", consts.democracy_price, consts.nsound,
                            consts.b3, consts.ob3)
        self.Tesla = AutoMoney(consts.tesla, consts.left, consts.third_height, consts.small_radius,
                               consts.white, consts.light, consts.small_radius, consts.small_delta,
                               consts.din, "Elecric cars ", consts.electro_price, consts.tsound,
                               consts.i3, consts.oi3)
        self.Sanction = Upgrade(consts.sanc, consts.right, consts.third_height, consts.small_radius,
                                consts.olive, consts.light_red, consts.small_radius, consts.small_delta,
                                consts.din, "Sanctions ", consts.sanction_price, consts.jsound,
                                consts.b2, consts.ob2)
        self.Cookie = Work(consts.usa, consts.middle, consts.middle_height, consts.big_radius,
                           consts.lime, consts.dark_green, consts.big_radius, consts.big_delta,
                           consts.din)
        # Create the player
        self.player = Saver(".txt", "users", nick)
        self.run = True
        self.nick = nick
        self.autech = self.player.load_game_data([self.nick + "autech"], [0])
        self.autodollar = self.player.load_game_data([self.nick + "autodollar"], [0])
        self.autotesla = self.player.load_game_data([self.nick + "autotesla"], [0])
        self.income = self.player.load_game_data([self.nick + "income"], [0])
        self.click = self.player.load_game_data([self.nick + "click"], [1])
        self.Capitalist = self.player.load_game_data([self.nick + "LVL"], [0])
        self.score = self.player.load_game_data([self.nick + "score"], [0])
        self.Nato.cost = self.player.load_game_data([self.nick + "Nato"], [consts.democracy_price])
        self.Tesla.cost = self.player.load_game_data([self.nick + "Tesla"], [consts.electro_price])
        self.Tech.cost = self.player.load_game_data([self.nick + "Tech"], [consts.it_price])
        self.Army.cost = self.player.load_game_data([self.nick + "Army"], [consts.army_price])
        self.Dollar.cost = self.player.load_game_data([self.nick + "Dollar"], [consts.dollar_price])
        self.Sanction.cost = self.player.load_game_data([self.nick + "Sanction"], [consts.sanction_price])

    def savegame(self):
        # this method saves progress of player, in files of following style nick + "data"
        self.player.save_game_data([self.income, self.autech, self.autodollar, self.autotesla, self.click,
                                    self.Capitalist, self.score, self.Nato.cost, self.Tesla.cost,
                                    self.Army.cost, self.Tech.cost, self.Sanction.cost, self.Dollar.cost],
                                   [self.nick + "income", self.nick + "autech", self.nick + "autodollar",
                                    self.nick + "autotesla", self.nick + "click", self.nick + "LVL", self.nick + "score",
                                    self.nick + "Nato", self.nick + "Tesla", self.nick + "Army", self.nick + "Tech",
                                    self.nick + "Sanction", self.nick + "Dollar"])

    def process_events(self):
        # game events loop
        while self.run:
            # print("score", score)
            if self.run:
                # runs collector while game is running, 0 if player hasn't bought anything
                self.autominer()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # if player leaves, game runs the save method
                    self.savegame()
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # main click, with sound effect
                        consts.tsound.play()
                        self.Cookie.pressed = True
                        self.score += self.click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # getting mouse pos x, y
                    x1 = pygame.mouse.get_pos()[0]
                    y1 = pygame.mouse.get_pos()[1]
                    '''
                    then in all if loops, checking where the mouse is clicked, if it is clicked in some of boosts areas
                    game checks if player is able to buy it, if he.she is, then click animation is played, 
                    price is changed, and the
                    boost begins working  
                    '''
                    if x1 >= self.Cookie.x - self.Cookie.radius and x1 <= self.Cookie.x + self.Cookie.radius and \
                            y1 >= self.Cookie.y - self.Cookie.radius and y1 <= self.Cookie.y + self.Cookie.radius:
                        consts.tsound.play()
                        self.score += self.click
                    self.autech, self.score = self.Tech.play(self.score, self.autech, x1, y1)
                    self.autotesla, self.score = self.Tesla.play(self.score, self.autotesla, x1, y1)
                    self.autodollar, self.score = self.Dollar.play(self.score, self.autodollar, x1, y1)
                    self.click, self.score = self.Army.play(self.score, self.click, x1, y1)
                    self.click, self.score = self.Nato.play(self.score, self.click, x1, y1)
                    self.click, self.score = self.Sanction.play(self.score, self.click, x1, y1)
                    self.income = self.autech + self.autodollar + self.autotesla
                self.capitalist()
            self.screen_draw()
        pygame.quit()

    def capitalist(self):
        if self.income > consts.income1:
            if self.income > consts.income2:
                if self.income > consts.income3:
                    if self.income > consts.income4:
                        if self.income > consts.income5:
                            self.Capitalist = consts.caplvl5
                        self.Capitalist = consts.caplvl4
                    self.Capitalist = consts.caplvl3
                self.Capitalist = consts.caplvl2
            self.Capitalist = consts.caplvl1
        if self.score >= consts.score and self.Capitalist >= consts.maxlvl:
            self.drawtext("America is proud of you!!!", consts.white, consts.red,
                          consts.vicx, consts.vicy, consts.vicz)
            pygame.display.update()

    def screen_draw(self):
        # display drawing
        # print("method score", self.score)
        self.win.blit(consts.bg, (0, 0))
        self.Cookie.draw(self.win)
        self.Dollar.draw(self.win, self.Dollar.cost)
        self.Tesla.draw(self.win, self.Tesla.cost)
        self.Army.draw(self.win, self.Army.cost)
        self.Tech.draw(self.win, self.Tech.cost)
        self.Nato.draw(self.win, self.Nato.cost)
        self.Sanction.draw(self.win, self.Sanction.cost)
        self.drawtext("Money " + str(f'{self.score:.2f}') + " $", consts.white,
                      consts.green, consts.monx, consts.mony, consts.monz)
        self.drawtext("Income " + str(f'{self.income:.2f}') + " $", consts.white,
                      consts.blue, consts.incx, consts.incy, consts.incz)
        self.drawtext("Working power " + str(f'{self.click:.2f}') + " $", consts.white,
                      consts.light, consts.worx, consts.wory, consts.worz)
        self.drawtext("Capitalism LVL " + str(f'{self.Capitalist}'), consts.white,
                      consts.black, consts.capx, consts.capy, consts.capz)
        self.drawtext("Click or press Space to work", consts.blue,
                      consts.white, consts.cx, consts.cy, consts.cz)
        self.drawtext("Player " + self.nick, consts.grey,
                      consts.white, consts.px, consts.py, consts.pz)
        pygame.display.update()

    def autominer(self):
        # autocollectors with sleep time, after which they increae the income with their value
        time.sleep(consts.sleep)
        self.income = self.autech + self.autodollar + self.autotesla
        self.score = self.score + self.income

    def drawtext(self, text, textcolor, rectcolor, x, y, fsize):
        # basic text drawing method, for nickname, income, etc
        font = pygame.font.SysFont('comicsans', fsize)
        text = font.render(text, True, textcolor, rectcolor)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.win.blit(text, textRect)
