import pygame
import consts
from src.buttons import Work, AutoMoney, Upgrade
from src.saver import Saver
import time


class Game:


    def __init__(self, nick):
        self.font = pygame.font.SysFont("comicsans", consts.mainfont)
        self.win = pygame.display.set_mode([consts.WIDTH, consts.HEIGHT])
        self.Army = Upgrade(consts.ARMY, consts.RIGHT, consts.fh, consts.sr, consts.OLIVE,
               consts.LIGHT_OLIVE, consts.sr, consts.sd, consts.din, "Army sales ", consts.arp)
        # global autech, autodollar, autotesla, income
        self.Tech = AutoMoney(consts.TECH, consts.LEFT, consts.fh, consts.sr,
                         consts.ORANGE, consts.LIGHT_ORANGE, consts.sr, consts.sd, consts.din, "Invest in IT ",
                         consts.itp)
        self.Dollar = AutoMoney(consts.DOLLAR, consts.LEFT, consts.sh, consts.sr,
                           consts.LIGHT, consts.GREEN, consts.sr, consts.sd, consts.din, "Dollar expansion", consts.dp)
        self.Nato = Upgrade(consts.DEMO, consts.RIGHT, consts.sh,
                       consts.sr, consts.DARK_BLUE, consts.BLUE, consts.sr, consts.sd, consts.din, "Democracy ",
                       consts.dmp)
        self.Tesla = AutoMoney(consts.TESLA, consts.LEFT, consts.th, consts.sr, consts.WHITE,
                          consts.LIGHT, consts.sr, consts.sd, consts.din, "Elecric cars ", consts.ep)
        self.Sanction = Upgrade(consts.SANC, consts.RIGHT, consts.th, consts.sr, consts.OLIVE,
                           consts.LIGHT_RED, consts.sr, consts.sd, consts.din, "Sanctions ", consts.sp)
        self.Cookie = Work(consts.USA, consts.MIDDLE, consts.mh, consts.br,
                      consts.LIME, consts.DARK_GREEN, consts.br, consts.bd, consts.din)
        self.game_over = False
        # Create the player
        self.player = Saver(".txt", "users", nick)
        self.run = True
        self.nick = nick
        self.autos = [self.Tech, self.Dollar, self.Tesla]
        self.boosts = [self.Army, self.Nato, self.Sanction]
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
        self.cols = [self.autech, self.autodollar, self.autotesla]
        self.income = self.autotesla + self.autech + self.autodollar

    def savegame(self):
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
        while self.run:
            # print("score", score)
            if self.run:
                self.autominer()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savegame()
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        consts.Tsound.play()
                        self.Cookie.pressed = True
                        self.score += self.click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x1 = pygame.mouse.get_pos()[0]
                    y1 = pygame.mouse.get_pos()[1]
                    if x1 >= self.Cookie.x - self.Cookie.radius and x1 <= self.Cookie.x + self.Cookie.radius and \
                            y1 >= self.Cookie.y - self.Cookie.radius and y1 <= self.Cookie.y + self.Cookie.radius:
                        consts.Tsound.play()
                        self.score += self.click
                    # for collector, a, o, c, s in self.autos, consts.ins, consts.ovs, colls, consts.sounds_1:
                    '''
                    for i in range(3):
                        if x1 >= self.autos[i].x - self.autos[i].radius and x1 <= self.autos[i].x + self.autos[i].radius and \
                                y1 >= self.autos[i].y - self.autos[i].radius and y1 <= self.autos[i].y + self.autos[i].radius:
                            # print(x1, y1)
                            if self.score >= self.autos[i].cost:
                                consts.sounds_1[i].play()
                                self.autos[i].buy = True
                                self.score -= self.autos[i].cost
                                self.autos[i].cost *= consts.ovs[i]
                                self.cols[i] += consts.ins[i]
                                self.income += consts.ins[i]
                                print(self.cols[i])
                                self.autos[i].cost = round(self.autos[i].cost, 0)
                            else:
                                self.autos[i].buy = False
                    '''
                    if x1 >= self.Tech.x - self.Tech.radius and x1 <= self.Tech.x + self.Tech.radius and \
                            y1 >= self.Tech.y - self.Tech.radius and y1 <= self.Tech.y + self.Tech.radius:
                        # print(x1, y1)
                        if self.score >= self.Tech.cost:
                            consts.Csound.play()
                            self.Tech.buy = True
                            self.score -= self.Tech.cost
                            self.Tech.cost *= 1.5
                            self.autech += 0.5
                            self.Tech.cost = round(self.Tech.cost, 0)
                        else:
                            self.Tech.buy = False
                    if x1 >= self.Dollar.x - self.Dollar.radius and x1 <= self.Dollar.x + self.Dollar.radius \
                            and y1 >= self.Dollar.y - self.Dollar.radius and y1 <= self.Dollar.y + self.Dollar.radius:
                        # print(x1, y1)
                        if self.score >= self.Dollar.cost:
                            consts.Dsound.play()
                            self.Dollar.buy = True
                            self.score -= self.Dollar.cost
                            self.Dollar.cost *= 2
                            self.autodollar += 2
                            self.Dollar.cost = round(self.Dollar.cost, 0)
                        else:
                            self.Dollar.buy = False
                    if x1 >= self.Tesla.x - self.Tesla.radius and x1 <= self.Tesla.x + self.Tesla.radius and y1 >= self.Tesla.y - self.Tesla.radius and\
                            y1 <= self.Tesla.y + self.Tesla.radius:
                        # print(x1, y1)
                        if self.score >= self.Tesla.cost:
                            consts.Csound.play()
                            self.Tesla.buy = True
                            self.score -= self.Tesla.cost
                            self.Tesla.cost *= 3
                            self.autotesla += 5
                            self.Tesla.cost = round(self.Tesla.cost, 0)
                        else:
                            self.Tesla.buy = False
                    if x1 >= self.Army.x - self.Army.radius and x1 <= self.Army.x + self.Army.radius and y1 >= self.Army.y - self.Army.radius \
                            and y1 <= self.Army.y + self.Army.radius:
                        # print(x1, y1)
                        if self.score >= self.Army.cost:
                            consts.Asound.play()
                            self.Army.buy = True
                            self.score -= self.Army.cost
                            self.Army.cost *= 4
                            self.click *= 1.2
                            self.Army.cost = round(self.Army.cost, 0)
                        else:
                            self.Army.buy = False
                    if x1 >= self.Nato.x - self.Nato.radius and x1 <= self.Nato.x + self.Nato.radius and y1 >= self.Nato.y - self.Nato.radius \
                            and y1 <= self.Nato.y + self.Nato.radius:
                        # print(x1, y1)
                        if self.score >= self.Nato.cost:
                            consts.Nsound.play()
                            self.Nato.buy = True
                            self.score -= self.Nato.cost
                            self.Nato.cost *= 7
                            self.click *= 2
                            self.Nato.cost = round(self.Nato.cost, 0)
                        else:
                            self.Nato.buy = False
                    if x1 >= self.Sanction.x - self.Sanction.radius and x1 <= self.Sanction.x + self.Sanction.radius \
                            and y1 >= self.Sanction.y - self.Sanction.radius and y1 <= self.Sanction.y + self.Sanction.radius:
                        # print(x1, y1)
                        if self.score >= self.Sanction.cost:
                            consts.Jsound.play()
                            self.Sanction.buy = True
                            self.score -= self.Sanction.cost
                            self.Sanction.cost *= 10
                            self.click *= 5
                            self.Sanction.cost = round(self.Sanction.cost, 0)
                        else:
                            self.Sanction.buy = False
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
                    self.drawtext("America is proud of you!!!", consts.WHITE, consts.RED, consts.vicx, consts.vicy, consts.vicz)
                    pygame.display.update()
            self.win.blit(consts.BG, (0, 0))
            self.Cookie.draw(self.win)
            self.Dollar.draw(self.win, self.Dollar.cost)
            self.Tesla.draw(self.win, self.Tesla.cost)
            self.Army.draw(self.win, self.Army.cost)
            self.Tech.draw(self.win, self.Tech.cost)
            self.Nato.draw(self.win, self.Nato.cost)
            self.Sanction.draw(self.win, self.Sanction.cost)
            self.drawtext("Money " + str(f'{self.score:.2f}') + " $", consts.WHITE, consts.GREEN, consts.monx, consts.mony, consts.monz)
            self.drawtext("Income " + str(f'{self.income:.2f}') + " $", consts.WHITE, consts.BLUE, consts.incx, consts.incy, consts.incz)
            self.drawtext("Working power " + str(f'{self.click:.2f}') + " $", consts.WHITE, consts.LIGHT, consts.worx, consts.wory, consts.worz)
            self.drawtext("Capitalism LVL " + str(f'{self.Capitalist}'), consts.WHITE, consts.BLACK, consts.capx, consts.capy, consts.capz)
            self.drawtext("Click or press Space to work", consts.BLUE, consts.WHITE, consts.cx, consts.cy, consts.cz)
            self.drawtext("Player " + self.nick, consts.GREY, consts.WHITE, consts.px, consts.py, consts.pz)
            pygame.display.update()
        pygame.quit()

    def autominer(self):
        time.sleep(consts.sleep)
        self.income = self.autech + self.autodollar + self.autotesla
        self.score = self.score + self.income

    def drawtext(self, text, textcolor, rectcolor, x, y, fsize):
        font = pygame.font.SysFont('comicsans', fsize)
        text = font.render(text, True, textcolor, rectcolor)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.win.blit(text, textRect)



