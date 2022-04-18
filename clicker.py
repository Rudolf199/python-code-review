from constants import *

pygame.init()
pygame.font.init()
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


def draw(Type, text, y, color, money):
    global a, b, c, d, e
    if money is True:
        a = 42
        b = 1
        c = 90
        d = 95
        e = 98
    else:
        a = 1030
        b = 990
        c = 720
        d = 725
        e = 728
    pygame.draw.circle(win, color, (a, y), 40, 1)
    win.blit(Type, (b, y - 40))
    pygame.draw.rect(win, color, [c, y - 15, 270, 30])
    pygame.draw.rect(win, BLACK, [d, y - 10, 260, 20])
    txt = font.render(text, True, WHITE)
    win.blit(txt, (e, y - 15))


def main():
    click = 1
    cost1 = 50
    cost2 = 100
    cost3 = 150
    cost4 = 200
    cost5 = 250
    cost6 = 300
    global score, autech, autodollar, autotesla, income, Capitalist
    win.blit(BG, (0, 0))
    win.blit(USA, (360, 100))
    run = True
    while run:
        print("score", score)
        if run:
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Tsound.play()
                    score += click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1 = pygame.mouse.get_pos()[0]
                y1 = pygame.mouse.get_pos()[1]
                if x1 >= 395 and x1 <= 700 and y1 >= 200 and y1 <= 365:
                    Tsound.play()
                    score += click
                if x1 >= 2 and x1 <= 42 and y1 >= 60 and y1 <= 140:
                    print(x1, y1)
                    if score >= cost1:
                        Csound.play()
                        score -= cost1
                        cost1 *= 1.5
                        autech += 0.5
                        cost1 = round(cost1, 0)

                if x1 >= 2 and x1 <= 42 and y1 >= 210 and y1 <= 290:
                    print(x1, y1)
                    if score >= cost2:
                        Dsound.play()
                        score -= cost2
                        cost2 *= 2
                        autodollar += 2
                        cost2 = round(cost2, 0)
                if x1 >= 2 and x1 <= 42 and y1 >= 360 and y1 <= 440:
                    print(x1, y1)
                    if score >= cost3:
                        Csound.play()
                        score -= cost3
                        cost3 *= 3
                        autotesla += 5
                        cost3 = round(cost3, 0)
                if x1 >= 990 and x1 <= 1070 and y1 >= 60 and y1 <= 140:
                    print(x1, y1)
                    if score >= cost4:
                        Asound.play()
                        score -= cost4
                        cost4 *= 4
                        click *= 1.2
                        cost4 = round(cost4, 0)
                if x1 >= 990 and x1 <= 1070 and y1 >= 210 and y1 <= 290:
                    print(x1, y1)
                    if score >= cost5:
                        Jsound.play()
                        score -= cost5
                        cost5 *= 7
                        click *= 2
                        cost5 = round(cost5, 0)
                if x1 >= 990 and x1 <= 1070 and y1 >= 360 and y1 <= 440:
                    print(x1, y1)
                    if score >= cost6:
                        Nsound.play()
                        score -= cost6
                        cost6 *= 10
                        click *= 5
                        cost6 = round(cost6, 0)
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
        draw(TECH, "Invest in IT " + '(' + str(f'{cost1:.2f}') + " $" + ')', 100, BLUE, True)
        draw(DOLLAR, "Dollar expansion " + '(' + str(f'{cost2:.2f}') + " $" + ')', 250, GREEN, True)
        draw(TESLA, "Electric cars " + '(' + str(f'{cost3:.2f}') + " $" + ')', 400, GREY, True)
        draw(ARMY, "Army " + '(' + str(f'{cost4:.2f}') + " $" + ')', 100, RED, False)
        draw(SANC, "Sanctions " + '(' + str(f'{cost5:.2f}') + " $" + ')', 250, OLIVE, False)
        draw(DEMO, "Democracy " + '(' + str(f'{cost6:.2f}') + " $" + ')', 400, WHITE, False)
        drawtext("Money " + str(f'{score:.2f}') + " $", WHITE, GREEN, 400, 600, 30)
        drawtext("Income " + str(f'{income:.2f}') + " $", WHITE, BLUE, 800, 600, 30)
        drawtext("Working power " + str(f'{click:.2f}') + " $", WHITE, LIGHT, 800, 670, 30)
        drawtext("Capitalism LVL " + str(f'{Capitalist}'), WHITE, BLACK, 400, 670, 30)
        drawtext("Click or press Space to work", BLUE, WHITE, 500, 500, 30)
        pygame.display.update()
    pygame.quit()


main()

