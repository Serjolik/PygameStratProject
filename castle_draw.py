import pygame
import os
from castle import Castle

black = (0, 0, 0)

class castle():
    def __init__(self):
        self.Plus_x = 200
        self.Plus_y = 50
        self.castle = Castle()
        self.game_over = False
        self.all_game_over = False
        self.blue = pygame.Color(0, 255, 255)
        self.Fon_for_castle = pygame.image.load(os.path.join('Textures', "castle_materials", "Fon_For_Castle.png"))
        self.fix_castle = pygame.image.load(os.path.join('Textures', "castle_materials", "fix_castle.png"))
        self.eath = pygame.image.load(os.path.join('Textures', "castle_materials", "TBcsback.png")).convert()
        self.tavern1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsTav1.png")).convert()
        self.tavern2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsTav2.png")).convert()
        self.capitol1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH101.png")).convert()
        self.capitol2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH201.png")).convert()
        self.capitol3 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH301.png")).convert()
        self.capitol4 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH401.png")).convert()
        self.castle1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsCas1.png")).convert()
        self.castle2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCscas2.png")).convert()
        self.castle3 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsCas3.png")).convert()
        self.shop1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsMrk1.png")).convert()
        self.shop2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsMrk2.png")).convert()
        self.mage1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsMag1.png")).convert()
        self.mage2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsMag2.png")).convert()
        self.mage3 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM301.png")).convert()
        self.mage4 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM401.png")).convert()
        self.stablesd = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsCavM.png")).convert()
        self.training1 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc101.png")).convert()
        self.training2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc201.png")).convert()
        self.grifin1 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsgr1h.png")).convert()
        self.grifin2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsgr2h.png")).convert()
        self.barracks1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsSwd1.png")).convert()
        self.barracks2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsswd2.png")).convert()
        self.guardhouse1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsPik1.png")).convert()
        self.guardhouse2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcspik2.png")).convert()
        self.archershouse1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsCrs1.png")).convert()
        self.archershouse2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcscrs2.png")).convert()
        self.monastary1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsMon1.png")).convert()
        self.monastary2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsmon2.png")).convert()
        self.portalgl1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsAng1.png")).convert()
        self.portalgl2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsang2.png")).convert()
        self.an_cap11 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH102.png")).convert()
        self.an_cap12 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH103.png")).convert()
        self.an_cap13 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH104.png")).convert()
        self.an_cap14 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH105.png")).convert()
        self.an_cap15 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH106.png")).convert()
        self.an_cap16 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH107.png")).convert()
        self.an_cap17 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH108.png")).convert()
        self.an_cap18 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH109.png")).convert()
        self.an_cap19 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH110.png")).convert()
        self.an_cap21 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH202.png")).convert()
        self.an_cap22 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH203.png")).convert()
        self.an_cap23 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH204.png")).convert()
        self.an_cap24 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH205.png")).convert()
        self.an_cap25 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH206.png")).convert()
        self.an_cap26 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH207.png")).convert()
        self.an_cap27 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH208.png")).convert()
        self.an_cap28 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH209.png")).convert()
        self.an_cap29 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH210.png")).convert()
        self.an_cap31 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH302.png")).convert()
        self.an_cap32 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH303.png")).convert()
        self.an_cap33 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH304.png")).convert()
        self.an_cap34 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH305.png")).convert()
        self.an_cap35 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH306.png")).convert()
        self.an_cap36 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH307.png")).convert()
        self.an_cap37 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH308.png")).convert()
        self.an_cap38 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH309.png")).convert()
        self.an_cap39 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH310.png")).convert()
        self.an_cap41 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH402.png")).convert()
        self.an_cap42 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH403.png")).convert()
        self.an_cap43 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH404.png")).convert()
        self.an_cap44 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH405.png")).convert()
        self.an_cap45 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH406.png")).convert()
        self.an_cap46 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH407.png")).convert()
        self.an_cap47 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH408.png")).convert()
        self.an_cap48 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH409.png")).convert()
        self.an_cap49 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsH410.png")).convert()
        self.an_mag31 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM302.png")).convert()
        self.an_mag32 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM303.png")).convert()
        self.an_mag33 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM304.png")).convert()
        self.an_mag34 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM305.png")).convert()
        self.an_mag35 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM306.png")).convert()
        self.an_mag36 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM307.png")).convert()
        self.an_mag37 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM308.png")).convert()
        self.an_mag38 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM309.png")).convert()
        self.an_mag39 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM310.png")).convert()
        self.an_mag310 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM311.png")).convert()
        self.an_mag41 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM402.png")).convert()
        self.an_mag42 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM403.png")).convert()
        self.an_mag43 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM404.png")).convert()
        self.an_mag44 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM405.png")).convert()
        self.an_mag45 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM406.png")).convert()
        self.an_mag46 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM407.png")).convert()
        self.an_mag47 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM408.png")).convert()
        self.an_mag48 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM409.png")).convert()
        self.an_mag49 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM410.png")).convert()
        self.an_mag410 = pygame.image.load(os.path.join('Textures', "castle_materials", "TBCsM411.png")).convert()
        self.an_tr1 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc102.png")).convert()
        self.an_tr2 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc103.png")).convert()
        self.an_tr3 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc104.png")).convert()
        self.an_tr4 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc105.png")).convert()
        self.an_tr5 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc106.png")).convert()
        self.an_tr6 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc107.png")).convert()
        self.an_tr7 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc108.png")).convert()
        self.an_tr8 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc109.png")).convert()
        self.an_tr9 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc110.png")).convert()
        self.an_tr11 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc202.png")).convert()
        self.an_tr12 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc203.png")).convert()
        self.an_tr13 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc204.png")).convert()
        self.an_tr14 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc205.png")).convert()
        self.an_tr15 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc206.png")).convert()
        self.an_tr16 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc207.png")).convert()
        self.an_tr17 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc208.png")).convert()
        self.an_tr18 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc209.png")).convert()
        self.an_tr19 = pygame.image.load(os.path.join('Textures', "castle_materials", "tbcsc210.png")).convert()
        self.water1 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf01.png")).convert()
        self.water2 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf02.png")).convert()
        self.water3 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf03.png")).convert()
        self.water4 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf04.png")).convert()
        self.water5 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf05.png")).convert()
        self.water6 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf06.png")).convert()
        self.water7 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf07.png")).convert()
        self.water8 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf08.png")).convert()
        self.water9 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf09.png")).convert()
        self.water10 = pygame.image.load(os.path.join('Textures', "castle_materials", "TACsWf10.png")).convert()
        self.up = pygame.image.load(os.path.join('Textures', "castle_materials", "1.png")).convert()
        self.up_cap1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsHal1.png")).convert()
        self.up_cap2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsHal2.png")).convert()
        self.up_cap3 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsHal3.png")).convert()
        self.up_cap4 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsHal4.png")).convert()
        self.up_mag1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMag1.png")).convert()
        self.up_mag2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMag2.png")).convert()
        self.up_mag3 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMag3.png")).convert()
        self.up_mag4 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMag4.png")).convert()
        self.up_tav1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsTav1.png")).convert()
        self.up_tav2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsTav2.png")).convert()
        self.up_cas1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCas1.png")).convert()
        self.up_cas2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCas2.png")).convert()
        self.up_cas3 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCas3.png")).convert()
        self.up_arch1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCrs1.png")).convert()
        self.up_arch2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCrs2.png")).convert()
        self.up_tr1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCv1.png")).convert()
        self.up_tr2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCv2.png")).convert()
        self.up_st = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsCv2S.png")).convert()
        self.up_gr1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsGr1H.png")).convert()
        self.up_gr2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsGr2H.png")).convert()
        self.up_mon1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMon1.png")).convert()
        self.up_mon2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMon2.png")).convert()
        self.up_shop1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMrk1.png")).convert()
        self.up_shop2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsMrk2.png")).convert()
        self.up_guard1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsPik1.png")).convert()
        self.up_guard2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsPik2.png")).convert()
        self.up_bar1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsSwd1.png")).convert()
        self.up_bar2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsSwd2.png")).convert()
        self.up_portal1 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsAng1.png")).convert()
        self.up_portal2 = pygame.image.load(os.path.join('Textures', "castle_materials", "ThCsAng2.png")).convert()
        self.tcap = 0
        self.tmag = 0
        self.x = 0
        self.y = 0

    def castle_draw(self, screen):
        self.game_over = False
        touch = 0
        while not self.game_over:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game_over = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and touch == 0:
                        self.game_over = True
                    if event.key == pygame.K_ESCAPE and touch == 1:
                        touch = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= 210 and event.pos[0] <= 375 and event.pos[1] <= 375 and event.pos[
                        1] >= 235 and touch == 0:
                        self.x = event.pos[0]
                        self.y = event.pos[1]
                        touch = 1

                    if touch == 1 and event.pos[0] >= (39 + self.Plus_x) and event.pos[0] <= (189 + self.Plus_x) and \
                            event.pos[1] >= (21 + self.Plus_y) and event.pos[1] <= (91 + self.Plus_y):
                        self.castle.upgr_cap()
                    if touch == 1 and event.pos[0] >= (229 + self.Plus_x) and event.pos[0] <= (379 + self.Plus_x) and \
                            event.pos[1] >= (21 + self.Plus_y) and event.pos[1] <= (91 + self.Plus_y):
                        self.castle.upgr_cast()
                    if touch == 1 and event.pos[0] >= (419 + self.Plus_x) and event.pos[0] <= (569 + self.Plus_x) and \
                            event.pos[1] >= (21 + self.Plus_y) and event.pos[1] <= (91 + self.Plus_y):
                        self.castle.upgr_tav()
                    if touch == 1 and event.pos[0] >= (609 + self.Plus_x) and event.pos[0] <= (759 + self.Plus_x) and \
                            event.pos[1] >= (21 + self.Plus_y) and event.pos[1] <= (91 + self.Plus_y):
                        self.castle.upgr_guard()
                    if touch == 1 and event.pos[0] >= (136 + self.Plus_x) and event.pos[0] <= (286 + self.Plus_x) and \
                            event.pos[1] >= (101 + self.Plus_y) and event.pos[1] <= (171 + self.Plus_y):
                        self.castle.upgr_shop()
                    if touch == 1 and event.pos[0] >= (326 + self.Plus_x) and event.pos[0] <= (476 + self.Plus_x) and \
                            event.pos[1] >= (101 + self.Plus_y) and event.pos[1] <= (171 + self.Plus_y):
                        self.castle.upgr_mage()
                    if touch == 1 and event.pos[0] >= (516 + self.Plus_x) and event.pos[0] <= (666 + self.Plus_x) and \
                            event.pos[1] >= (101 + self.Plus_y) and event.pos[1] <= (171 + self.Plus_y):
                        self.castle.upgr_arch()
                    if touch == 1 and event.pos[0] >= (229 + self.Plus_x) and event.pos[0] <= (379 + self.Plus_x) and \
                            event.pos[1] >= (181 + self.Plus_y) and event.pos[1] <= (251 + self.Plus_y):
                        self.castle.upgr_stables()
                    if touch == 1 and event.pos[0] >= (419 + self.Plus_x) and event.pos[0] <= (569 + self.Plus_x) and \
                            event.pos[1] >= (181 + self.Plus_y) and event.pos[1] <= (251 + self.Plus_y):
                        self.castle.upgr_grif()
                    if touch == 1 and event.pos[0] >= (39 + self.Plus_x) and event.pos[0] <= (189 + self.Plus_x) and \
                            event.pos[1] >= (261 + self.Plus_y) and event.pos[1] <= (331 + self.Plus_y) and event.pos[
                        0] != self.x and event.pos[1] != self.y:
                        self.castle.upgr_bar()
                    if touch == 1 and event.pos[0] >= (229 + self.Plus_x) and event.pos[0] <= (379 + self.Plus_x) and \
                            event.pos[1] >= (261 + self.Plus_y) and event.pos[1] <= (331 + self.Plus_y):
                        self.castle.upgr_mon()
                    if touch == 1 and event.pos[0] >= (419 + self.Plus_x) and event.pos[0] <= (569 + self.Plus_x) and \
                            event.pos[1] >= (261 + self.Plus_y) and event.pos[1] <= (331 + self.Plus_y):
                        self.castle.upgr_train()
                    if touch == 1 and event.pos[0] >= (609 + self.Plus_x) and event.pos[0] <= (759 + self.Plus_x) and \
                            event.pos[1] >= (261 + self.Plus_y) and event.pos[1] <= (331 + self.Plus_y):
                        self.castle.upgr_portal()

            draw_eath = self.eath.get_rect(center=(600, 284))
            screen.blit(self.eath, draw_eath)
            Fon = self.Fon_for_castle.get_rect(center=(600, 340))
            screen.blit(self.Fon_for_castle, Fon)
            self.tcap = (self.tcap + 1) % 9
            self.tmag = (self.tmag + 1) % 10

            if self.castle.lvl_portalgl == 1:
                self.portalgl1.set_colorkey(self.blue)
                draw_portalgl = self.portalgl1.get_rect(center=(445 + self.Plus_x, 61 + self.Plus_y))
                screen.blit(self.portalgl1, draw_portalgl)
            elif self.castle.lvl_portalgl == 2:
                self.portalgl2.set_colorkey(self.blue)
                draw_portalgl = self.portalgl2.get_rect(center=(445 + self.Plus_x, 61 + self.Plus_y))
                screen.blit(self.portalgl2, draw_portalgl)
            if self.castle.lvl_stables == 1:
                self.stablesd.set_colorkey(self.blue)
                draw_stables = self.stablesd.get_rect(center=(435 + self.Plus_x, 225 + self.Plus_y))
                screen.blit(self.stablesd, draw_stables)
            if self.castle.lvl_training == 1:
                self.training1.set_colorkey(self.blue)
                draw_training = self.training1.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                screen.blit(self.training1, draw_training)
                if self.tcap == 0:
                    self.an_tr1.set_colorkey(self.blue)
                    draw_antr = self.an_tr1.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr1, draw_antr)
                elif self.tcap == 1:
                    self.an_tr2.set_colorkey(self.blue)
                    draw_antr = self.an_tr2.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr2, draw_antr)
                elif self.tcap == 2:
                    self.an_tr3.set_colorkey(self.blue)
                    draw_antr = self.an_tr3.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr3, draw_antr)
                elif self.tcap == 3:
                    self.an_tr4.set_colorkey(self.blue)
                    draw_antr = self.an_tr4.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr4, draw_antr)
                elif self.tcap == 4:
                    self.an_tr5.set_colorkey(self.blue)
                    draw_antr = self.an_tr5.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr5, draw_antr)
                elif self.tcap == 5:
                    self.an_tr6.set_colorkey(self.blue)
                    draw_antr = self.an_tr6.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr6, draw_antr)
                elif self.tcap == 6:
                    self.an_tr7.set_colorkey(self.blue)
                    draw_antr = self.an_tr7.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr7, draw_antr)
                elif self.tcap == 7:
                    self.an_tr8.set_colorkey(self.blue)
                    draw_antr = self.an_tr8.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr8, draw_antr)
                elif self.tcap == 8:
                    self.an_tr9.set_colorkey(self.blue)
                    draw_antr = self.an_tr9.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr9, draw_antr)
            elif self.castle.lvl_training == 2:
                self.training2.set_colorkey(self.blue)
                draw_training = self.training2.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                screen.blit(self.training2, draw_training)
                if self.tcap == 0:
                    self.an_tr11.set_colorkey(self.blue)
                    draw_antr = self.an_tr11.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr11, draw_antr)
                elif self.tcap == 1:
                    self.an_tr12.set_colorkey(self.blue)
                    draw_antr = self.an_tr12.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr12, draw_antr)
                elif self.tcap == 2:
                    self.an_tr13.set_colorkey(self.blue)
                    draw_antr = self.an_tr13.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr13, draw_antr)
                elif self.tcap == 3:
                    self.an_tr14.set_colorkey(self.blue)
                    draw_antr = self.an_tr14.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr14, draw_antr)
                elif self.tcap == 4:
                    self.an_tr15.set_colorkey(self.blue)
                    draw_antr = self.an_tr15.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr15, draw_antr)
                elif self.tcap == 5:
                    self.an_tr16.set_colorkey(self.blue)
                    draw_antr = self.an_tr16.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr16, draw_antr)
                elif self.tcap == 6:
                    self.an_tr17.set_colorkey(self.blue)
                    draw_antr = self.an_tr17.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr17, draw_antr)
                elif self.tcap == 7:
                    self.an_tr18.set_colorkey(self.blue)
                    draw_antr = self.an_tr18.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr18, draw_antr)
                elif self.tcap == 8:
                    self.an_tr19.set_colorkey(self.blue)
                    draw_antr = self.an_tr19.get_rect(center=(300 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_tr19, draw_antr)

            if self.castle.lvl_capitol == 1:
                self.capitol1.set_colorkey(self.blue)
                draw_capitol = self.capitol1.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                screen.blit(self.capitol1, draw_capitol)
                if self.tcap == 0:
                    self.an_cap11.set_colorkey(self.blue)
                    draw_ancap = self.an_cap11.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap11, draw_ancap)
                elif self.tcap == 1:
                    self.an_cap12.set_colorkey(self.blue)
                    draw_ancap = self.an_cap12.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap12, draw_ancap)
                elif self.tcap == 2:
                    self.an_cap13.set_colorkey(self.blue)
                    draw_ancap = self.an_cap13.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap13, draw_ancap)
                elif self.tcap == 3:
                    self.an_cap14.set_colorkey(self.blue)
                    draw_ancap = self.an_cap14.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap14, draw_ancap)
                elif self.tcap == 4:
                    self.an_cap15.set_colorkey(self.blue)
                    draw_ancap = self.an_cap15.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap15, draw_ancap)
                elif self.tcap == 5:
                    self.an_cap16.set_colorkey(self.blue)
                    draw_ancap = self.an_cap16.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap16, draw_ancap)
                elif self.tcap == 6:
                    self.an_cap17.set_colorkey(self.blue)
                    draw_ancap = self.an_cap17.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap17, draw_ancap)
                elif self.tcap == 7:
                    self.an_cap18.set_colorkey(self.blue)
                    draw_ancap = self.an_cap18.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap18, draw_ancap)
                elif self.tcap == 8:
                    self.an_cap19.set_colorkey(self.blue)
                    draw_ancap = self.an_cap19.get_rect(center=(100 + self.Plus_x, 290 + self.Plus_y))
                    screen.blit(self.an_cap19, draw_ancap)



            elif self.castle.lvl_capitol == 2:
                self.capitol2.set_colorkey(self.blue)
                draw_capitol = self.capitol2.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                screen.blit(self.capitol2, draw_capitol)
                if self.tcap == 0:
                    self.an_cap21.set_colorkey(self.blue)
                    draw_ancap = self.an_cap21.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap21, draw_ancap)
                elif self.tcap == 1:
                    self.an_cap22.set_colorkey(self.blue)
                    draw_ancap = self.an_cap22.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap22, draw_ancap)
                elif self.tcap == 2:
                    self.an_cap23.set_colorkey(self.blue)
                    draw_ancap = self.an_cap23.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap23, draw_ancap)
                elif self.tcap == 3:
                    self.an_cap24.set_colorkey(self.blue)
                    draw_ancap = self.an_cap24.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap24, draw_ancap)
                elif self.tcap == 4:
                    self.an_cap25.set_colorkey(self.blue)
                    draw_ancap = self.an_cap25.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap25, draw_ancap)
                elif self.tcap == 5:
                    self.an_cap26.set_colorkey(self.blue)
                    draw_ancap = self.an_cap26.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap26, draw_ancap)
                elif self.tcap == 6:
                    self.an_cap27.set_colorkey(self.blue)
                    draw_ancap = self.an_cap27.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap27, draw_ancap)
                elif self.tcap == 7:
                    self.an_cap28.set_colorkey(self.blue)
                    draw_ancap = self.an_cap28.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap28, draw_ancap)
                elif self.tcap == 8:
                    self.an_cap29.set_colorkey(self.blue)
                    draw_ancap = self.an_cap29.get_rect(center=(100 + self.Plus_x, 270 + self.Plus_y))
                    screen.blit(self.an_cap29, draw_ancap)
            elif self.castle.lvl_capitol == 3:
                self.capitol3.set_colorkey(self.blue)
                draw_capitol = self.capitol3.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                screen.blit(self.capitol3, draw_capitol)
                if self.tcap == 0:
                    self.an_cap31.set_colorkey(self.blue)
                    draw_ancap = self.an_cap31.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap31, draw_ancap)
                elif self.tcap == 1:
                    self.an_cap32.set_colorkey(self.blue)
                    draw_ancap = self.an_cap32.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap32, draw_ancap)
                elif self.tcap == 2:
                    self.an_cap33.set_colorkey(self.blue)
                    draw_ancap = self.an_cap33.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap33, draw_ancap)
                elif self.tcap == 3:
                    self.an_cap34.set_colorkey(self.blue)
                    draw_ancap = self.an_cap34.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap34, draw_ancap)
                elif self.tcap == 4:
                    self.an_cap35.set_colorkey(self.blue)
                    draw_ancap = self.an_cap35.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap35, draw_ancap)
                elif self.tcap == 5:
                    self.an_cap36.set_colorkey(self.blue)
                    draw_ancap = self.an_cap36.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap36, draw_ancap)
                elif self.tcap == 6:
                    self.an_cap37.set_colorkey(self.blue)
                    draw_ancap = self.an_cap37.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap37, draw_ancap)
                elif self.tcap == 7:
                    self.an_cap38.set_colorkey(self.blue)
                    draw_ancap = self.an_cap38.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap38, draw_ancap)
                elif self.tcap == 8:
                    self.an_cap39.set_colorkey(self.blue)
                    draw_ancap = self.an_cap39.get_rect(center=(100 + self.Plus_x, 260 + self.Plus_y))
                    screen.blit(self.an_cap39, draw_ancap)
            elif self.castle.lvl_capitol == 4:
                self.capitol4.set_colorkey(self.blue)
                draw_capitol = self.capitol4.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                screen.blit(self.capitol4, draw_capitol)
                if self.tcap == 0:
                    self.an_cap41.set_colorkey(self.blue)
                    draw_ancap = self.an_cap41.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap41, draw_ancap)
                elif self.tcap == 1:
                    self.an_cap42.set_colorkey(self.blue)
                    draw_ancap = self.an_cap42.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap42, draw_ancap)
                elif self.tcap == 2:
                    self.an_cap43.set_colorkey(self.blue)
                    draw_ancap = self.an_cap43.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap43, draw_ancap)
                elif self.tcap == 3:
                    self.an_cap44.set_colorkey(self.blue)
                    draw_ancap = self.an_cap44.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap44, draw_ancap)
                elif self.tcap == 4:
                    self.an_cap45.set_colorkey(self.blue)
                    draw_ancap = self.an_cap45.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap45, draw_ancap)
                elif self.tcap == 5:
                    self.an_cap46.set_colorkey(self.blue)
                    draw_ancap = self.an_cap46.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap46, draw_ancap)
                elif self.tcap == 6:
                    self.an_cap47.set_colorkey(self.blue)
                    draw_ancap = self.an_cap47.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap47, draw_ancap)
                elif self.tcap == 7:
                    self.an_cap48.set_colorkey(self.blue)
                    draw_ancap = self.an_cap48.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap48, draw_ancap)
                elif self.tcap == 8:
                    self.an_cap49.set_colorkey(self.blue)
                    draw_ancap = self.an_cap49.get_rect(center=(100 + self.Plus_x, 250 + self.Plus_y))
                    screen.blit(self.an_cap49, draw_ancap)
            if self.castle.lvl_tavern == 1:
                self.tavern1.set_colorkey(self.blue)
                draw_tavern = self.tavern1.get_rect(center=(30 + self.Plus_x, 320 + self.Plus_y))
                screen.blit(self.tavern1, draw_tavern)
            elif self.castle.lvl_tavern == 2:
                self.tavern2.set_colorkey(self.blue)
                draw_tavern = self.tavern2.get_rect(center=(30 + self.Plus_x, 300 + self.Plus_y))
                screen.blit(self.tavern2, draw_tavern)
            if self.castle.lvl_grifin == 1:
                self.grifin1.set_colorkey(self.blue)
                draw_grifin_bastion = self.grifin1.get_rect(center=(125 + self.Plus_x, 115 + self.Plus_y))
                screen.blit(self.grifin1, draw_grifin_bastion)
            elif self.castle.lvl_grifin == 2:
                self.grifin2.set_colorkey(self.blue)
                draw_grifin_bastion = self.grifin2.get_rect(center=(125 + self.Plus_x, 115 + self.Plus_y))
                screen.blit(self.grifin2, draw_grifin_bastion)
            if self.castle.lvl_guardhouse == 1:
                self.guardhouse1.set_colorkey(self.blue)
                draw_guard_house = self.guardhouse1.get_rect(center=(334 + self.Plus_x, 136 + self.Plus_y))
                screen.blit(self.guardhouse1, draw_guard_house)
            elif self.castle.lvl_guardhouse == 2:
                self.guardhouse2.set_colorkey(self.blue)
                draw_guard_house = self.guardhouse2.get_rect(center=(340 + self.Plus_x, 123 + self.Plus_y))
                screen.blit(self.guardhouse2, draw_guard_house)
            if self.castle.lvl_barracks == 1:
                self.barracks1.set_colorkey(self.blue)
                draw_barracks = self.barracks1.get_rect(center=(248 + self.Plus_x, 135 + self.Plus_y))
                screen.blit(self.barracks1, draw_barracks)
            elif self.castle.lvl_barracks == 2:
                self.barracks2.set_colorkey(self.blue)
                draw_barracks = self.barracks2.get_rect(center=(250 + self.Plus_x, 124 + self.Plus_y))
                screen.blit(self.barracks2, draw_barracks)
            if self.castle.lvl_archershouse == 1:
                self.archershouse1.set_colorkey(self.blue)
                draw_archers_house = self.archershouse1.get_rect(center=(418 + self.Plus_x, 161 + self.Plus_y))
                screen.blit(self.archershouse1, draw_archers_house)
            elif self.castle.lvl_archershouse == 2:
                self.archershouse2.set_colorkey(self.blue)
                draw_archers_house = self.archershouse2.get_rect(center=(418 + self.Plus_x, 155 + self.Plus_y))
                screen.blit(self.archershouse2, draw_archers_house)
            if self.castle.lvl_castle == 1:
                self.castle1.set_colorkey(self.blue)
                draw_castle = self.castle1.get_rect(center=(658 + self.Plus_x, 142 + self.Plus_y))
                screen.blit(self.castle1, draw_castle)
            elif self.castle.lvl_castle == 2:
                self.castle2.set_colorkey(self.blue)
                draw_castle = self.castle2.get_rect(center=(639 + self.Plus_x, 157 + self.Plus_y))
                screen.blit(self.castle2, draw_castle)
            elif self.castle.lvl_castle == 3:
                self.castle3.set_colorkey(self.blue)
                draw_castle = self.castle3.get_rect(center=(639 + self.Plus_x, 142 + self.Plus_y))
                screen.blit(self.castle3, draw_castle)
            if self.castle.lvl_shop == 2:
                self.shop2.set_colorkey(self.blue)
                draw_silo = self.shop2.get_rect(center=(510 + self.Plus_x, 264 + self.Plus_y))
                screen.blit(self.shop2, draw_silo)
                self.shop1.set_colorkey(self.blue)
                draw_shop = self.shop1.get_rect(center=(560 + self.Plus_x, 318 + self.Plus_y))
                screen.blit(self.shop1, draw_shop)
            elif self.castle.lvl_shop == 1:
                self.shop1.set_colorkey(self.blue)
                draw_shop = self.shop1.get_rect(center=(560 + self.Plus_x, 318 + self.Plus_y))
                screen.blit(self.shop1, draw_shop)
            if self.castle.lvl_mage == 1:
                self.mage1.set_colorkey(self.blue)
                draw_magegild = self.mage1.get_rect(center=(753 + self.Plus_x, 217 + self.Plus_y))
                screen.blit(self.mage1, draw_magegild)
            elif self.castle.lvl_mage == 2:
                self.mage2.set_colorkey(self.blue)
                draw_magegild = self.mage2.get_rect(center=(753 + self.Plus_x, 205 + self.Plus_y))
                screen.blit(self.mage2, draw_magegild)
            elif self.castle.lvl_mage == 3:
                self.mage3.set_colorkey(self.blue)
                draw_magegild = self.mage3.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                screen.blit(self.mage3, draw_magegild)
                if self.tmag == 0:
                    self.an_mag31.set_colorkey(self.blue)
                    draw_anmag = self.an_mag31.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag31, draw_anmag)
                elif self.tmag == 0:
                    self.an_mag31.set_colorkey(self.blue)
                    draw_anmag = self.an_mag31.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag31, draw_anmag)
                elif self.tmag == 1:
                    self.an_mag32.set_colorkey(self.blue)
                    draw_anmag = self.an_mag32.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag32, draw_anmag)
                elif self.tmag == 2:
                    self.an_mag33.set_colorkey(self.blue)
                    draw_anmag = self.an_mag33.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag33, draw_anmag)
                elif self.tmag == 3:
                    self.an_mag34.set_colorkey(self.blue)
                    draw_anmag = self.an_mag34.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag34, draw_anmag)
                elif self.tmag == 4:
                    self.an_mag35.set_colorkey(self.blue)
                    draw_anmag = self.an_mag35.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag35, draw_anmag)
                elif self.tmag == 5:
                    self.an_mag36.set_colorkey(self.blue)
                    draw_anmag = self.an_mag36.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag36, draw_anmag)
                elif self.tmag == 6:
                    self.an_mag37.set_colorkey(self.blue)
                    draw_anmag = self.an_mag37.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag37, draw_anmag)
                elif self.tmag == 7:
                    self.an_mag38.set_colorkey(self.blue)
                    draw_anmag = self.an_mag38.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag38, draw_anmag)
                elif self.tmag == 8:
                    self.an_mag39.set_colorkey(self.blue)
                    draw_anmag = self.an_mag39.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag39, draw_anmag)
                elif self.tmag == 9:
                    self.an_mag310.set_colorkey(self.blue)
                    draw_anmag = self.an_mag310.get_rect(center=(754 + self.Plus_x, 190 + self.Plus_y))
                    screen.blit(self.an_mag310, draw_anmag)

            elif self.castle.lvl_mage == 4:
                self.mage4.set_colorkey(self.blue)
                draw_magegild = self.mage4.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                screen.blit(self.mage4, draw_magegild)
                if self.tmag == 0:
                    self.an_mag41.set_colorkey(self.blue)
                    draw_anmag = self.an_mag41.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag41, draw_anmag)
                elif self.tmag == 1:
                    self.an_mag42.set_colorkey(self.blue)
                    draw_anmag = self.an_mag42.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag42, draw_anmag)
                elif self.tmag == 2:
                    self.an_mag43.set_colorkey(self.blue)
                    draw_anmag = self.an_mag43.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag43, draw_anmag)
                elif self.tmag == 3:
                    self.an_mag44.set_colorkey(self.blue)
                    draw_anmag = self.an_mag44.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag44, draw_anmag)
                elif self.tmag == 4:
                    self.an_mag45.set_colorkey(self.blue)
                    draw_anmag = self.an_mag45.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag45, draw_anmag)
                elif self.tmag == 5:
                    self.an_mag46.set_colorkey(self.blue)
                    draw_anmag = self.an_mag46.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag46, draw_anmag)
                elif self.tmag == 6:
                    self.an_mag47.set_colorkey(self.blue)
                    draw_anmag = self.an_mag47.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag47, draw_anmag)
                elif self.tmag == 7:
                    self.an_mag48.set_colorkey(self.blue)
                    draw_anmag = self.an_mag48.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag48, draw_anmag)
                elif self.tmag == 8:
                    self.an_mag49.set_colorkey(self.blue)
                    draw_anmag = self.an_mag49.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag49, draw_anmag)
                elif self.tmag == 9:
                    self.an_mag410.set_colorkey(self.blue)
                    draw_anmag = self.an_mag410.get_rect(center=(754 + self.Plus_x, 175 + self.Plus_y))
                    screen.blit(self.an_mag410, draw_anmag)
            if self.castle.lvl_monastary == 1:
                self.monastary1.set_colorkey(self.blue)
                draw_monastary = self.monastary1.get_rect(center=(633 + self.Plus_x, 240 + self.Plus_y))
                screen.blit(self.monastary1, draw_monastary)
            elif self.castle.lvl_monastary == 2:
                self.monastary2.set_colorkey(self.blue)
                draw_monastary = self.monastary2.get_rect(center=(633 + self.Plus_x, 218 + self.Plus_y))
                screen.blit(self.monastary2, draw_monastary)
            if self.tmag == 0:
                draw_water = self.water1.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water1, draw_water)
            if self.tmag == 1:
                draw_water = self.water2.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water2, draw_water)
            if self.tmag == 2:
                draw_water = self.water3.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water3, draw_water)
            if self.tmag == 3:
                draw_water = self.water4.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water4, draw_water)
            if self.tmag == 4:
                draw_water = self.water5.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water5, draw_water)
            if self.tmag == 5:
                draw_water = self.water6.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water6, draw_water)
            if self.tmag == 6:
                draw_water = self.water7.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water7, draw_water)
            if self.tmag == 7:
                draw_water = self.water8.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water8, draw_water)
            if self.tmag == 8:
                draw_water = self.water9.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water9, draw_water)
            if self.tmag == 9:
                draw_water = self.water10.get_rect(center=(60 + self.Plus_x, 141 + self.Plus_y))
                screen.blit(self.water10, draw_water)

            Fix_castle = self.fix_castle.get_rect(center=(600, 340))
            screen.blit(self.fix_castle, Fix_castle)
            if touch == 1:
                draw_up = self.up.get_rect(center=(601, 258))
                screen.blit(self.up, draw_up)
                if self.castle.lvl_capitol == 1:
                    draw_upcap = self.up_cap1.get_rect(center=(114 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cap1, draw_upcap)
                if self.castle.lvl_capitol == 2:
                    draw_upcap = self.up_cap2.get_rect(center=(114 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cap2, draw_upcap)
                if self.castle.lvl_capitol == 3:
                    draw_upcap = self.up_cap3.get_rect(center=(114 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cap3, draw_upcap)
                if self.castle.lvl_capitol == 4:
                    draw_upcap = self.up_cap4.get_rect(center=(114 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cap4, draw_upcap)
                if self.castle.lvl_castle == 1:
                    draw_upcas = self.up_cas1.get_rect(center=(306 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cas1, draw_upcas)
                if self.castle.lvl_castle == 2:
                    draw_upcas = self.up_cas2.get_rect(center=(306 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cas2, draw_upcas)
                if self.castle.lvl_castle == 3:
                    draw_upcas = self.up_cas3.get_rect(center=(306 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_cas3, draw_upcas)
                if self.castle.lvl_tavern == 1:
                    draw_uptav = self.up_tav1.get_rect(center=(498 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_tav1, draw_uptav)
                if self.castle.lvl_tavern == 2:
                    draw_uptav = self.up_tav2.get_rect(center=(498 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_tav2, draw_uptav)
                if self.castle.lvl_shop == 1:
                    draw_upsh = self.up_shop1.get_rect(center=(209 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_shop1, draw_upsh)
                if self.castle.lvl_shop == 2:
                    draw_upsh = self.up_shop2.get_rect(center=(209 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_shop2, draw_upsh)
                if self.castle.lvl_mage == 1:
                    draw_upmag = self.up_mag1.get_rect(center=(401 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_mag1, draw_upmag)
                if self.castle.lvl_mage == 2:
                    draw_upmag = self.up_mag2.get_rect(center=(401 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_mag2, draw_upmag)
                if self.castle.lvl_mage == 3:
                    draw_upmag = self.up_mag3.get_rect(center=(401 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_mag3, draw_upmag)
                if self.castle.lvl_mage == 4:
                    draw_upmag = self.up_mag4.get_rect(center=(401 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_mag4, draw_upmag)
                if self.castle.lvl_stables == 1:
                    draw_upst = self.up_st.get_rect(center=(305 + self.Plus_x, 217 + self.Plus_y))
                    screen.blit(self.up_st, draw_upst)
                if self.castle.lvl_grifin == 1:
                    draw_upgrif = self.up_gr1.get_rect(center=(498 + self.Plus_x, 217 + self.Plus_y))
                    screen.blit(self.up_gr1, draw_upgrif)
                if self.castle.lvl_grifin == 2:
                    draw_upgrif = self.up_gr2.get_rect(center=(498 + self.Plus_x, 217 + self.Plus_y))
                    screen.blit(self.up_gr2, draw_upgrif)
                if self.castle.lvl_guardhouse == 1:
                    draw_upguard = self.up_guard1.get_rect(center=(690 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_guard1, draw_upguard)
                if self.castle.lvl_guardhouse == 2:
                    draw_upguard = self.up_guard2.get_rect(center=(690 + self.Plus_x, 56 + self.Plus_y))
                    screen.blit(self.up_guard2, draw_upguard)
                if self.castle.lvl_archershouse == 1:
                    draw_uparch = self.up_arch1.get_rect(center=(593 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_arch1, draw_uparch)
                if self.castle.lvl_archershouse == 2:
                    draw_uparch = self.up_arch2.get_rect(center=(593 + self.Plus_x, 137 + self.Plus_y))
                    screen.blit(self.up_arch2, draw_uparch)
                if self.castle.lvl_barracks == 1:
                    draw_upbar = self.up_bar1.get_rect(center=(114 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_bar1, draw_upbar)
                if self.castle.lvl_barracks == 2:
                    draw_upbar = self.up_bar2.get_rect(center=(114 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_bar2, draw_upbar)
                if self.castle.lvl_monastary == 1:
                    draw_upmon = self.up_mon1.get_rect(center=(306 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_mon1, draw_upmon)
                if self.castle.lvl_monastary == 2:
                    draw_upmon = self.up_mon2.get_rect(center=(306 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_mon2, draw_upmon)
                if self.castle.lvl_training == 1:
                    draw_uptr = self.up_tr1.get_rect(center=(498 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_tr1, draw_uptr)
                if self.castle.lvl_training == 2:
                    draw_uptr = self.up_tr2.get_rect(center=(498 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_tr2, draw_uptr)
                if self.castle.lvl_portalgl == 1:
                    draw_upportal = self.up_portal1.get_rect(center=(690 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_portal1, draw_upportal)
                if self.castle.lvl_portalgl == 2:
                    draw_upportal = self.up_portal2.get_rect(center=(690 + self.Plus_x, 297 + self.Plus_y))
                    screen.blit(self.up_portal2, draw_upportal)

            pygame.display.flip()
            pygame.time.wait(60)