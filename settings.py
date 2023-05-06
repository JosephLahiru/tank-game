import os, json
from constats import *


class Settings:
    def __init__(self):
        self.music = None
        self.sound = None
        self.player = None

        if os.path.isfile('settings.txt'):
            self.read()
        else:
            open('settings.txt', 'x')
            self.reset()
            self.save()

    def save(self):
        with open('settings.txt', 'w') as f:  # opens a file
            data = {'controls': self.player, 'sound': self.sound, 'music': self.music}
            json_data = json.dumps(data)
            f.write(json_data)

    def read(self):
        with open('settings.txt', 'r') as f:
            data = json.load(f)
            self.player = data['controls']
            self.music = data['music']
            self.sound = data['sound']
            self.player[1] = self.player['1']
            self.player[2] = self.player['2']
            self.player.pop('1')
            self.player.pop('2')

    def reset(self):
        self.player = {
            1: ['w', 's', 'a', 'd', 'space'],
            2: ['i', 'k', 'j', 'l', 'n']
        }

        self.sound = True
        self.music = True
