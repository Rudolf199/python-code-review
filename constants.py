import pygame
import time
pygame.init()

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
