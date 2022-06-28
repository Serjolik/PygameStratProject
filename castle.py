import pygame
import os
from Hero import My_Hero
class Castle():
    def __init__(self):
        self.hero = My_Hero()
        self.lvl_tavern = 1
        self.lvl_capitol = 1
        self.lvl_castle = 1
        self.lvl_shop = 1
        self.lvl_mage = 1
        self.lvl_stables = 0
        self.lvl_training = 1
        self.lvl_grifin = 1
        self.lvl_barracks = 1
        self.lvl_guardhouse = 1
        self.lvl_archershouse = 1
        self.lvl_monastary = 1
        self.lvl_portalgl = 1
        self.hero = My_Hero()
        self.count_day = -1
    def upgr_tav(self):
        if self.hero.postroika_v_den > 0:
            if self.lvl_tavern < 2 and self.hero.day != self.count_day:
                self.lvl_tavern += 1
                self.hero.postroika_v_den = self.hero.postroika_v_den - 1

    def upgr_cap(self):
        if self.hero.postroika_v_den > 0:
            if self.lvl_capitol < 4 and self.hero.day != self.count_day:
                self.lvl_capitol += 1
                self.hero.postroika_v_den = self.hero.postroika_v_den - 1
    def upgr_cast(self):
        if self.lvl_castle < 3 and self.hero.day != self.count_day:
            self.lvl_castle += 1
    def upgr_shop(self):
        if self.lvl_shop < 2 and self.hero.day != self.count_day:
            self.lvl_shop += 1
    def upgr_mage(self):
        if self.lvl_mage < 4 and self.hero.day != self.count_day:
            self.lvl_mage += 1
    def upgr_stables(self):
        if self.lvl_stables < 1 and self.hero.day != self.count_day:
            self.lvl_stables += 1
    def upgr_train(self):
        if self.lvl_training< 2 and self.hero.day != self.count_day:
            self.lvl_training += 1
    def upgr_grif(self):
        if self.lvl_grifin < 2 and self.hero.day != self.count_day:
            self.lvl_grifin += 1
    def upgr_bar(self):
        if self.lvl_barracks < 2 and self.hero.day != self.count_day:
            self.lvl_barracks += 1
    def upgr_guard(self):
        if self.lvl_guardhouse < 2 and self.hero.day != self.count_day:
            self.lvl_guardhouse += 1
    def upgr_arch(self):
        if self.lvl_archershouse < 2 and self.hero.day != self.count_day:
            self.lvl_archershouse += 1
    def upgr_mon(self):
        if self.lvl_monastary < 2 and self.hero.day != self.count_day:
            self.lvl_monastary += 1
    def upgr_portal(self):
        if self.lvl_portalgl < 2 and self.hero.day != self.count_day:
            self.lvl_portalgl += 1


