import pickle
import os


class Saver:
    # class is for saving game data
    def __init__(self, file_ex, folder, nick):
        # file extension, folder where its gonna save, and nickname, as subdir name
        self.ex = file_ex
        self.folder = folder
        self.nick = nick

    def save_data(self, data, name):
        # saving single data type, in single file
        # print(self.folder)
        # os.makedirs(self.folder, exist_ok=True)
        # self.folder.mkdir()
        os.makedirs(f"{self.folder}/{self.nick}", exist_ok=True)
        # print(self.nick)
        # self.nick.mkdir()
        data_file = open(f"{self.folder}/{self.nick}/{name}{self.ex}", "wb")
        pickle.dump(data, data_file)

    def load_data(self, name):
        # loading single data type, from a single file
        data_file = open(f"{self.folder}/{self.nick}/{name}{self.ex}", "rb")
        data = pickle.load(data_file)
        return data

    def check_for_file(self, name):
        # checks if file exists
        return os.path.exists(f"{self.folder}/{self.nick}/{name}{self.ex}")

    def load_game_data(self, files, default_data):
        # loads all data from all files of players subdirectory
        variables = []
        for index, file in enumerate(files):
            if self.check_for_file(file):
                variables.append(self.load_data(file))
            else:
                variables.append(default_data[index])
        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]

    def save_game_data(self, data_to_save, file_names):
        # saves all progress of player in his named subdirectory
        for index, file in enumerate(data_to_save):
            self.save_data(file, file_names[index])
