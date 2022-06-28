import pygame
from pygame import *
import os
class mapp():
    def __init__(self):
        # ------------------------------------------ТЕКСТУРЫ КАРТЫ------------------------------------------------------

        # -------------------------------------------Туман войны--------------------------------------------------------
        self.War_fog = pygame.image.load(os.path.join('Textures', 'war_fog.png'))
        # -----------------------------------------------ЗАМОК----------------------------------------------------------
        self.Castle = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'Castle.png'))
        self.Castle.set_colorkey((0, 255, 255))
        # ----------------------------------------------ВУЛКАН----------------------------------------------------------
        self.Vulkano_0 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol50.png'))
        self.Vulkano_1 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol51.png'))
        self.Vulkano_2 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol52.png'))
        self.Vulkano_3 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol53.png'))
        self.Vulkano_4 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol54.png'))
        self.Vulkano_5 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol55.png'))
        self.Vulkano_6 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol56.png'))
        self.Vulkano_7 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol57.png'))
        self.Vulkano_8 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol58.png'))
        self.Vulkano_9 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol59.png'))
        self.Vulkano_10 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol60.png'))
        self.Vulkano_11 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol61.png'))
        self.Vulkano_12 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol62.png'))
        self.Vulkano_13 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLvol63.png'))

        # -------------------------------------------ЛУЖА ЛАВЫ----------------------------------------------------------
        self.Puddle_Lava_0 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav80.png'))
        self.Puddle_Lava_1 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav81.png'))
        self.Puddle_Lava_2 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav82.png'))
        self.Puddle_Lava_3 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav83.png'))
        self.Puddle_Lava_4 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav84.png'))
        self.Puddle_Lava_5 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav85.png'))
        self.Puddle_Lava_6 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav86.png'))
        self.Puddle_Lava_7 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav87.png'))
        self.Puddle_Lava_8 = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLlav88.png'))
        self.Puddle_Lava_0.set_colorkey((0, 255, 255))
        self.Puddle_Lava_1.set_colorkey((0, 255, 255))
        self.Puddle_Lava_2.set_colorkey((0, 255, 255))
        self.Puddle_Lava_3.set_colorkey((0, 255, 255))
        self.Puddle_Lava_4.set_colorkey((0, 255, 255))
        self.Puddle_Lava_5.set_colorkey((0, 255, 255))
        self.Puddle_Lava_6.set_colorkey((0, 255, 255))
        self.Puddle_Lava_7.set_colorkey((0, 255, 255))
        self.Puddle_Lava_8.set_colorkey((0, 255, 255))

        # ----------------------------------------------Деревья---------------------------------------------------------
        self.Tree = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'AVLAUTR0.png'))

        # ----------------------------------------------Золото(Ресурс)--------------------------------------------------
        self.Gold_0 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_1.png'))
        self.Gold_1 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_2.png'))
        self.Gold_2 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_3.png'))
        self.Gold_3 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_4.png'))
        self.Gold_4 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_5.png'))
        self.Gold_5 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_6.png'))
        self.Gold_6 = pygame.image.load(os.path.join('Textures', 'resources', 'gold_7.png'))

        # ----------------------------------------------Дерево(Ресурс)--------------------------------------------------
        self.Wood = pygame.image.load(os.path.join('Textures', 'resources', 'wood.png'))
        # ----------------------------------------------Минералы(Ресурс)------------------------------------------------

        # ------------------------------------------------Камень(Ресурс)------------------------------------------------
        self.Stone = pygame.image.load(os.path.join('Textures', 'resources', 'stone.png'))
        # -------------------------------------------------Ртуть(Ресурс)------------------------------------------------
        self.Mercury = pygame.image.load(os.path.join('Textures', 'resources', 'mercury.png'))
        # --------------------------------------------------Сера(Ресурс)------------------------------------------------
        self.Sulfur = pygame.image.load(os.path.join('Textures', 'resources', 'sulfur.png'))

        # ----------------------------------------------Кристалл(Ресурс)------------------------------------------------
        self.Crystal_0 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_1.png'))
        self.Crystal_1 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_2.png'))
        self.Crystal_2 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_3.png'))
        self.Crystal_3 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_4.png'))
        self.Crystal_4 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_5.png'))
        self.Crystal_5 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_6.png'))
        self.Crystal_6 = pygame.image.load(os.path.join('Textures', 'resources', 'crystal_7.png'))
        # --------------------------------------------Драгоценности(Ресурс)---------------------------------------------
        self.Jewelry_0 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_1.png'))
        self.Jewelry_1 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_2.png'))
        self.Jewelry_2 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_3.png'))
        self.Jewelry_3 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_4.png'))
        self.Jewelry_4 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_5.png'))
        self.Jewelry_5 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_6.png'))
        self.Jewelry_6 = pygame.image.load(os.path.join('Textures', 'resources', 'jewelry_7.png'))

        # ------------------------------------------Сундук с опытом и деньгами------------------------------------------
        self.Chest_0 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_1.png'))
        self.Chest_1 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_2.png'))
        self.Chest_2 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_3.png'))
        self.Chest_3 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_4.png'))
        self.Chest_4 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_5.png'))
        self.Chest_5 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_6.png'))
        self.Chest_6 = pygame.image.load(os.path.join('Textures', 'resources', 'chest_7.png'))

        # ------------------------------------------ТЕКСТУРЫ КАРТЫ------------------------------------------------------

        self.surf_2 = pygame.image.load(os.path.join('Textures', 'Move', 'go_up.png'))
        self.surf_1 = pygame.image.load(os.path.join('Textures', 'Move', 'go_down.png'))
        self.surf_3 = pygame.image.load(os.path.join('Textures', 'Move', 'go_right.png'))
        self.surf_4 = pygame.image.load(os.path.join('Textures', 'Move', 'go_left.png'))

        self.surf_2_not = pygame.image.load(os.path.join('Textures', 'Move', 'Direction_up.png'))
        self.surf_1_not = pygame.image.load(os.path.join('Textures', 'Move', 'Direction_down.png'))
        self.surf_3_not = pygame.image.load(os.path.join('Textures', 'Move', 'Direction_right.png'))
        self.surf_4_not = pygame.image.load(os.path.join('Textures', 'Move', 'Direction_left.png'))

        self.PLATFORM_WIDTH = 50
        self.PLATFORM_HEIGHT = 50
        self.PLATFORM_COLOR = "#FFFFFF"
        self.PLATFORM_COLOR_EXIT = "#FF0000"
        self.PLATFORM_COLOR_GOLD = "#FFFF00"

        self.Dirt = pygame.image.load(os.path.join('Textures', 'TEXTURES', 'grass.png'))

    def Map_bg(self, a, level, map_x, map_y):
        PLATFORM_WIDTH = 50
        PLATFORM_HEIGHT = 50
        past_map_x = map_x
        past_map_y = map_y

        for row in level:  # вся строка
            for col in row:
                dirt = self.Dirt.get_rect(center=(map_x + 25, map_y + 25))
                a.blit(self.Dirt, dirt)
                map_x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            map_y += PLATFORM_HEIGHT  # то же самое и с высотой
            map_x = past_map_x  # на каждой новой строчке начинаем с нуля
        map_y = past_map_y
        map_x = past_map_x

    def Maps(self, a, width, height, map_x, map_y, level, mask, checker_image_13, checker_image_9, checker_image_7,
             hero_x, hero_y):

        x = 0
        y = 0

        window = a

        mac_x = map_x
        mac_y = map_y

        past_map_x = map_x
        past_map_y = map_y
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if hero_x != x or hero_y != y:
                    if col == "-":
                        # создаем блок, заливаем его цветом и рисеум его

                        tree = self.Tree.get_rect(center=(map_x+15, map_y+15))
                        a.blit(self.Tree, tree)
                    elif col == "Castle":
                        castle = self.Castle.get_rect(center=(map_x + 10, map_y + 2))
                        a.blit(self.Castle, castle)
                    elif col == "+":
                        pf = Surface((self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))
                        pf.fill(Color(self.PLATFORM_COLOR_EXIT))
                        a.blit(pf, (map_x, map_y))
                    elif col == "wood":
                        wood = self.Wood.get_rect(center=(map_x + 25, map_y + 25))
                        a.blit(self.Wood, wood)
                    elif col == "stone":
                        stone = self.Stone.get_rect(center=(map_x + 25, map_y + 25))
                        a.blit(self.Stone, stone)
                    elif col == "sulfur":
                         sulfur = self.Sulfur.get_rect(center=(map_x + 25, map_y + 25))
                         a.blit(self.Sulfur, sulfur)
                    elif col == "mercury":
                        mercury = self.Mercury.get_rect(center=(map_x + 25, map_y + 25))
                        a.blit(self.Mercury, mercury)

                    elif col == "gold":
                        if checker_image_7 == 0:
                            Gold = self.Gold_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_0, Gold)
                        elif checker_image_7 == 1:
                            Gold = self.Gold_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_1, Gold)
                        elif checker_image_7 == 2:
                            Gold = self.Gold_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_2, Gold)
                        elif checker_image_7 == 3:
                            Gold = self.Gold_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_3, Gold)
                        elif checker_image_7 == 4:
                            Gold = self.Gold_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_4, Gold)
                        elif checker_image_7 == 5:
                            Gold = self.Gold_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_5, Gold)
                        elif checker_image_7 == 6:
                            Gold = self.Gold_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Gold_6, Gold)

                    elif col == "crystal":
                        if checker_image_7 == 0:
                            Crystal = self.Crystal_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_0, Crystal)
                        elif checker_image_7 == 1:
                            Crystal = self.Crystal_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_1, Crystal)
                        elif checker_image_7 == 2:
                            Crystal = self.Crystal_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_2, Crystal)
                        elif checker_image_7 == 3:
                            Crystal = self.Crystal_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_3, Crystal)
                        elif checker_image_7 == 4:
                            Crystal = self.Crystal_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_4, Crystal)
                        elif checker_image_7 == 5:
                            Crystal = self.Crystal_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_5, Crystal)
                        elif checker_image_7 == 6:
                            Crystal = self.Crystal_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Crystal_6, Crystal)

                    elif col == "jewelry":
                        if checker_image_7 == 0:
                            Jewelry = self.Jewelry_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_0, Jewelry)
                        elif checker_image_7 == 1:
                            Jewelry = self.Jewelry_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_1, Jewelry)
                        elif checker_image_7 == 2:
                            Jewelry = self.Jewelry_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_2, Jewelry)
                        elif checker_image_7 == 3:
                            Jewelry = self.Jewelry_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_3, Jewelry)
                        elif checker_image_7 == 4:
                            Jewelry = self.Jewelry_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_4, Jewelry)
                        elif checker_image_7 == 5:
                            Jewelry = self.Jewelry_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_5, Jewelry)
                        elif checker_image_7 == 6:
                            Jewelry = self.Jewelry_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Jewelry_6, Jewelry)

                    elif col == "chest":
                        if checker_image_7 == 0:
                            Chest = self.Chest_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_0, Chest)
                        elif checker_image_7 == 1:
                            Chest = self.Chest_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_1, Chest)
                        elif checker_image_7 == 2:
                            Chest = self.Chest_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_2, Chest)
                        elif checker_image_7 == 3:
                            Chest = self.Chest_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_3, Chest)
                        elif checker_image_7 == 4:
                            Chest = self.Chest_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_4, Chest)
                        elif checker_image_7 == 5:
                            Chest = self.Chest_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_5, Chest)
                        elif checker_image_7 == 6:
                            Chest = self.Chest_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Chest_6, Chest)

                    elif col == "Puddle_lava":
                        if checker_image_9 == 0 or checker_image_9 == 1:
                            Puddle_Lava = self.Puddle_Lava_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_0, Puddle_Lava)
                        elif checker_image_9 == 2 or checker_image_9 == 3:
                            Puddle_Lava = self.Puddle_Lava_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_1, Puddle_Lava)
                        elif checker_image_9 == 4 or checker_image_9 == 5:
                            Puddle_Lava = self.Puddle_Lava_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_2, Puddle_Lava)
                        elif checker_image_9 == 6 or checker_image_9 == 7:
                            Puddle_Lava = self.Puddle_Lava_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_3, Puddle_Lava)
                        elif checker_image_9 == 8 or checker_image_9 == 9:
                            Puddle_Lava = self.Puddle_Lava_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_4, Puddle_Lava)
                        elif checker_image_9 == 10 or checker_image_9 == 11:
                            Puddle_Lava = self.Puddle_Lava_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_5, Puddle_Lava)
                        elif checker_image_9 == 12 or checker_image_9 == 13:
                            Puddle_Lava = self.Puddle_Lava_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_6, Puddle_Lava)
                        elif checker_image_9 == 14 or checker_image_9 == 15:
                            Puddle_Lava = self.Puddle_Lava_7.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_7, Puddle_Lava)
                        elif checker_image_9 == 16 or checker_image_9 == 17:
                            Puddle_Lava = self.Puddle_Lava_8.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Puddle_Lava_8, Puddle_Lava)

                    elif col == "Vulkano":
                        if checker_image_13 == 0:
                            Vulkano = self.Vulkano_0.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_0, Vulkano)
                        elif checker_image_13 == 1:
                            Vulkano = self.Vulkano_1.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_1, Vulkano)
                        elif checker_image_13 == 2:
                            Vulkano = self.Vulkano_2.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_2, Vulkano)
                        elif checker_image_13 == 3:
                            Vulkano = self.Vulkano_3.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_3, Vulkano)
                        elif checker_image_13 == 4:
                            Vulkano = self.Vulkano_4.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_4, Vulkano)
                        elif checker_image_13 == 5:
                            Vulkano = self.Vulkano_5.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_5, Vulkano)
                        elif checker_image_13 == 6:
                            Vulkano = self.Vulkano_6.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_6, Vulkano)
                        elif checker_image_13 == 7:
                            Vulkano = self.Vulkano_7.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_7, Vulkano)
                        elif checker_image_13 == 8:
                            Vulkano = self.Vulkano_8.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_8, Vulkano)
                        elif checker_image_13 == 9:
                            Vulkano = self.Vulkano_9.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_9, Vulkano)
                        elif checker_image_13 == 10:
                            Vulkano = self.Vulkano_10.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_10, Vulkano)
                        elif checker_image_13 == 11:
                            Vulkano = self.Vulkano_11.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_11, Vulkano)
                        elif checker_image_13 == 12:
                            Vulkano = self.Vulkano_12.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_12, Vulkano)
                        elif checker_image_13 == 13:
                            Vulkano = self.Vulkano_13.get_rect(center=(map_x + 25, map_y + 25))
                            a.blit(self.Vulkano_13, Vulkano)
                x = x + 1
                map_x += self.PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            x = 0
            y = y + 1
            map_y += self.PLATFORM_HEIGHT  # то же самое и с высотой
            map_x = past_map_x  # на каждой новой строчке начинаем с нуля

        Test = 1
        past_mac_x = mac_x
        for row in mask:  # вся строка
            for col in row:  # каждый символ
                if col == "1":
                    # создаем блок, заливаем его цветом и рисеум его
                    direction_1 = self.surf_1.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_1, (35, 35)), (direction_1))
                if col == "2":
                    direction_2 = self.surf_2.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_2, (35, 35)), (direction_2))
                if col == "3":
                    direction_3 = self.surf_3.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_3, (35, 35)), (direction_3))
                if col == "4":
                    direction_4 = self.surf_4.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_4, (35, 35)), (direction_4))
                if col == "5":
                    # создаем блок, заливаем его цветом и рисеум его
                    direction_1 = self.surf_1_not.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_1_not, (35, 35)), (direction_1))
                if col == "6":
                    direction_2 = self.surf_2_not.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_2_not, (35, 35)), (direction_2))
                if col == "7":
                    direction_3 = self.surf_3_not.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_3_not, (35, 35)), (direction_3))
                if col == "8":
                    direction_4 = self.surf_4_not.get_rect(center=(mac_x+25, mac_y+25))
                    a.blit(pygame.transform.scale(self.surf_4_not, (35, 35)), (direction_4))


                mac_x += self.PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            mac_y += self.PLATFORM_HEIGHT  # то же самое и с высотой
            mac_x = past_mac_x  # на каждой новой строчке начинаем с нуля

    def draw_move_bar(self, a, x, y, pct):
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)
        if pct <= 0:
            pct = 0
        else:
            BAR_LENGTH = 5
            BAR_HEIGHT = 100
            fill = (pct / 75) * BAR_HEIGHT
            fill_rect = pygame.Rect(x, y-int(fill), BAR_LENGTH, fill)
            pygame.draw.rect(a, GREEN, fill_rect)
    def draw_mana_bar(self, a, x, y, pct):
        BLUE = (0, 0, 255)
        WHITE = (255, 255, 255)
        if pct <= 0:
            pct = 0
        else:
            BAR_LENGTH = 5
            BAR_HEIGHT = 100
            fill = (pct / 75) * BAR_HEIGHT
            fill_rect = pygame.Rect(x, y-int(fill), BAR_LENGTH, fill)
            pygame.draw.rect(a, BLUE, fill_rect)
    def draw_minimap(self, level, screen, hero_x, hero_y, war_fog):
        PLATFORM_WIDTH = 4
        PLATFORM_HEIGHT = 10
        PLATFORM_COLOR_1 = "#FFFFFF"
        PLATFORM_COLOR_2 = "#000000"
        PLATFORM_COLOR_3 = "#013220"
        PLATFORM_COLOR_4 = "#F7F21A"
        PLATFORM_COLOR_5 = "#7F7679"
        PLATFORM_COLOR_6 = "#3B5998"
        PLATFORM_COLOR_7 = "#140F0B"
        x = 1144
        y = 25
        level_draw = level
        if level_draw[hero_y][hero_x] != "Castle":
            level_draw[hero_y][hero_x] = "1"
        x1 = 0
        y1 = 0
        for row in level_draw:  # вся строка
            for col in row:  # каждый символ
                if war_fog[y1][x1] == "1":
                    if col == "1":
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_1))
                        screen.blit(pf, (x, y))
                    elif col == "-":
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_5))
                        screen.blit(pf, (x, y))
                    elif col == "Castle":
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_6))
                        screen.blit(pf, (x, y))
                    elif col != " " and col != "n" and col != "Castle" and col != "Vulkano" and col != "Puddle_Lava":
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_4))
                        screen.blit(pf, (x, y))
                    elif col == "Vulkano" or col == "Puddle_Lava":
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_7))
                        screen.blit(pf, (x, y))
                    else:
                        pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                        pf.fill(Color(PLATFORM_COLOR_3))
                        screen.blit(pf, (x, y))
                else:
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR_2))
                    screen.blit(pf, (x, y))
                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
                x1 = x1 + 1
            y1 = y1 + 1
            x1 = 0
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 1144  # на каждой новой строчке начинаем с нуля
        level_draw[hero_y][hero_x] = " "
    def draw_war_fog(self, a, level, map_x, map_y, hero_x, hero_y):
        PLATFORM_WIDTH = 50
        PLATFORM_HEIGHT = 50
        past_map_x = map_x
        past_map_y = map_y
        level[hero_y][hero_x] = "1"
        if hero_y > 0:
            level[hero_y-1][hero_x] = "1"
        if hero_x > 0:
            level[hero_y][hero_x-1] = "1"
        level[hero_y+1][hero_x] = "1"
        level[hero_y][hero_x+1] = "1"
        level[hero_y + 1][hero_x - 1] = "1"
        level[hero_y - 1][hero_x + 1] = "1"
        level[hero_y + 1][hero_x + 1] = "1"
        level[hero_y - 1][hero_x - 1] = "1"
        for row in level:  # вся строка
            for col in row:
                if col != "1":
                    war_fog = self.War_fog.get_rect(center=(map_x + 25, map_y + 25))
                    a.blit(self.War_fog, war_fog)
                map_x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            map_y += PLATFORM_HEIGHT  # то же самое и с высотой
            map_x = past_map_x  # на каждой новой строчке начинаем с нуля
        map_y = past_map_y
        map_x = past_map_x