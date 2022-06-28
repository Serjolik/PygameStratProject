import pygame
import os
from Draw_Map import mapp
from Hero import My_Hero
from castle_draw import castle

black = (0, 0, 0) #Цветовая заливка чёрного цвета
white = (255, 255, 255)#Цветовая заливка белого цвета

"""
Функция нахождения гипотинузы
Принимает на вход текущие координаты и координаты цели
"""

def distance_calculation(hero_x, hero_y, Move_x, Move_y):
    line_x = abs(Move_x - hero_x)
    line_y = abs(Move_y - hero_y)
    x = (line_x ** 2) + (line_y ** 2)
    return x

"""
Функция нахождения кратчайшей гипотинузы
Принимает на вход 4 разных гипотинузы
"""

def shortest_path_search(uway, dway, rway, lway):
    if (uway <= dway) and (uway <= rway) and (uway <= lway):
        return 1
    elif (dway <= uway) and (dway <= rway) and (dway <= lway):
        return 2
    elif (rway <= dway) and (rway <= uway) and (rway <= lway):
        return 3
    elif (lway <= dway) and (lway <= rway) and (lway <= uway):
        return 4


"""
количество элементов в массиве по длине и ширине
"""
x_simbols = 40
y_simbols = 60

"""
Функция отвечает за изменение кадров с некоторой задержкой
"""
def Zadershka():
    pygame.display.flip()
    pygame.time.wait(5)

def Zadershka_X5():
    pygame.display.flip()
    pygame.time.wait(100)


"""
основная функция
"""
def main():
    Map = mapp()
    pygame.init()  # Инициализация pygame
    pygame.display.set_caption("Heroes of Might and Magic")  # Пишем в шапку
    # -------------------------------------------------------------------------
    way = 0 #Номер выбранного пути
    hero = My_Hero() #Ввод класса герой
    past_move_limit = 0
    Hero_Window = False
    End_Turn_Checker = 0
    END_TURN = pygame.image.load(os.path.join('Textures', 'Panels_and_button', 'End_Turn.png'))
    end_turn = END_TURN.get_rect(center=(1253, 479))
    Hero_Button = pygame.image.load(os.path.join('Textures', 'Panels_and_button', 'hero.png'))
    hero_button = Hero_Button.get_rect(center=(1253, 435))
    Castle_Checker = 0
    Castle_Button = pygame.image.load(os.path.join('Textures', 'Panels_and_button', 'Castle_Button.png'))
    castle_button = Castle_Button.get_rect(center=(1231, 271))
    Castle_ico = pygame.image.load(os.path.join('Textures', 'Panels_and_button', "Castle_ico.png"))
    castle_ico = Castle_ico.get_rect(center=(1329, 293))
    hero_face_ico =pygame.image.load(os.path.join('Textures', 'Hero', "Hero_face_ico.png"))
    Hero_face_ico = hero_face_ico.get_rect(center=(1162, 293))
    Hero_face = pygame.image.load(os.path.join('Textures', 'Hero', 'Hero_face.png'))
    hero_face = Hero_face.get_rect(center=(1168, 553))
    game_event = ""

    Hero_Menu = pygame.image.load(os.path.join('Textures', 'Hero.png'))
    hero_menu = Hero_Menu.get_rect(center=(600, 370))

    Chest_selected = False



    shetchik_po_5 = 0
    
    """
    Используется в передвижении героя
    """

    past_hero_x = 0 #Прошлая координата героя по X
    past_hero_y = 0 #Прошлая координата героя по Y
    save_x = 0 #Сохранённая координата по x
    save_y = 0 #Сохранённая координата по y
    """
    Используется в отрисовке стрелок в другом массиве
    """
    x_direction = 1 #выбор пути по x
    y_direction = 1 #выбор пути по y
    past_x_direction = 0 #Выбор пути по x
    past_y_direction = 0 #Выбор пути по y

    """
    Номер изображения используется для анимации по кадрам
    """

    checker_image_13 = 0
    checker_image_9 = 0
    checker_image_7 = 0

    """
    Переменные длин гипотинузы
    """
    uway = 0
    dway = 0
    rway = 0
    lway = 0
    
    """
    Маска, массив который имеет при себе только стрелки, 
    которые не влияют на объекты основного массива, а лишь рисуются поверх
    """
    level_mask = [[0]*50 for i in range(20)]
    """
    Основной массив, содержащий в себе объекты, 
    """

    level = [
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
        ["-","1"," "," "," "," ","jewelry"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-","-","-"," "," "," ","-","-","-"," "," ","-","-"],
        ["-"," "," ","chest","-"," "," ","-"," "," "," "," "," "," "," "," ","sulfur"," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","jewelry"," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," "," "," "," ","chest"," ","mercury"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","crystal","-"," "," "," "," "," "," ","-"],
        ["-","chest"," "," "," "," "," "," "," "," "," "," "," ","-","-"," "," "," "," "," "," ","stone"," "," "," "," ","-","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"," "," "," ","-"],
        ["-"," "," "," ","chest"," "," "," "," "," "," "," "," "," "," "," ","wood"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","gold"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"," ","-"],
        ["-","-"," "," "," "," "," "," ","gold"," "," ","n","n","n"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," ","-"," ","-"," "," ","n","Castle","n"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","mercury"," "," "," "," "," "," "," "," "," "," ","-"],
        ["-","mercury"," "," "," "," "," "," "," "," "," ","n"," ","n"," "," "," "," "," "," ","Vulkano"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","sulfur"," "," "," "," "," "," ","-"],
        ["-"," ","-","crystal"," ","-","-","-","-"," "," "," "," "," "," "," "," "," "," ","n","n","n"," "," "," "," "," "," "," "," "," ","mercury"," "," ","-","-","-"," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," ","gold"," "," "," "," "," "," "," "," ","gold"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," "," ","-"," ","-"," "," "," "," "," "," "," "," "," "," "," "," ","-","-"," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," ","chest"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","crystal"," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," ","-"," "," "," ","-","-","-"," ","gold","-"," ","-","-"," "," "," "," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","wood"," "," ","sulfur"," "," "," "," "," ","wood"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," ","Vulkano"," "," "," "," "," "," "," "," "," "," "," "," ","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","gold"," "," "," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," ","n","n","n"," "," "," "," "," "," "," "," ","gold"," "," "," "," "," ","-","-"," "," "," "," "," "," "," "," "," ","-","-"," "," "," "," "," "," ","-"," "," "," ","-"," "," "," "," "," ","-"],
        ["-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","Puddle_lava"," "," "," "," "," "," ","chest"," "," "," "," "," "," "," "," "," "," ","jewelry"," "," "," "," "," "," "," "," "," "," "," ","-"],
        ["-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","-","-"],
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    ]
    """
    Копия массива для изменения
    """
    level_copy = level
    
    war_fog = [[0]*50 for i in range(20)]
    war_fog[7][12] = "1"
    war_fog[7][13] = "1"
    war_fog[7][11] = "1"
    war_fog[8][12] = "1"
    war_fog[6][12] = "1"
    war_fog[8][13] = "1"
    war_fog[8][11] = "1"
    war_fog[6][11] = "1"
    war_fog[6][13] = "1"
    war_fog[5][12] = "1"
    war_fog[9][12] = "1"
    war_fog[7][14] = "1"
    war_fog[7][10] = "1"
    war_fog[5][13] = "1"
    war_fog[5][11] = "1"
    war_fog[9][12] = "1"
    war_fog[9][13] = "1"
    war_fog[9][11] = "1"
    war_fog[7][14] = "1"
    war_fog[8][14] = "1"
    war_fog[6][14] = "1"
    war_fog[7][10] = "1"
    war_fog[6][10] = "1"
    war_fog[8][10] = "1"


    #-------------------------------------------------------------------------
    x = y = 0
    my_way = 0
    font = pygame.font.Font(None, 20)

    """
    Координаты мыши
    """
    mouse_x = 25
    mouse_y = 25
    """
    Координаты героя на массиве
    """
    hero_x = 1
    hero_y = 1
    """
    Изменение карты при отрисовке, для движения мышкой по карте
    """
    maps_x = -5
    maps_y = -5

    save_box = " " #Сохранение объкта на который наступил герой
    size = width, height = 1366, 768 #разрешение экрана
    max_x = 52 # Максимальные координаты героя по x
    max_y = 20 # Максимальные координаты героя по y
    screen = pygame.display.set_mode(
        (width, height), pygame.HWSURFACE | pygame.DOUBLEBUF) #Параметры окна
    game_over = False

    shectchek_po_devyati = 0

    surf_Fon = pygame.image.load(os.path.join('Textures', 'Castle_materials', '2.png'))

    Hero_Left_1 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_1.png'))
    Hero_Left_2 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_2.png'))
    Hero_Left_3 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_3.png'))
    Hero_Left_4 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_4.png'))
    Hero_Left_5 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_5.png'))
    Hero_Left_6 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_6.png'))
    Hero_Left_7 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_7.png'))
    Hero_Left_8 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_8.png'))
    Hero_Left_9 = pygame.image.load(os.path.join('Textures', 'Hero', 'Right_9.png'))
    Hero_Right_1 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_1.png'))
    Hero_Right_2 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_2.png'))
    Hero_Right_3 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_3.png'))
    Hero_Right_4 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_4.png'))
    Hero_Right_5 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_5.png'))
    Hero_Right_6 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_6.png'))
    Hero_Right_7 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_7.png'))
    Hero_Right_8 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_8.png'))
    Hero_Right_9 = pygame.image.load(os.path.join('Textures', 'Hero', 'Left_9.png'))
    Hero_Down_1 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_1.png'))
    Hero_Down_2 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_2.png'))
    Hero_Down_3 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_3.png'))
    Hero_Down_4 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_4.png'))
    Hero_Down_5 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_5.png'))
    Hero_Down_6 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_6.png'))
    Hero_Down_7 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_7.png'))
    Hero_Down_8 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_8.png'))
    Hero_Down_9 = pygame.image.load(os.path.join('Textures', 'Hero', 'Up_9.png'))
    Hero_Up_1 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_1.png'))
    Hero_Up_2 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_2.png'))
    Hero_Up_3 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_3.png'))
    Hero_Up_4 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_4.png'))
    Hero_Up_5 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_5.png'))
    Hero_Up_6 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_6.png'))
    Hero_Up_7 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_7.png'))
    Hero_Up_8 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_8.png'))
    Hero_Up_9 = pygame.image.load(os.path.join('Textures', 'Hero', 'Down_9.png'))

    Hero_State = 3


    Crystall = pygame.image.load(os.path.join('Textures', 'Do', 'Crystall.png'))
    Chest = pygame.image.load(os.path.join('Textures', 'Do', 'Chest.png'))
    Gold = pygame.image.load(os.path.join('Textures', 'Do', 'Gold.png'))
    Jewelry = pygame.image.load(os.path.join('Textures', 'Do', 'Jewelry.png'))
    Mercury = pygame.image.load(os.path.join('Textures', 'Do', 'Mercury.png'))
    Wood = pygame.image.load(os.path.join('Textures', 'Do', 'Wood.png'))
    Stone = pygame.image.load(os.path.join('Textures', 'Do', 'Stone.png'))
    Sulfur = pygame.image.load(os.path.join('Textures', 'Do', 'Sulfur.png'))


    End_timer_bg = pygame.image.load(os.path.join('Textures', 'time', 'bg.png'))
    End_timer_1 = pygame.image.load(os.path.join('Textures', 'time', '1.png'))
    End_timer_2 = pygame.image.load(os.path.join('Textures', 'time', '2.png'))
    End_timer_3 = pygame.image.load(os.path.join('Textures', 'time', '3.png'))
    End_timer_4 = pygame.image.load(os.path.join('Textures', 'time', '4.png'))
    End_timer_5 = pygame.image.load(os.path.join('Textures', 'time', '5.png'))
    End_timer_6 = pygame.image.load(os.path.join('Textures', 'time', '6.png'))
    End_timer_7 = pygame.image.load(os.path.join('Textures', 'time', '7.png'))
    End_timer_8 = pygame.image.load(os.path.join('Textures', 'time', '8.png'))
    End_timer_9 = pygame.image.load(os.path.join('Textures', 'time', '9.png'))
    End_timer_10 = pygame.image.load(os.path.join('Textures', 'time', '10.png'))

    surf_point = pygame.image.load(os.path.join('Textures', 'Move', 'xgreen.png')) #Крест на который идёт герой
    surf_point.set_colorkey((255, 255, 255))
    surf_not_point = pygame.image.load(os.path.join('Textures', 'Move', 'xred.png')) #Крест на который идёт герой
    surf_not_point.set_colorkey((255, 255, 255))

    Button = pygame.image.load(os.path.join('Textures', 'Do','Button.png'))
    Do_Gold = pygame.image.load(os.path.join('Textures', 'Do', 'Do_Gold.png'))
    Do_Exp = pygame.image.load(os.path.join('Textures', 'Do', 'Do_Exp.png'))


    xred_checker = 0

    Anti_Bug = 0

    Castle = castle()

    Do_Check = False #Проверка на выполнение действия
    Gold_or_exp = " "

    Hero_Checker = 0

    x1 = 50 #Координаты цели
    y1 = 50 #Координаты цели
    save_x1 = 1 #Сохранение координат цели
    save_y1 = 1 #Сохранение координат цели
    save = "-" #Сохранение объкта на который наступил герой
    mac_x = 0 #Переменные, которые отвечают за координаты цели в создании стрелок, а не в самом движении
    mac_y = 0
    checker_image_10 = 0
    Draw_hero = False
    draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x, hero_y)

    while not game_over:
        if Castle.all_game_over == True:
            game_over = True
        screen.fill(black)
        level_mask[hero_y][hero_x] = " "
        """
        Анимация
        """
        checker_image_9 = (checker_image_9 + 1) % 18
        checker_image_13 = (checker_image_13 + 1) % 13
        checker_image_7 = (checker_image_7 + 1) % 7
        shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
        """
        Запрет на выход за пределы карты
        """
        if Do_Check == False and Hero_Window == False:
            if mouse_x >= width - 25:
                if maps_x > -1 * max_x*50+1166:
                    maps_x = maps_x - 15
            if mouse_y >= height - 25:
                if maps_y > -1 * max_y*50+658:
                    maps_y = maps_y - 15
            if mouse_x <= 25:
                if maps_x <= max_x:
                    maps_x = maps_x + 15
            if mouse_y <= 25:
                if maps_y <= max_y:
                    maps_y = maps_y + 15
        #Перенос нужных переменных в файл отрисовки карты
        #Рисовка креста
        map_bg = Map.Map_bg(screen, level, maps_x, maps_y)
        my_map = Map.Maps(screen, width, height, maps_x, maps_y, level, level_mask, checker_image_13, checker_image_9,
                   checker_image_7, hero_x, hero_y)
        draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x, hero_y)
        Khrest = surf_point.get_rect(center=(x1 * 50 + 25 + maps_x, y1 * 50 + 25 + maps_y))
        if x1 > 0 and y1 > 0 and x1 < 22 + (maps_x / 50 * (-1)) and y1 <= max_y:
            if x1 != hero_x or y1 != hero_y:
                if xred_checker == 0:
                    screen.blit(surf_point, Khrest)
                else:
                    screen.blit(surf_not_point, Khrest)
        if Hero_State == 1:
            sem = Hero_Up_1.get_rect(center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 25 + maps_y))
            screen.blit(Hero_Up_1, sem)
        elif Hero_State == 2:
            sem = Hero_Down_1.get_rect(center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 25 + maps_y))
            screen.blit(Hero_Down_1, sem)
        elif Hero_State == 3:
            sem = Hero_Left_1.get_rect(center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 25 + maps_y))
            screen.blit(Hero_Left_1, sem)
        elif Hero_State == 4:
            sem = Hero_Right_1.get_rect(center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 25 + maps_y))
            screen.blit(Hero_Right_1, sem)

        sem_fon = surf_Fon.get_rect(center=(683, 384))
        Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
        screen.blit(surf_Fon, sem_fon)
        if End_Turn_Checker == 1:
            screen.blit(END_TURN, end_turn)
        if Castle_Checker == 1:
            screen.blit(Castle_Button, castle_button)
        if Hero_Checker == 1:
            screen.blit(Hero_Button, hero_button)
        screen.blit(Castle_ico, castle_ico)
        screen.blit(hero_face_ico, Hero_face_ico)
        map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
        map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
        text = font.render(str(hero.Gold), True, white)
        screen.blit(text, [1060, 744])
        text = font.render(str(hero.Wood), True, white)
        screen.blit(text, [400, 744])
        text = font.render(str(hero.Mercury), True, white)
        screen.blit(text, [510, 744])
        text = font.render(str(hero.Stone), True, white)
        screen.blit(text, [620, 744])
        text = font.render(str(hero.Sulfur), True, white)
        screen.blit(text, [730, 744])
        text = font.render(str(hero.Crystals), True, white)
        screen.blit(text, [840, 744])
        text = font.render(str(hero.Jewelry), True, white)
        screen.blit(text, [950, 744])
        text = font.render(str(hero.Attack), True, white)
        screen.blit(text, [1223, 580])
        text = font.render(str(hero.Defense), True, white)
        screen.blit(text, [1258, 580])
        text = font.render(str(hero.Magic), True, white)
        screen.blit(text, [1293, 580])
        text = font.render(str(hero.Knowledge), True, white)
        screen.blit(text, [1328, 580])
        text = font.render(str(hero.name), True, white)
        screen.blit(text, [1218, 518])
        text = font.render(str(hero.month), True, white)
        screen.blit(text, [1190, 743])
        text = font.render(str("Месяц:"), True, white)
        screen.blit(text, [1138, 743])
        text = font.render(str(hero.week), True, white)
        screen.blit(text, [1270, 743])
        text = font.render(str("Неделя:"), True, white)
        screen.blit(text, [1213, 743])
        text = font.render(str(hero.day), True, white)
        screen.blit(text, [1333, 743])
        text = font.render(str("День:"), True, white)
        screen.blit(text, [1288, 743])
        if Hero_Window == True:
            screen.blit(Hero_Menu, hero_menu)
            font = pygame.font.Font(None, 25)
            text = font.render(str(hero.Attack), True, white)
            screen.blit(text, [290, 221])
            text = font.render(str(hero.Defense), True, white)
            screen.blit(text, [365, 221])
            text = font.render(str(hero.Magic), True, white)
            screen.blit(text, [440, 221])
            text = font.render(str(hero.Knowledge), True, white)
            screen.blit(text, [515, 221])
            text = font.render(str(hero.Experience), True, white)
            screen.blit(text, [320, 324])
            text = font.render(str(hero.Mana), True, white)
            screen.blit(text, [470, 324])
            font = pygame.font.Font(None, 30)
            text = font.render(str(hero.Hero_Level), True, white)
            screen.blit(text, [433, 115])
            font = pygame.font.Font(None, 20)
        if Do_Check == True:
            screen.blit(Chest, [420, 82])
            if Chest_selected == True:
                screen.blit(Button, [582, 493])
                if Gold_or_exp == "Gold":
                    screen.blit(Do_Gold, [491, 330])
                elif Gold_or_exp == "Exp":
                    screen.blit(Do_Exp, [650, 330])

        if hero.Mana >= 10:
            text = font.render(str(hero.Mana), True, white)
            screen.blit(text, [1323, 631])
        else:
            text = font.render(str(hero.Mana), True, white)
            screen.blit(text, [1327, 631])
        screen.blit(Hero_face, hero_face)
        if save_box != " ":
            if save_box == "gold":
                screen.blit(Gold, [1120, 502])
                # Gold + 1
            elif save_box == "wood":
                screen.blit(Wood, [1120, 502])
                # Wood + 1
            elif save_box == "crystal":
                screen.blit(Crystall, [1120, 502])
                # crystal + 1
            elif save_box == "stone":
                screen.blit(Stone, [1120, 502])
                # stone + 1
            elif save_box == "sulfur":
                screen.blit(Sulfur, [1120, 502])
                # sulfur + 1
            elif save_box == "mercury":
                screen.blit(Mercury, [1120, 502])
                # mercury + 1
            elif save_box == "jewelry":
                screen.blit(Jewelry, [1120, 502])
                # jewelry + 1
        Zadershka()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if Hero_Window == False:
                        game_over = True
                    else:
                        Hero_Window = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                Взять координаты нажатия мыши и обнулить массив со стрелками
                """
                x1 = int(event.pos[0] / 50 - maps_x / 50)
                y1 = int(event.pos[1] / 50 - maps_y / 50)
                level_mask = [[0]*50 for i in range(20)]
                if x1 < 22 + (maps_x/50*(-1)):

                    """
                    Рисовка стрелок с исключениями в виде непроходимых участков
                    """
                    if x1 <= max_x and y1 <= max_y:
                        if war_fog[y1][x1] != "1" or level[y1][x1] == "-" or level[y1][x1] == "Vulkano" or level[y1][x1] == "Puddle_lava" or level[y1][x1] == "n" or level[y1][x1] == "Castle" or Do_Check or End_Turn_Checker or Hero_Window:
                            y1 = 0
                            x1 = 0
                            save_x1 = 0
                            save_y1 = 0
                        elif level[y1][x1] != "-" and level[y1][x1] != "Vulkano" and level[y1][x1] != "Puddle_lava" and level[y1][x1] != "n" and x1 > 0 and y1 > 0:
                            #-----------------------------------------------------------------------------------------------
                            x_direction = hero_x
                            y_direction = hero_y
                            past_move_limit = hero.Move_limit
                            Anti_Bug = 0
                            while (x_direction != x1 or y_direction != y1) and Anti_Bug <= 1000:
                                Anti_Bug = Anti_Bug + 1
                                uway = distance_calculation(x_direction, y_direction + 1, x1, y1)
                                dway = distance_calculation(x_direction, y_direction - 1, x1, y1)
                                rway = distance_calculation(x_direction + 1, y_direction, x1, y1)
                                lway = distance_calculation(x_direction - 1, y_direction, x1, y1)
                                my_way = distance_calculation(x_direction, y_direction, x1, y1)

                                if level[y_direction + 1][x_direction] !=" ":
                                    uway = uway + 9999999
                                    if (level[y_direction + 1][
                                        x_direction] == "-" or level[y_direction+1][x_direction] == "Vulkano" or level[y_direction+1][x_direction] == "n" or level[y_direction+1][x_direction] == "Castle" or level[y_direction+1][x_direction] == "Puddle_lava") and y_direction != 1 and y_direction != max_y:
                                        if dway > my_way:
                                            dway = dway + 100000
                                if level[y_direction - 1][x_direction] !=" ":
                                    dway = dway + 9999999
                                    if (level[y_direction - 1][
                                        x_direction] == "-" or level[y_direction - 1][x_direction] == "Vulkano" or level[y_direction - 1][x_direction] == "n" or level[y_direction - 1][x_direction] == "Castle" or level[y_direction - 1][x_direction] == "Puddle_lava") and y_direction != 1 and y_direction != max_y:
                                        if uway > my_way:
                                            uway = uway + 100000
                                if level[y_direction][x_direction + 1] != " ":
                                    rway = rway + 9999999
                                    if (level[y_direction][
                                        x_direction + 1] == "-" or level[y_direction][x_direction + 1] == "Vulkano" or level[y_direction][x_direction + 1] == "n" or level[y_direction][x_direction + 1] == "Castle" or level[y_direction][x_direction + 1] == "Puddle_lava") and x_direction != 1 and x_direction != max_x:
                                        if lway > my_way:
                                            lway = lway + 100000
                                if level[y_direction][x_direction - 1] != " ":
                                    lway = lway + 9999999
                                    if (level[y_direction][
                                        x_direction - 1] == "-" or level[y_direction][x_direction - 1] == "Vulkano" or level[y_direction][x_direction - 1] == "n" or level[y_direction][x_direction - 1] == "Castle" or level[y_direction][x_direction - 1] == "Puddle_lava") and x_direction != 1 and x_direction != max_x:
                                        if rway > my_way:
                                            rway = rway + 100000
                                if y_direction + 1 == y1 and x_direction == x1:
                                    uway = 0
                                elif y_direction - 1 == y1 and x_direction == x1:
                                    dway = 0
                                elif y_direction == y1 and x_direction + 1 == x1:
                                    rway = 0
                                elif y_direction == y1 and x_direction - 1 == x1:
                                    lway = 0

                                way = shortest_path_search(uway, dway, rway, lway)

                                past_x_direction = x_direction
                                past_y_direction = y_direction

                                if way == 1 and hero.Move_limit>=0:
                                    level_mask[y_direction][x_direction] = "1"
                                    y_direction = y_direction + 1
                                    #ВВЕРХ
                                elif way == 2 and hero.Move_limit>=0:
                                    level_mask[y_direction][x_direction] = "2"
                                    y_direction = y_direction - 1
                                    #ВНИЗ
                                elif way == 3 and hero.Move_limit>=0:
                                    level_mask[y_direction][x_direction] = "3"
                                    x_direction = x_direction + 1
                                    #ВПРАВО
                                elif way == 4 and hero.Move_limit>=0:
                                    level_mask[y_direction][x_direction] = "4"
                                    x_direction = x_direction - 1
                                    #ВЛЕВО
                                elif way == 1:
                                    level_mask[y_direction][x_direction] = "5"
                                    y_direction = y_direction + 1
                                    # ВВЕРХ
                                elif way == 2:
                                    level_mask[y_direction][x_direction] = "6"
                                    y_direction = y_direction - 1
                                    # ВНИЗ
                                elif way == 3:
                                    level_mask[y_direction][x_direction] = "7"
                                    x_direction = x_direction + 1
                                    # ВПРАВО
                                elif way == 4:
                                    level_mask[y_direction][x_direction] = "8"
                                    x_direction = x_direction - 1
                                    # ВЛЕВО
                                hero.Move_limit -= 1
                                if hero.Move_limit <= -1:
                                    xred_checker = 1
                                else:
                                    xred_checker = 0
                            if Anti_Bug >= 1000:
                                level_mask = [
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", "-", "-", "-", " ", " ", " ", "-", "-", "-", " ", " ",
                                     "-", "-"],
                                    ["-", " ", " ", "-", "-", " ", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", "-", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", "-", "-", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-",
                                     " ", "-"],
                                    ["-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", "-", " ", "-", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", "-", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", "-", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", "-",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", "-", "-", "-", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", "-", "-", " ", "-", "-", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", "-", "-", "-", "-", "-", "-", "-", " ", "-", "-", " ", "-", "-",
                                     " ", " ", " ", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-",
                                     "-", " ", " ", " ", " ", " ", " ", "-", " ", " ", " ", "-", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", "-"],
                                    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", " ", " ", " ",
                                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                                     "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                     "-", "-"]
                                ]
                                x1 = 0
                                y1 = 0
                                save_x1 = -1
                                save_y1 = -1
                                hero.Move_limit = past_move_limit
                            else:
                                hero.Move_limit = past_move_limit
                                past_x_direction = 0
                                past_y_direction = 0
                                #-----------------------------------------------------------------------------------------------
                                level[save_y][save_x] = save
                                save = level[y1][x1]
                                save_x = x1
                                save_y = y1
                            if x1 == save_x1 and y1 == save_y1:
                                #ЕСЛИ КООРДИНАТЫ НАЖАТИЯ СОВПАДАЮТ С КООРДИНАТАМИ ПРОШЛОГО НАЖАТИЯ
                                level[hero_y][hero_x] = " "
                                Anti_Bug = 0
                                while (hero_x != x1 or hero_y != y1) and hero.Move_limit > 0 and Anti_Bug <= 1000:
                                    Anti_Bug = Anti_Bug + 1
                                    #ПОКА КООРДИНАТЫ НЕ РАВНЫ - НАЧАТЬ ДВИЖЕНИЕ В СТОРОНУ ТОЧКИ
                                    #Повторная анимация в цикле движения
                                    checker_image_13 = (checker_image_13 + 1) % 13
                                    checker_image_7 = (checker_image_7 + 1) % 7
                                    checker_image_9 = (checker_image_9 + 1) % 9

                                    screen.fill(black)
                                    level_mask[hero_y][hero_x] = " "
                                    hero.Move_limit = hero.Move_limit - 1
                                    uway = distance_calculation(hero_x, hero_y+1, x1, y1)
                                    dway = distance_calculation(hero_x, hero_y-1, x1, y1)
                                    rway = distance_calculation(hero_x+1, hero_y, x1, y1)
                                    lway = distance_calculation(hero_x-1, hero_y, x1, y1)
                                    my_way = distance_calculation(hero_x, hero_y, x1, y1)

                                    if level[hero_y+1][hero_x] != " ":
                                        uway = uway + 9999999
                                        if (level[hero_y+1][hero_x] == "-" or level[hero_y+1][hero_x] == "Vulkano" or level[hero_y+1][hero_x] == "n" or level[hero_y+1][hero_x] == "Castle" or level[hero_y+1][hero_x] == "Puddle_lava") and hero_y != 1 and hero_y !=max_y:
                                            if dway > my_way:
                                                dway = dway + 100000
                                    if level[hero_y-1][hero_x] != " ":
                                        dway = dway + 9999999
                                        if (level[hero_y-1][hero_x] == "-" or level[hero_y-1][hero_x] == "Vulkano" or level[hero_y-1][hero_x] == "n" or level[hero_y-1][hero_x] == "Castle" or level[hero_y-1][hero_x] == "Puddle_lava") and hero_y != 1 and hero_y !=max_y:
                                            if uway > my_way:
                                                uway = uway + 100000
                                    if level[hero_y][hero_x+1] != " ":
                                        rway = rway + 9999999
                                        if (level[hero_y][hero_x+1] == "-" or level[hero_y][hero_x+1] == "Vulkano" or level[hero_y][hero_x+1] == "n" or level[hero_y][hero_x+1] == "Castle" or level[hero_y][hero_x+1] == "Puddle_lava") and hero_x != 1 and hero_x !=max_x:
                                            if lway > my_way:
                                                lway = lway + 100000
                                    if level[hero_y][hero_x-1] != " ":
                                        lway = lway + 9999999
                                        if (level[hero_y][hero_x-1] == "-" or level[hero_y][hero_x-1] == "Vulkano" or level[hero_y][hero_x-1] == "n" or level[hero_y][hero_x-1] == "Castle" or level[hero_y][hero_x-1] == "Puddle_lava") and hero_x != 1 and hero_x !=max_x:
                                            if rway > my_way:
                                                rway = rway + 100000
                                    if hero_y + 1 == y1 and hero_x == x1:
                                        uway = 0
                                    elif hero_y - 1 == y1 and hero_x == x1:
                                        dway = 0
                                    elif hero_y == y1 and hero_x + 1 == x1:
                                        rway = 0
                                    elif hero_y == y1 and hero_x - 1 == x1:
                                        lway = 0

                                    way = shortest_path_search(uway, dway, rway, lway)

                                    past_hero_x = hero_x
                                    past_hero_y = hero_y

                                    if way == 1:
                                        hero_y = hero_y + 1
                                        if xred_checker == 0:
                                            screen.blit(surf_point, Khrest)
                                        else:
                                            screen.blit(surf_not_point, Khrest)
                                        Hero_State = 1
                                        shetchik_po_5 = 0
                                        while shetchik_po_5 < 5:
                                            checker_image_9 = (checker_image_9 + 1) % 18
                                            checker_image_13 = (checker_image_13 + 1) % 13
                                            checker_image_7 = (checker_image_7 + 1) % 7
                                            map_bg = Map.Map_bg(screen, level, maps_x, maps_y)
                                            my_map = Map.Maps(screen, width, height, maps_x, maps_y, level, level_mask,
                                                              checker_image_13, checker_image_9, checker_image_7, hero_x, hero_y)
                                            draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x,
                                                                            hero_y)
                                            if x1 != hero_x or y1 != hero_y:
                                                if xred_checker == 0:
                                                    screen.blit(surf_point, Khrest)
                                                else:
                                                    screen.blit(surf_not_point, Khrest)
                                            shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
                                            shetchik_po_5 = shetchik_po_5 + 1
                                            if Hero_State == 1:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Up_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Up_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Up_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Up_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Up_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Up_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Up_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Up_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Up_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Up_9, sem)
                                            elif Hero_State == 2:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Down_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Down_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Down_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Down_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Down_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Down_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Down_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Down_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Down_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Down_9, sem)
                                            elif Hero_State == 3:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Left_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Left_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Left_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Left_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Left_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Left_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Left_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Left_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Left_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Left_9, sem)
                                            elif Hero_State == 4:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Right_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Right_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Right_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Right_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Right_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Right_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Right_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Right_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Right_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 - 25 + shetchik_po_5 * 10 + maps_y))
                                                    screen.blit(Hero_Right_9, sem)
                                            level_mask[hero_y][hero_x] = " "
                                            Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
                                            screen.blit(surf_Fon, sem_fon)
                                            screen.blit(Castle_ico, castle_ico)
                                            screen.blit(hero_face_ico, Hero_face_ico)
                                            map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
                                            map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
                                            text = font.render(str(hero.Gold), True, white)
                                            screen.blit(text, [1060, 744])
                                            text = font.render(str(hero.Wood), True, white)
                                            screen.blit(text, [400, 744])
                                            text = font.render(str(hero.Mercury), True, white)
                                            screen.blit(text, [510, 744])
                                            text = font.render(str(hero.Stone), True, white)
                                            screen.blit(text, [620, 744])
                                            text = font.render(str(hero.Sulfur), True, white)
                                            screen.blit(text, [730, 744])
                                            text = font.render(str(hero.Crystals), True, white)
                                            screen.blit(text, [840, 744])
                                            text = font.render(str(hero.Jewelry), True, white)
                                            screen.blit(text, [950, 744])
                                            text = font.render(str(hero.Attack), True, white)
                                            screen.blit(text, [1223, 580])
                                            text = font.render(str(hero.Defense), True, white)
                                            screen.blit(text, [1258, 580])
                                            text = font.render(str(hero.Magic), True, white)
                                            screen.blit(text, [1293, 580])
                                            text = font.render(str(hero.Knowledge), True, white)
                                            screen.blit(text, [1328, 580])
                                            text = font.render(str(hero.name), True, white)
                                            screen.blit(text, [1218, 518])
                                            text = font.render(str(hero.month), True, white)
                                            screen.blit(text, [1190, 743])
                                            text = font.render(str("Месяц:"), True, white)
                                            screen.blit(text, [1138, 743])
                                            text = font.render(str(hero.week), True, white)
                                            screen.blit(text, [1270, 743])
                                            text = font.render(str("Неделя:"), True, white)
                                            screen.blit(text, [1213, 743])
                                            text = font.render(str(hero.day), True, white)
                                            screen.blit(text, [1333, 743])
                                            text = font.render(str("День:"), True, white)
                                            screen.blit(text, [1288, 743])
                                            if hero.Mana >= 10:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1323, 631])
                                            else:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1327, 631])
                                            screen.blit(Hero_face, hero_face)
                                            Zadershka()
                                        #ВВЕРХ
                                    elif way == 2:
                                        hero_y = hero_y - 1
                                        if xred_checker == 0:
                                            screen.blit(surf_point, Khrest)
                                        else:
                                            screen.blit(surf_not_point, Khrest)
                                        Hero_State = 2
                                        shetchik_po_5 = 0
                                        while shetchik_po_5 < 5:
                                            checker_image_9 = (checker_image_9 + 1) % 18
                                            checker_image_13 = (checker_image_13 + 1) % 13
                                            checker_image_7 = (checker_image_7 + 1) % 7
                                            map_bg = Map.Map_bg(screen, level, maps_x, maps_y)
                                            my_map = Map.Maps(screen, width, height, maps_x, maps_y, level, level_mask,
                                                              checker_image_13, checker_image_9, checker_image_7, hero_x, hero_y)
                                            draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x,
                                                                            hero_y)
                                            shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
                                            if x1 != hero_x or y1 != hero_y:
                                                if xred_checker == 0:
                                                    screen.blit(surf_point, Khrest)
                                                else:
                                                    screen.blit(surf_not_point, Khrest)
                                            shetchik_po_5 = shetchik_po_5 + 1
                                            if Hero_State == 1:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Up_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Up_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Up_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Up_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Up_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Up_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Up_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Up_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Up_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Up_9, sem)
                                            elif Hero_State == 2:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Down_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Down_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Down_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Down_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Down_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Down_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Down_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Down_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Down_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Down_9, sem)
                                            elif Hero_State == 3:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Left_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Left_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Left_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Left_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Left_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Left_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Left_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Left_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Left_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Left_9, sem)
                                            elif Hero_State == 4:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Right_1.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Right_2.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Right_3.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Right_4.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Right_5.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Right_6.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Right_7.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Right_8.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Right_9.get_rect(
                                                        center=(hero_x * 50 + 25 + maps_x, hero_y * 50 + 75 - (shetchik_po_5 * 10) + maps_y))
                                                    screen.blit(Hero_Right_9, sem)
                                            level_mask[hero_y][hero_x] = " "
                                            Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
                                            screen.blit(surf_Fon, sem_fon)
                                            screen.blit(Castle_ico, castle_ico)
                                            screen.blit(hero_face_ico, Hero_face_ico)
                                            map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
                                            map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
                                            text = font.render(str(hero.Gold), True, white)
                                            screen.blit(text, [1060, 744])
                                            text = font.render(str(hero.Wood), True, white)
                                            screen.blit(text, [400, 744])
                                            text = font.render(str(hero.Mercury), True, white)
                                            screen.blit(text, [510, 744])
                                            text = font.render(str(hero.Stone), True, white)
                                            screen.blit(text, [620, 744])
                                            text = font.render(str(hero.Sulfur), True, white)
                                            screen.blit(text, [730, 744])
                                            text = font.render(str(hero.Crystals), True, white)
                                            screen.blit(text, [840, 744])
                                            text = font.render(str(hero.Jewelry), True, white)
                                            screen.blit(text, [950, 744])
                                            text = font.render(str(hero.Attack), True, white)
                                            screen.blit(text, [1223, 580])
                                            text = font.render(str(hero.Defense), True, white)
                                            screen.blit(text, [1258, 580])
                                            text = font.render(str(hero.Magic), True, white)
                                            screen.blit(text, [1293, 580])
                                            text = font.render(str(hero.Knowledge), True, white)
                                            screen.blit(text, [1328, 580])
                                            text = font.render(str(hero.name), True, white)
                                            screen.blit(text, [1218, 518])
                                            text = font.render(str(hero.month), True, white)
                                            screen.blit(text, [1190, 743])
                                            text = font.render(str("Месяц:"), True, white)
                                            screen.blit(text, [1138, 743])
                                            text = font.render(str(hero.week), True, white)
                                            screen.blit(text, [1270, 743])
                                            text = font.render(str("Неделя:"), True, white)
                                            screen.blit(text, [1213, 743])
                                            text = font.render(str(hero.day), True, white)
                                            screen.blit(text, [1333, 743])
                                            text = font.render(str("День:"), True, white)
                                            screen.blit(text, [1288, 743])
                                            if hero.Mana >= 10:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1323, 631])
                                            else:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1327, 631])
                                            screen.blit(Hero_face, hero_face)
                                            Zadershka()
                                            #ВНИЗ
                                    elif way == 3:
                                        hero_x = hero_x + 1
                                        if xred_checker == 0:
                                            screen.blit(surf_point, Khrest)
                                        else:
                                            screen.blit(surf_not_point, Khrest)
                                        Hero_State = 3
                                        shetchik_po_5 = 0
                                        while shetchik_po_5 < 5:
                                            checker_image_9 = (checker_image_9 + 1) % 18
                                            checker_image_13 = (checker_image_13 + 1) % 13
                                            checker_image_7 = (checker_image_7 + 1) % 7
                                            map_bg = Map.Map_bg(screen, level, maps_x, maps_y)
                                            my_map = Map.Maps(screen, width, height, maps_x, maps_y, level, level_mask,
                                                              checker_image_13, checker_image_9, checker_image_7, hero_x, hero_y)
                                            draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x,
                                                                            hero_y)
                                            shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
                                            shetchik_po_5 = shetchik_po_5 + 1
                                            if x1 != hero_x or y1 != hero_y:
                                                if xred_checker == 0:
                                                    screen.blit(surf_point, Khrest)
                                                else:
                                                    screen.blit(surf_not_point, Khrest)
                                            if Hero_State == 1:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Up_1.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Up_2.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Up_3.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Up_4.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Up_5.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Up_6.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Up_7.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Up_8.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Up_9.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_9, sem)
                                            elif Hero_State == 2:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Down_1.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Down_2.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Down_3.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Down_4.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Down_5.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Down_6.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Down_7.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Down_8.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Down_9.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_9, sem)
                                            elif Hero_State == 3:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Left_1.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Left_2.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Left_3.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Left_4.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Left_5.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Left_6.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Left_7.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Left_8.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Left_9.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_9, sem)
                                            elif Hero_State == 4:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Right_1.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Right_2.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Right_3.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Right_4.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Right_5.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Right_6.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Right_7.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Right_8.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Right_9.get_rect(
                                                        center=(hero_x * 50 - 25 + (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_9, sem)
                                            level_mask[hero_y][hero_x] = " "
                                            Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
                                            screen.blit(surf_Fon, sem_fon)
                                            screen.blit(Castle_ico, castle_ico)
                                            screen.blit(hero_face_ico, Hero_face_ico)
                                            map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
                                            map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
                                            text = font.render(str(hero.Gold), True, white)
                                            screen.blit(text, [1060, 744])
                                            text = font.render(str(hero.Wood), True, white)
                                            screen.blit(text, [400, 744])
                                            text = font.render(str(hero.Mercury), True, white)
                                            screen.blit(text, [510, 744])
                                            text = font.render(str(hero.Stone), True, white)
                                            screen.blit(text, [620, 744])
                                            text = font.render(str(hero.Sulfur), True, white)
                                            screen.blit(text, [730, 744])
                                            text = font.render(str(hero.Crystals), True, white)
                                            screen.blit(text, [840, 744])
                                            text = font.render(str(hero.Jewelry), True, white)
                                            screen.blit(text, [950, 744])
                                            text = font.render(str(hero.Attack), True, white)
                                            screen.blit(text, [1223, 580])
                                            text = font.render(str(hero.Defense), True, white)
                                            screen.blit(text, [1258, 580])
                                            text = font.render(str(hero.Magic), True, white)
                                            screen.blit(text, [1293, 580])
                                            text = font.render(str(hero.Knowledge), True, white)
                                            screen.blit(text, [1328, 580])
                                            text = font.render(str(hero.name), True, white)
                                            screen.blit(text, [1218, 518])
                                            text = font.render(str(hero.month), True, white)
                                            screen.blit(text, [1190, 743])
                                            text = font.render(str("Месяц:"), True, white)
                                            screen.blit(text, [1138, 743])
                                            text = font.render(str(hero.week), True, white)
                                            screen.blit(text, [1270, 743])
                                            text = font.render(str("Неделя:"), True, white)
                                            screen.blit(text, [1213, 743])
                                            text = font.render(str(hero.day), True, white)
                                            screen.blit(text, [1333, 743])
                                            text = font.render(str("День:"), True, white)
                                            screen.blit(text, [1288, 743])
                                            if hero.Mana >= 10:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1323, 631])
                                            else:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1327, 631])
                                            screen.blit(Hero_face, hero_face)
                                            Zadershka()
                                            #ВПРАВО
                                    elif way == 4:
                                        hero_x = hero_x - 1
                                        if xred_checker == 0:
                                            screen.blit(surf_point, Khrest)
                                        else:
                                            screen.blit(surf_not_point, Khrest)
                                        Hero_State = 4
                                        shetchik_po_5 = 0
                                        if x1 != hero_x or y1 != hero_y:
                                            if xred_checker == 0:
                                                screen.blit(surf_point, Khrest)
                                            else:
                                                screen.blit(surf_not_point, Khrest)
                                        while shetchik_po_5 < 5:
                                            checker_image_9 = (checker_image_9 + 1) % 18
                                            checker_image_13 = (checker_image_13 + 1) % 13
                                            checker_image_7 = (checker_image_7 + 1) % 7
                                            map_bg = Map.Map_bg(screen, level, maps_x, maps_y)
                                            my_map = Map.Maps(screen, width, height, maps_x, maps_y, level, level_mask,
                                                              checker_image_13, checker_image_9, checker_image_7, hero_x, hero_y)
                                            draw_war_fog = Map.draw_war_fog(screen, war_fog, maps_x, maps_y, hero_x,
                                                                            hero_y)
                                            shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
                                            shetchik_po_5 = shetchik_po_5 + 1
                                            if x1 != hero_x or y1 != hero_y:
                                                if xred_checker == 0:
                                                    screen.blit(surf_point, Khrest)
                                                else:
                                                    screen.blit(surf_not_point, Khrest)
                                            if Hero_State == 1:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Up_1.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Up_2.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Up_3.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Up_4.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Up_5.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Up_6.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Up_7.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Up_8.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Up_9.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Up_9, sem)
                                            elif Hero_State == 2:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Down_1.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Down_2.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Down_3.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Down_4.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Down_5.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Down_6.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Down_7.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Down_8.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Down_9.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Down_9, sem)
                                            elif Hero_State == 3:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Left_1.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Left_2.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Left_3.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Left_4.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Left_5.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Left_6.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Left_7.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Left_8.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Left_9.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Left_9, sem)
                                            elif Hero_State == 4:
                                                if shectchek_po_devyati == 0:
                                                    sem = Hero_Right_1.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_1, sem)
                                                elif shectchek_po_devyati == 1:
                                                    sem = Hero_Right_2.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_2, sem)
                                                elif shectchek_po_devyati == 2:
                                                    sem = Hero_Right_3.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_3, sem)
                                                elif shectchek_po_devyati == 3:
                                                    sem = Hero_Right_4.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_4, sem)
                                                elif shectchek_po_devyati == 4:
                                                    sem = Hero_Right_5.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_5, sem)
                                                elif shectchek_po_devyati == 5:
                                                    sem = Hero_Right_6.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_6, sem)
                                                elif shectchek_po_devyati == 6:
                                                    sem = Hero_Right_7.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_7, sem)
                                                elif shectchek_po_devyati == 7:
                                                    sem = Hero_Right_8.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_8, sem)
                                                elif shectchek_po_devyati == 8:
                                                    sem = Hero_Right_9.get_rect(
                                                        center=(hero_x * 50 + 75 - (shetchik_po_5 * 10) + maps_x, hero_y * 50 + 25 + maps_y))
                                                    screen.blit(Hero_Right_9, sem)
                                            level_mask[hero_y][hero_x] = " "
                                            Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
                                            screen.blit(surf_Fon, sem_fon)
                                            screen.blit(Castle_ico, castle_ico)
                                            screen.blit(hero_face_ico, Hero_face_ico)
                                            map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
                                            map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
                                            text = font.render(str(hero.Gold), True, white)
                                            screen.blit(text, [1060, 744])
                                            text = font.render(str(hero.Wood), True, white)
                                            screen.blit(text, [400, 744])
                                            text = font.render(str(hero.Mercury), True, white)
                                            screen.blit(text, [510, 744])
                                            text = font.render(str(hero.Stone), True, white)
                                            screen.blit(text, [620, 744])
                                            text = font.render(str(hero.Sulfur), True, white)
                                            screen.blit(text, [730, 744])
                                            text = font.render(str(hero.Crystals), True, white)
                                            screen.blit(text, [840, 744])
                                            text = font.render(str(hero.Jewelry), True, white)
                                            screen.blit(text, [950, 744])
                                            text = font.render(str(hero.Attack), True, white)
                                            screen.blit(text, [1223, 580])
                                            text = font.render(str(hero.Defense), True, white)
                                            screen.blit(text, [1258, 580])
                                            text = font.render(str(hero.Magic), True, white)
                                            screen.blit(text, [1293, 580])
                                            text = font.render(str(hero.Knowledge), True, white)
                                            screen.blit(text, [1328, 580])
                                            text = font.render(str(hero.name), True, white)
                                            screen.blit(text, [1218, 518])
                                            text = font.render(str(hero.month), True, white)
                                            screen.blit(text, [1190, 743])
                                            text = font.render(str("Месяц:"), True, white)
                                            screen.blit(text, [1138, 743])
                                            text = font.render(str(hero.week), True, white)
                                            screen.blit(text, [1270, 743])
                                            text = font.render(str("Неделя:"), True, white)
                                            screen.blit(text, [1213, 743])
                                            text = font.render(str(hero.day), True, white)
                                            screen.blit(text, [1333, 743])
                                            text = font.render(str("День:"), True, white)
                                            screen.blit(text, [1288, 743])
                                            if hero.Mana >= 10:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1323, 631])
                                            else:
                                                text = font.render(str(hero.Mana), True, white)
                                                screen.blit(text, [1327, 631])
                                            screen.blit(Hero_face, hero_face)
                                            Zadershka()
                                    if level[hero_y][hero_x] == "gold":
                                        hero.pick_up_gold()
                                        #Gold + 1
                                    elif level[hero_y][hero_x] == "wood":
                                        hero.pick_up_wood()
                                        #Wood + 1
                                    elif level[hero_y][hero_x] == "stone":
                                        hero.pick_up_stone()
                                        #stone + 1
                                    elif level[hero_y][hero_x] == "sulfur":
                                        hero.pick_up_sulfur()
                                        #sulfur + 1
                                    elif level[hero_y][hero_x] == "mercury":
                                        hero.pick_up_mercury()
                                        #mercury + 1
                                    elif level[hero_y][hero_x] == "jewelry":
                                        hero.pick_up_Jewelry()
                                        #jewelry + 1
                                    elif level[hero_y][hero_x] == "crystal":
                                        hero.pick_up_Crystal()
                                        #Crystal + 1
                                    elif level[hero_y][hero_x] == "chest":
                                        Do_Check = True
                                        game_event = "Chest"
                                    elif level[hero_y - 1][hero_x] == "Castle":
                                        Castle.castle_draw(screen)
                                    shectchek_po_devyati = (shectchek_po_devyati + 1) % 9
                                    level_mask[hero_y][hero_x] = " "
                                    save_box = level[hero_y][hero_x]
                                past_hero_x = 0
                                past_hero_y = 0

                            else: #ЕСЛИ КООРДИНАТЫ НАЖАТИЯ, НЕ СОВПАДАЮТ С ПРОШЛЫМИ КООРДИНАТАМИ НАЖАТИЯ
                                save_x1 = x1
                                save_y1 = y1
                    else:
                        x1 = 0
                        y1 = 0
                if (int(event.pos[0]) >= 1212 and int(event.pos[1]) >= 456 and int(event.pos[0]) <= 1291 and int(event.pos[1] <= 496)) and Hero_Window == False and Do_Check == False:
                    End_Turn_Checker = 1
                    screen.blit(END_TURN, end_turn)
                    x1=0
                    y1=0
                if (int(event.pos[0]) >= 1210 and int(event.pos[1]) >= 416 and int(event.pos[0]) <= 1291 and int(event.pos[1] <= 453)) and Hero_Window == False and Do_Check == False:
                    Hero_Checker = True
                    screen.blit(Hero_Button, hero_button)
                    x1 = 0
                    y1 = 0
                if (int(event.pos[0]) >= 1210 and int(event.pos[1]) >= 251 and int(event.pos[0]) <= 1250 and int(event.pos[1] <= 289)) and Hero_Window == False and Do_Check == False:
                    Castle_Checker = True
                    screen.blit(Castle_Button, castle_button)
                    x1 = 0
                    y1 = 0
                if Do_Check == True:
                    if game_event == "Chest":
                        if event.pos[0] >= 490 and event.pos[1] >= 328 and event.pos[0] <= 591 and event.pos[1] <= 443:
                            Gold_or_exp = "Gold"
                            Chest_selected = True
                        elif event.pos[0] >= 646 and event.pos[1] >= 328 and event.pos[0] <= 749 and event.pos[1] <= 443:
                            Gold_or_exp = "Exp"
                            Chest_selected = True
                        if event.pos[0] >= 582 and event.pos[1] >= 495 and event.pos[0] <= 665 and event.pos[1] <= 531 and Chest_selected:
                            Do_Check = False
                            Chest_selected = False
                            if Gold_or_exp == "Gold":
                                hero.Gold = hero.Gold + 1000
                            else:
                                hero.Experience = hero.Experience + 500
                                if hero.Experience >= hero.Level_Up_Experience:
                                    hero.Experience = hero.Experience - hero.Level_Up_Experience
                                    hero.Level_Up_Experience += 500
                                    if hero.Attack == 1:
                                        hero.Attack += 1
                                    elif hero.Defense == 1:
                                        hero.Defense += 1
                                    elif hero.Defence == 1:
                                        hero.Magic += 1
                                    else:
                                        hero.Knowledge += 1
                                    hero.Hero_Level+=1
                            Gold_or_exp = ""
                    elif game_event == "Hero":
                        Draw_hero = True


            if event.type == pygame.MOUSEMOTION:
                #Изменение картинки при движении мышкой
                mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if (int(event.pos[0]) >= 1210 and int(event.pos[1]) >= 416 and int(event.pos[0]) <= 1291 and int(
                        event.pos[1] <= 453)) and Hero_Checker == True and Hero_Window == False and Do_Check == False:
                    Hero_Window = True
                if Hero_Window == True:
                    screen.blit(Hero_Menu, hero_menu)


                elif (int(event.pos[0]) >= 1210 and int(event.pos[1]) >= 251 and int(event.pos[0]) <= 1250 and int(event.pos[1] <= 289)) and Hero_Window == False and Do_Check == False and Castle_Checker==True:
                    if maps_x != -20 or maps_y != -20:
                        maps_x = -20
                        maps_y = -20
                    else:
                        Map.draw_minimap(level_copy, screen, hero_x, hero_y,war_fog)
                        screen.blit(surf_Fon, sem_fon)
                        screen.blit(Castle_ico, castle_ico)
                        screen.blit(hero_face_ico, Hero_face_ico)
                        map_fon = Map.draw_move_bar(screen, 1124, 309, hero.Move_limit)
                        map_fon = Map.draw_mana_bar(screen, 1195, 309, hero.Mana)
                        text = font.render(str(hero.Gold), True, white)
                        screen.blit(text, [1060, 744])
                        text = font.render(str(hero.Wood), True, white)
                        screen.blit(text, [400, 744])
                        text = font.render(str(hero.Mercury), True, white)
                        screen.blit(text, [510, 744])
                        text = font.render(str(hero.Stone), True, white)
                        screen.blit(text, [620, 744])
                        text = font.render(str(hero.Sulfur), True, white)
                        screen.blit(text, [730, 744])
                        text = font.render(str(hero.Crystals), True, white)
                        screen.blit(text, [840, 744])
                        text = font.render(str(hero.Jewelry), True, white)
                        screen.blit(text, [950, 744])
                        text = font.render(str(hero.Attack), True, white)
                        screen.blit(text, [1223, 580])
                        text = font.render(str(hero.Defense), True, white)
                        screen.blit(text, [1258, 580])
                        text = font.render(str(hero.Magic), True, white)
                        screen.blit(text, [1293, 580])
                        text = font.render(str(hero.Knowledge), True, white)
                        screen.blit(text, [1328, 580])
                        text = font.render(str(hero.name), True, white)
                        screen.blit(text, [1218, 518])
                        text = font.render(str(hero.month), True, white)
                        screen.blit(text, [1190, 743])
                        text = font.render(str("Месяц:"), True, white)
                        screen.blit(text, [1138, 743])
                        text = font.render(str(hero.week), True, white)
                        screen.blit(text, [1270, 743])
                        text = font.render(str("Неделя:"), True, white)
                        screen.blit(text, [1213, 743])
                        text = font.render(str(hero.day), True, white)
                        screen.blit(text, [1333, 743])
                        text = font.render(str("День:"), True, white)
                        screen.blit(text, [1288, 743])
                        if hero.Mana >= 10:
                            text = font.render(str(hero.Mana), True, white)
                            screen.blit(text, [1323, 631])
                        else:
                            text = font.render(str(hero.Mana), True, white)
                            screen.blit(text, [1327, 631])
                        screen.blit(Hero_face, hero_face)
                        Zadershka()
                        Castle.castle_draw(screen)

                elif End_Turn_Checker == 1 and (int(event.pos[0]) >= 1212 and int(event.pos[1]) >= 456 and int(event.pos[0]) <= 1291 and int(event.pos[1] <= 496)) and Hero_Window == False and Do_Check == False:
                    if hero.postroika_v_den == 0:
                        hero.postroika_v_den = 1
                    while checker_image_10 != 10:
                        if checker_image_10 == 0:
                            screen.blit(End_timer_bg, [1117, 498])
                            screen.blit(End_timer_1, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 1:
                            screen.blit(End_timer_2, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 2:
                            screen.blit(End_timer_3, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 3:
                            screen.blit(End_timer_4, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 4:
                            screen.blit(End_timer_5, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 5:
                            screen.blit(End_timer_6, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 6:
                            screen.blit(End_timer_7, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 7:
                            screen.blit(End_timer_8, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 8:
                            screen.blit(End_timer_9, [1220, 602])
                            Zadershka_X5()
                        elif checker_image_10 == 9:
                            screen.blit(End_timer_10, [1220, 602])
                            Zadershka_X5()
                        checker_image_10 = checker_image_10 + 1
                    checker_image_10 = 0
                    hero.end_turn()
                    save_x1 = 0
                    save_y1 = 0
                Castle_Checker = False
                Hero_Checker = False
                End_Turn_Checker = False


if __name__ == '__main__':
    main()