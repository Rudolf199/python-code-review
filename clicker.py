from constants import *
from buttons import Work, AutoMoney, Upgrade
from saver import Saver
import os


pygame.init()
pygame.font.init()
print("Enter your nickname: ")
nick = str(input())
save = Saver(".save", "users", nick)
print(os.path.dirname("users"))
win = pygame.display.set_mode([1080, 720])
pygame.display.set_caption('Capitalist 1.0')
font = pygame.font.SysFont("comicsans", 19)
clock = pygame.time.Clock()



def drawtext(text, textcolor, rectcolor, x, y, fsize):
    font = pygame.font.SysFont('comicsans', fsize)
    text = font.render(text, True, textcolor, rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)


def autominer():
    global score
    global autech, autodollar, autotesla, income
    time.sleep(0.1)
    income = autech + autodollar + autotesla
    score = score + income


Tesla = AutoMoney(TESLA, 42, 400, 35, WHITE, LIGHT, 35, 37, 10, "Elecric cars ", 400)
Cookie = Work(USA, 540, 300, 145, LIME, DARK_GREEN, 145, 177, 10)
Army = Upgrade(ARMY, 1030, 100, 35, OLIVE, LIGHT_OLIVE, 35, 37, 10, "Army sales ", 200)
Tech = AutoMoney(TECH, 42, 100, 35, ORANGE, LIGHT_ORANGE, 35, 37, 10, "Invest in IT ", 50)
Dollar = AutoMoney(DOLLAR, 42, 250, 35, LIGHT, GREEN, 35, 37, 10, "Dollar expansion", 100)
Nato = Upgrade(DEMO, 1030, 250, 35, DARK_BLUE, BLUE, 35, 37, 10, "Democracy ", 600)
Sanction = Upgrade(SANC, 1030, 400, 35, OLIVE, LIGHT_RED, 35, 37, 10, "Sanctions ", 300)


def main():
    # click = 1
    global score, autech, autodollar, autotesla, income, Capitalist
    income, autech, autodollar, autotesla, click, Capitalist, \
    score = save.load_game_data([nick + "income", nick + "autech", nick + "autodollar", nick + "autotesla", nick + "click", nick + "LVL", nick + "score"],
                                                                                          [0, 0, 0, 0, 1, 0, 0])
    print(income, click, Capitalist, score)
    # тут будет анимация
    run = True
    while run:
        # print("score", score)
        if run:
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([income, autech, autodollar, autotesla, click, Capitalist, score],
                                    [nick + "income", nick + "autech", nick + "autodollar", nick + "autotesla", nick + "click", nick + "LVL", nick + "score"])
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Tsound.play()
                    Cookie.pressed = True
                    score += click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1 = pygame.mouse.get_pos()[0]
                y1 = pygame.mouse.get_pos()[1]
                if x1 >= Cookie.x - Cookie.radius and x1 <= Cookie.x + Cookie.radius and y1 >= Cookie.y - Cookie.radius and y1 <= Cookie.y + Cookie.radius:
                    Tsound.play()
                    score += click
                if x1 >= Tech.x - Tech.radius and x1 <= Tech.x + Tech.radius and y1 >= Tech.y - Tech.radius and y1 <= Tech.y + Tech.radius:
                    #print(x1, y1)
                    if score >= Tech.cost:
                        Csound.play()
                        Tech.buy = True
                        score -= Tech.cost
                        Tech.cost *= 1.5
                        autech += 0.5
                        Tech.cost = round(Tech.cost, 0)
                    else:
                        Tech.buy = False
                if x1 >= Dollar.x - Dollar.radius and x1 <= Dollar.x + Dollar.radius and y1 >= Dollar.y - Dollar.radius and y1 <= Dollar.y + Dollar.radius:
                    # print(x1, y1)
                    if score >= Dollar.cost:
                        Dsound.play()
                        Dollar.buy = True
                        score -= Dollar.cost
                        Dollar.cost *= 2
                        autodollar += 2
                        Dollar.cost = round(Dollar.cost, 0)
                    else:
                        Dollar.buy = False
                if x1 >= Tesla.x - Tesla.radius and x1 <= Tesla.x + Tesla.radius and y1 >= Tesla.y - Tesla.radius and y1 <= Tesla.y + Tesla.radius:
                    # print(x1, y1)
                    if score >= Tesla.cost:
                        Csound.play()
                        Tesla.buy = True
                        score -= Tesla.cost
                        Tesla.cost *= 3
                        autotesla += 5
                        Tesla.cost = round(Tesla.cost, 0)
                    else:
                        Tesla.buy = False
                if x1 >= Army.x - Army.radius and x1 <= Army.x + Army.radius and y1 >= Army.y - Army.radius and y1 <= Army.y + Army.radius:
                    # print(x1, y1)
                    if score >= Army.cost:
                        Asound.play()
                        Army.buy = True
                        score -= Army.cost
                        Army.cost *= 4
                        click *= 1.2
                        Army.cost = round(Army.cost, 0)
                    else:
                        Army.buy = False
                if x1 >= Nato.x - Nato.radius and x1 <= Nato.x + Nato.radius and y1 >= Nato.y - Nato.radius and y1 <= Nato.y + Nato.radius:
                    # print(x1, y1)
                    if score >= Nato.cost:
                        Nsound.play()
                        Nato.buy = True
                        score -= Nato.cost
                        Nato.cost *= 7
                        click *= 2
                        Nato.cost = round(Nato.cost, 0)
                    else:
                        Nato.buy = False
                if x1 >= Sanction.x - Sanction.radius and x1 <= Sanction.x + Sanction.radius and y1 >= Sanction.y - Sanction.radius and y1 <= Sanction.y + Sanction.radius:
                    # print(x1, y1)
                    if score >= Sanction.cost:
                        Jsound.play()
                        Sanction.buy = True
                        score -= Sanction.cost
                        Sanction.cost *= 10
                        click *= 5
                        Sanction.cost = round(Sanction.cost, 0)
                    else:
                        Sanction.buy = False
            if income > 10:
                if income > 100:
                    if income > 1000:
                        if income > 10000:
                            if income > 1000000:
                                Capitalist = 5
                            Capitalist = 4
                        Capitalist = 3
                    Capitalist = 2
                Capitalist = 1
            if score >= 1000000000000000000000000000 and Capitalist >= 5:
                drawtext("America is proud of you!!!", WHITE, RED, 400, 200, 50)
                pygame.display.update()
        win.blit(BG, (0, 0))
        Cookie.draw(win)
        Dollar.draw(win, Dollar.cost)
        Tesla.draw(win, Tesla.cost)
        Army.draw(win, Army.cost)
        Tech.draw(win, Tech.cost)
        Nato.draw(win, Nato.cost)
        Sanction.draw(win, Sanction.cost)
        drawtext("Money " + str(f'{score:.2f}') + " $", WHITE, GREEN, 400, 600, 30)
        drawtext("Income " + str(f'{income:.2f}') + " $", WHITE, BLUE, 800, 600, 30)
        drawtext("Working power " + str(f'{click:.2f}') + " $", WHITE, LIGHT, 800, 670, 30)
        drawtext("Capitalism LVL " + str(f'{Capitalist}'), WHITE, BLACK, 400, 670, 30)
        drawtext("Click or press Space to work", BLUE, WHITE, 500, 500, 30)
        drawtext("Player " + nick, GREY, WHITE, 800, 20, 15)
        pygame.display.update()
    pygame.quit()


main()
