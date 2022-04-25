import pygame
from src.game import Game
from src.users import Users
# import consts

# main game loop
def main():
    pygame.init()
    pygame.display.set_caption('Capitalist 2.0')
    pygame.font.init()
    Users()
    print("Enter your nickname: ")
    nick = str(input())
    game = Game(nick)
    clock = pygame.time.Clock()
    while game.run:
        game.process_events()
        clock.tick(60)
    pygame.quit()


main()
