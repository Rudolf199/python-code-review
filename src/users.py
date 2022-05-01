import pickle
import os


class Users:
    # class users, printing users list before the game
    def __init__(self):
        # checking if users directory exists, and printing if it does, not to make a error
        self.path = os.path.exists("./users")
        if self.path:
            # if exists
            self.userlist = os.listdir('users')
            # print(userlist)
            for user in self.userlist:
                # for each user from userlist (users are represented as subdirs in "users"
                print(user)
                print("Army: ", pickle.load(open(f"users/{user}/{user}Army.txt", "rb")))
                print("AutoIT: ", pickle.load(open(f"users/{user}/{user}autech.txt", "rb")))
                print("AutoDollar: ", pickle.load(open(f"users/{user}/{user}autodollar.txt", "rb")))
                print("AutoTesla: ", pickle.load(open(f"users/{user}/{user}autotesla.txt", "rb")))
                print("Click: ", pickle.load(open(f"users/{user}/{user}click.txt", "rb")))
                print("Dollar: ", pickle.load(open(f"users/{user}/{user}Dollar.txt", "rb")))
                print("Income: ", pickle.load(open(f"users/{user}/{user}income.txt", "rb")))
                print("LVL: ", pickle.load(open(f"users/{user}/{user}LVL.txt", "rb")))
                print("Nato: ", pickle.load(open(f"users/{user}/{user}Nato.txt", "rb")))
                print("Sanction: ", pickle.load(open(f"users/{user}/{user}Sanction.txt", "rb")))
                print("Money: ", pickle.load(open(f"users/{user}/{user}score.txt", "rb")))
                print("Tech: ", pickle.load(open(f"users/{user}/{user}Tech.txt", "rb")))
                print("Tesla: ", pickle.load(open(f"users/{user}/{user}Tesla.txt", "rb")))
                print("###########\n")
                # printing save data