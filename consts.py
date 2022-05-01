import pygame as pygame

pygame.init()
fsize = 20
font = pygame.font.SysFont("comicsans", fsize)
left = 42
middle = 540
right = 1030
first_height = 100
second_height = 250
third_height = 400
middle_height = 300
small_radius = 35
big_radius = 145
din = 10
small_delta = 37
big_delta = 177
army_price = 200
it_price = 50
dollar_price = 100
democracy_price = 600
electro_price = 400
sanction_price = 300
maxscore = 10000000000000
maxlvl = 5
income1 = 10
income2 = 100
income3 = 1000
income4 = 10000
income5 = 100000
vicx = 400
vicy = 200
vicz = 50
# # #
monx = 400
mony = 600
monz = 30
# # #
incx = 800
incy = 600
incz = 30
# # #
worx = 800
wory = 670
worz = 30
# # #
capx = 400
capy = 670
capz = 30
# # #
cx = 500
cy = 500
cz = 30
# # #
px = 800
py = 20
pz = 15
# # #
width = 1080
height = 720
mainfont = 19
sleep = 0.1
light = (173, 216, 230)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
dark_blue = (11, 11, 69)
grey = (128, 128, 128)
green = (0, 255, 0)
olive = (128, 128, 0)
light_olive = (156, 175, 136)
orange = (255, 131, 0)
light_orange = (252, 210, 153)
lime = (0, 255, 0)
dark_green = (0, 100, 0)
light_red = (255, 204, 203)
# sourceFileDir = os.path.dirname(os.path.abspath(__file__))
army = pygame.transform.scale(pygame.image.load('images/army2.png'), (80, 80))
usa = pygame.transform.scale(pygame.image.load('images/usa.png'), (300, 300))
tech = pygame.transform.scale(pygame.image.load('images/tech.png'), (80, 80))
dollar = pygame.transform.scale(pygame.image.load('images/dollar.png'), (80, 80))
tesla = pygame.transform.scale(pygame.image.load('images/tesla.png'), (80, 80))
sanc = pygame.transform.scale(pygame.image.load('images/sanc.png'), (80, 80))
demo = pygame.transform.scale(pygame.image.load('images/nato.png'), (80, 80))
bg = pygame.transform.scale(pygame.image.load('images/usabg.png'), (1080, 720))
asound = pygame.mixer.Sound('sounds/army.wav')
csound = pygame.mixer.Sound('sounds/click.wav')
dsound = pygame.mixer.Sound('sounds/dollar.wav')
nsound = pygame.mixer.Sound('sounds/nato.wav')
jsound = pygame.mixer.Sound('sounds/sanction.wav')
tsound = pygame.mixer.Sound('sounds/tesla.wav')
autech = 0
autodollar = 0
autotesla = 0
capitalist = 0
'''
a = 0
b = 0
c = 0
d = 0
e = 0
'''
score = 0
income = 0
FPS = 30
# # #
b1 = 1.2
b2 = 2
b3 = 5
ob1 = 4
ob2 = 7  # overprice boost 2
ob3 = 10
caplvl1 = 1
caplvl2 = 2
caplvl3 = 3
caplvl4 = 4
caplvl5 = 5

i1 = 0.5
oi1 = 1.5
i2 = 2
oi2 = 2  # overprice income 2
i3 = 5
oi3 = 3
rect_delta_x1 = 35
rect_delta_x2 = 15
rect_delta_y1 = 20
rect_delta_x11 = 30
rect_delta_x22 = 7
rect_delta = 5
rect_delta_y2 = 10
rect_delta_y22 = 25
rect_corr = 1.3
