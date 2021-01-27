import pygame
import os, sys
import json


dEcryptKey = "Lun@F0rL1fe"

class Player:
    def __init__(self):
        self.townName = "Wicked"
        self.money = 0
        self.darkIron = 0
        self.level = 0
        self.progess = 0
        self.unlocks = []
        self.hasSave = False
        self.data = {}
        self.savePath = "./Data/Player/"

    def load_data(self):
        for dirPath, dirnames, filenames in os.walk(self.savePath):
            if len(filenames) > 0:
                print(filenames)
                return filenames


    def save_data(self):
        pass
