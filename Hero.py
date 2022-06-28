import pygame
import os


class My_Hero():

    def __init__(self):
        self.name = "Ваше величество"

        self.month = 1
        self.week = 1
        self.day = 1

        self.Hero_Level = 1
        self.Level_Up_Experience = 1000

        self.Move_limit = 20
        self.Mana = 5
        self.Gold = 0
        self.Wood = 0
        self.Mercury = 0
        self.Stone = 0
        self.Sulfur = 0
        self.Crystals = 0
        self.Jewelry = 0
        self.Experience = 0
        self.Magic_lvl = 0

        self.Attack = 1
        self.Defense = 1
        self.Magic = 1
        self.Knowledge = 1

        self.gold_mine = 0
        self.wood_mine = 0
        self.mercury_mine = 0
        self.crystal_mine = 0
        self.sulfure_mine = 0
        self.stone_mine = 0

        self.postroika_v_den = 1

        self.surf_strelka = pygame.image.load(os.path.join('Textures',"Hero.png"))
        self.sem_strelka = self.surf_strelka.get_rect(center=(500, 400))

    def pick_up_gold(self):
        self.Gold = self.Gold + 500
    def pick_up_wood(self):
        self.Wood = self.Wood + 5
    def pick_up_stone(self):
        self.Stone = self.Stone + 5
    def pick_up_mercury(self):
        self.Mercury = self.Mercury + 5
    def pick_up_sulfur(self):
        self.Sulfur = self.Sulfur + 5
    def pick_up_Jewelry(self):
        self.Jewelry = self.Jewelry + 5
    def pick_up_Crystal(self):
        self.Crystals = self.Crystals + 5

    def end_turn(self):
        self.Move_limit = 20
        if self.Mana < self.Knowledge * 10:
            if self.Mana + 5 < self.Knowledge * 10:
                self.Mana = self.Mana + 5
            else:
                self.Mana = self.Knowledge * 10
        self.Gold += self.gold_mine
        self.Wood += self.wood_mine
        self.Sulfur += self.sulfure_mine
        self.Stone += self.stone_mine
        self.Crystals += self.crystal_mine
        self.Mercury += self.mercury_mine
        self.day = self.day + 1
        if self.day == 8:
            self.week = self.week + 1
            self.day = 1
        if self.week == 4:
            self.week = 1
            self.month = self.month + 1
        if self.month == 13:
            self.month = 1