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
        self.win = pygame.display.set_mode([consts.WIDTH, consts.HEIGHT])
        self.Army = Upgrade(consts.ARMY, consts.RIGHT, consts.fh, consts.sr, consts.OLIVE,
                            consts.LIGHT_OLIVE, consts.sr, consts.sd, consts.din, "Army sales ", consts.arp,
                            consts.Asound, consts.b1, consts.ob1)
        self.Tech = AutoMoney(consts.TECH, consts.LEFT, consts.fh, consts.sr,
                              consts.ORANGE, consts.LIGHT_ORANGE, consts.sr, consts.sd, consts.din, "Invest in IT ",
                              consts.itp, consts.Tsound, consts.i1, consts.oi1)
        self.Dollar = AutoMoney(consts.DOLLAR, consts.LEFT, consts.sh, consts.sr,
                                consts.LIGHT, consts.GREEN, consts.sr, consts.sd,
                                consts.din, "Dollar expansion", consts.dp, consts.Dsound, consts.i2, consts.oi2)
        self.Nato = Upgrade(consts.DEMO, consts.RIGHT, consts.sh,
                            consts.sr, consts.DARK_BLUE, consts.BLUE, consts.sr, consts.sd, consts.din, "Democracy ",
                            consts.dmp, consts.Nsound, consts.b3, consts.ob3)
        self.Tesla = AutoMoney(consts.TESLA, consts.LEFT, consts.th, consts.sr, consts.WHITE,
                               consts.LIGHT, consts.sr, consts.sd, consts.din, "Elecric cars ", consts.ep,
                               consts.Tsound, consts.i3, consts.oi3)
        self.Sanction = Upgrade(consts.SANC, consts.RIGHT, consts.th, consts.sr, consts.OLIVE,
                                consts.LIGHT_RED, consts.sr, consts.sd, consts.din, "Sanctions ", consts.sp,
                                consts.Jsound, consts.b2, consts.ob2)
        self.Cookie = Work(consts.USA, consts.MIDDLE, consts.mh, consts.br,
                           consts.LIME, consts.DARK_GREEN, consts.br, consts.bd, consts.din)
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
        self.Nato.cost = self.player.load_game_data([self.nick + "Nato"], [consts.dmp])
        self.Tesla.cost = self.player.load_game_data([self.nick + "Tesla"], [consts.ep])
        self.Tech.cost = self.player.load_game_data([self.nick + "Tech"], [consts.itp])
        self.Army.cost = self.player.load_game_data([self.nick + "Army"], [consts.arp])
        self.Dollar.cost = self.player.load_game_data([self.nick + "Dollar"], [consts.dp])
        self.Sanction.cost = self.player.load_game_data([self.nick + "Sanction"], [consts.sp])

    def savegame(self):
        # this method saves progress of player, in files of following style nick + "data"
        self.player.save_game_data([self.income, self.autech, self.autodollar, self.autotesla, self.click,
                                    self.Capitalist, self.score,
                                    self.Nato.cost, self.Tesla.cost,
                                    self.Army.cost, self.Tech.cost, self.Sanction.cost, self.Dollar.cost],
                                   [self.nick + "income", self.nick + "autech", self.nick + "autodollar",
                                    self.nick + "autotesla",
                                    self.nick + "click", self.nick + "LVL", self.nick + "score", self.nick + "Nato",
                                    self.nick + "Tesla", self.nick + "Army",
                                    self.nick + "Tech", self.nick + "Sanction", self.nick + "Dollar"])

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
                        consts.Tsound.play()
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
                        consts.Tsound.play()
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
                            self.Capitalist = 5
                        self.Capitalist = 4
                    self.Capitalist = 3
                self.Capitalist = 2
            self.Capitalist = 1
        if self.score >= consts.score and self.Capitalist >= consts.maxlvl:
            self.drawtext("America is proud of you!!!", consts.WHITE, consts.RED,
                          consts.vicx, consts.vicy, consts.vicz)
            pygame.display.update()

    def screen_draw(self):
        # display drawing
        # print("method score", self.score)
        self.win.blit(consts.BG, (0, 0))
        self.Cookie.draw(self.win)
        self.Dollar.draw(self.win, self.Dollar.cost)
        self.Tesla.draw(self.win, self.Tesla.cost)
        self.Army.draw(self.win, self.Army.cost)
        self.Tech.draw(self.win, self.Tech.cost)
        self.Nato.draw(self.win, self.Nato.cost)
        self.Sanction.draw(self.win, self.Sanction.cost)
        self.drawtext("Money " + str(f'{self.score:.2f}') + " $", consts.WHITE, consts.GREEN,
                      consts.monx, consts.mony, consts.monz)
        self.drawtext("Income " + str(f'{self.income:.2f}') + " $", consts.WHITE,
                      consts.BLUE, consts.incx, consts.incy, consts.incz)
        self.drawtext("Working power " + str(f'{self.click:.2f}') + " $", consts.WHITE,
                      consts.LIGHT, consts.worx, consts.wory, consts.worz)
        self.drawtext("Capitalism LVL " + str(f'{self.Capitalist}'), consts.WHITE,
                      consts.BLACK, consts.capx, consts.capy, consts.capz)
        self.drawtext("Click or press Space to work", consts.BLUE, consts.WHITE,
                      consts.cx, consts.cy, consts.cz)
        self.drawtext("Player " + self.nick, consts.GREY, consts.WHITE,
                      consts.px, consts.py, consts.pz)
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
