import pygame as pygame

pygame.init()
LEFT = 42
MIDDLE = 540
RIGHT = 1030
fh = 100
sh = 250
th = 400
mh = 300
sr = 35
br = 145
din = 10
sd = 37
bd = 177
arp = 200
itp = 50
dp = 100
dmp = 600
ep = 400
sp = 300
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
WIDTH = 1080
HEIGHT = 720
mainfont = 19
sleep = 0.1
LIGHT = (173, 216, 230)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (11, 11, 69)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
OLIVE = (128, 128, 0)
LIGHT_OLIVE = (156, 175, 136)
ORANGE = (255, 131, 0)
LIGHT_ORANGE = (252, 210, 153)
LIME = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
LIGHT_RED = (255, 204, 203)
# sourceFileDir = os.path.dirname(os.path.abspath(__file__))
ARMY = pygame.transform.scale(pygame.image.load('images/army2.png'), (80, 80))
USA = pygame.transform.scale(pygame.image.load('images/usa.png'), (300, 300))
TECH = pygame.transform.scale(pygame.image.load('images/tech.png'), (80, 80))
DOLLAR = pygame.transform.scale(pygame.image.load('images/dollar.png'), (80, 80))
TESLA = pygame.transform.scale(pygame.image.load('images/tesla.png'), (80, 80))
SANC = pygame.transform.scale(pygame.image.load('images/sanc.png'), (80, 80))
DEMO = pygame.transform.scale(pygame.image.load('images/nato.png'), (80, 80))
BG = pygame.transform.scale(pygame.image.load('images/usabg.png'), (1080, 720))
Asound = pygame.mixer.Sound('sounds/army.wav')
Csound = pygame.mixer.Sound('sounds/click.wav')
Dsound = pygame.mixer.Sound('sounds/dollar.wav')
Nsound = pygame.mixer.Sound('sounds/nato.wav')
Jsound = pygame.mixer.Sound('sounds/sanction.wav')
Tsound = pygame.mixer.Sound('sounds/tesla.wav')
sounds_1 = [Csound, Dsound, Csound]
sounds_2 = [Asound, Nsound, Jsound]
autech = 0
autodollar = 0
autotesla = 0
Capitalist = 0
a = 0
b = 0
c = 0
d = 0
e = 0
score = 0
income = 0
FPS = 30
# # #
b1 = 1.2
b2 = 2
b3 = 5
ob1 = 4
ob2 = 7
ob3 = 10


i1 = 0.5
oi1 = 1.5
i2 = 2
oi2 = 2
i3 = 5
oi3 = 3
ins = [i1, i2, i3]
ovs = [oi1, oi2, oi3]
