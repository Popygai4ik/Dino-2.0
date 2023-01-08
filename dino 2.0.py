# ----------------------------------------------------------------
# Пропишем основные импорты
# ----------------------------------------------------------------
#  Импортируем библеотеку pygame
import pygame
#  Импортируем библеотеку sys
import sys
# Из библеотеки random раздел choice
from random import choice
# Из библеотеки random раздел randit
from random import randint

# ----------------------------------------------------------------
# Выставляем основные элементы
# ----------------------------------------------------------------
# Инициализируем pygame
pygame.init()
# Инициализируем иконку приложения
icon = pygame.image.load('data/dino/динозавр для игры 1(стоит).png')
# Установим иконку приложения
pygame.display.set_icon(icon)
# Обозначаем размер окна
size = width, height = 800, 400
# Выставляем значение кол-во кадров
FPS = 60
# Выставляем размер окна
screen = pygame.display.set_mode(size)
# Обозначаем название нашей игры
pygame.display.set_caption('Dino 2.0')
# Обозначаем время
clock = pygame.time.Clock()
# Выставляем размер шрифта
size_shrift = 20
# Добавляем шрифт
shrift = pygame.font.Font('data/font/Sonic 1 Title Screen Filled.ttf', size_shrift)
# Добавлем время начала игры
start_time = 0
# Добавлем счет
score = 0
# ----------------------------------------------------------------
# Добавляем музыку
# ----------------------------------------------------------------
# Добавляем фоновую музыку
fon_music = pygame.mixer.Sound('data/music/(fon)e4c1fdca51422a9.mp3')
# Начинаем проигровать фоновую музыку
fon_music.play(loops=-1)
fon2_music = pygame.mixer.Sound('data/music/(fon)48bb90af8e1e401.mp3')
# Добавляем звук проигрыша
lose_music = pygame.mixer.Sound('data/music/jg-032316-sfx-video-game-game-over-3.mp3')
# ----------------------------------------------------------------
# Дообавляем фон нашей игры
# ----------------------------------------------------------------
# Добалем фоновое изображение для старта игры
start_fon = pygame.image.load('data/start_screen/210420200620119050.jpg')
# Добалем фоновое изображение для смерти в игре
lose_fon = pygame.image.load('data/lose_screen/iow_dinosaurisle.jpg')
# Добавляем небо
sky = pygame.image.load("data/sky/небо для игры.png")
# Добавлем землю
land = pygame.image.load("data/land/земля для игры.png")
# ----------------------------------------------------------------
# Добавляем паучка в нашу игру
# ----------------------------------------------------------------
#  Добавляем 1 изображение
spider_frame_1 = pygame.image.load('data/spider/паук для игры 1.png').convert_alpha()
# Добавляем 2 изображение
spider_frame_2 = pygame.image.load('data/spider/паук для игры 2.png').convert_alpha()
# Объединяем изображения
spider_frames = [spider_frame_1, spider_frame_2]
# Добавляем значение анимации
spider_frame_index = 0
# Добавляем анимацию
snail_surf = spider_frames[spider_frame_index]
# ----------------------------------------------------------------
# Добавляем стрекозу в нашу игру
# ----------------------------------------------------------------
#  Добавляем 1 изображение
dragonfly_frame1 = pygame.image.load('data/dragonfly/стрекоза для игры 1.png').convert_alpha()
# Добавляем 2 изображение
dragonfly_frame2 = pygame.image.load('data/dragonfly/стрекоза для игры 2.png').convert_alpha()
# Объединяем изображения
dragonfly_frames = [dragonfly_frame1, dragonfly_frame2]
# Добавляем значение анимации
dragonfly_frame_index = 0
# Добавляем анимацию
dragonfly_surf = dragonfly_frames[dragonfly_frame_index]


# ----------------------------------------------------------------
# Функция terminate
# ----------------------------------------------------------------
def terminate():
    pygame.quit()
    sys.exit()


# ----------------------------------------------------------------
# Класс Дино
# ----------------------------------------------------------------
class dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i = 0
        # ----------------------------------------------------------------
        # Дообавляем динозаврика в нашу игру
        # ----------------------------------------------------------------
        #  Добавляем 1 изображение динозаврика
        self.dino_walk_1 = pygame.image.load('data/dino/динозавр для игры 2(бег).png').convert_alpha()
        # Добавляем 2 изображение динозаврика
        self.dino_walk_2 = pygame.image.load('data/dino/динозавр для игры 3(бег).png').convert_alpha()
        # Объединяем изображения динозаврика
        self.dino_walk = [self.dino_walk_1, self.dino_walk_2]
        # Добавляем значение бега динозаврика
        self.dino_walk_index = 0
        # Добавляем анимацию
        self.image = self.dino_walk[self.dino_walk_index]
        # Добавлем к динозаврику квадрат
        self.rect = self.image.get_rect(midbottom=(80, 300))
        # Добавлем гравитацию динозаврику
        self.dino_gravity = 0
        # Добавляем изображение прыжка динозаврика
        self.dino_jump = pygame.image.load('data/dino/динозавр для игры 4(прыжок).png').convert_alpha()
        # ----------------------------------------------------------------
        # Дообавляем музыку динозаврика в нашу игру
        # ----------------------------------------------------------------
        # Добавим звук прыжка
        self.jump_music = pygame.mixer.Sound('data/music/cartoon-spring-boing-03 (mp3cut.net)(jump).mp3')
        # Выставляем звук
        self.jump_music.set_volume(0.5)

    def key_down(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 260:
            self.dino_gravity = -20
            self.jump_music.play()

    def dino_animation(self):
        if self.rect.bottom < 260:
            self.image = self.dino_jump
        else:
            self.dino_walk_index += 0.1
            if self.dino_walk_index >= len(self.dino_walk):
                self.dino_walk_index = 0
            self.image = self.dino_walk[int(self.dino_walk_index)]

    def dino_gravityx(self):
        self.dino_gravity += 1
        self.rect.y += self.dino_gravity
        if self.rect.bottom >= 260:
            self.rect.bottom = 260

    def update(self):
        self.key_down()
        self.dino_animation()
        self.dino_gravityx()


# ----------------------------------------------------------------
# Функция start screen
# ----------------------------------------------------------------
def start_screen():
    # Пропишем нужный нам текст
    intro_text = ["Dino 2.0",
                  "В игре есть много разных и ",
                  "прикольных персонажей,",
                  'каждый интересен по своему',
                  'и очень опасен, буде осторожны!']
    # Подбирем фон
    fon = pygame.transform.scale(start_fon, (800, 400))
    # Нарисуем наш фон
    screen.blit(fon, (0, 0))
    # Выставим шрифт
    sh = pygame.font.Font('data/font/Sonic 1 Title Screen Filled.ttf', 4)
    # Выставляем шрифт
    font = pygame.font.Font('data/font/Sonic 1 Title Screen Filled.ttf', size_shrift)
    # Выставлям координаты текста
    text_coord = 15
    # Выводим текст
    for line in intro_text:
        # Если это название, то пишем его по другому
        if line == 'Dino 2.0':
            # Выставляем шрифт
            font2 = pygame.font.Font('data/font/Motel King Medium(RUS by Slavchansky).ttf', 57)
            # Рендарим текст
            string_rendered = font2.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 230
            text_coord += intro_rect.height
            text_coord += 125
        else:
            # Рендарим текст
            string_rendered = font.render(line, 1, pygame.Color('Green'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
        # Рисуем наш текст
        screen.blit(string_rendered, intro_rect)

    # Запускаем наше окно
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
                # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# ----------------------------------------------------------------------------
# Функция display_score
# ----------------------------------------------------------------------------
def display_score():
    # Достаем шрифт
    font6 = pygame.font.Font('data/font/19180.otf', 48)
    # Получаем время с начала игры
    tick = pygame.time.get_ticks()
    # Вычисляем время от последней смерти
    real_time = int(tick / 1000) - start_time
    # Рендарим текст
    score_image = font6.render(f'Счет {real_time}', 1, (0, 0, 0))
    # Выставляем координаты
    score_cord = score_image.get_rect(center=(400, 50))
    # Отрисоваваем счетчик стор
    screen.blit(score_image, score_cord)
    return real_time


def lose_screen():
    # Пропишем нужный нам текст
    intro_text = ["Dino 2.0",
                  '1',
                  "Вы проиграли,",
                  "попробуйте еще раз.",
                  'Для этого нажмите на пробел',
                  'и игра пойдет заново!']
    # Подбирем фон
    fon = pygame.transform.scale(lose_fon, (800, 400))
    # Нарисуем наш фон
    screen.blit(fon, (0, 0))
    sh = pygame.font.Font('data/font/Sonic 1 Title Screen Filled.ttf', 4)
    # Выставляем шрифт
    font = pygame.font.Font('data/font/Sonic 1 Title Screen Filled.ttf', size_shrift)
    # Выставлям координаты текста
    text_coord = 15
    # Выводим текст
    for line in intro_text:
        # Если это название то пишем его по другому
        if line == 'Dino 2.0':
            # Выставляем шрифт
            font2 = pygame.font.Font('data/font/Motel King Medium(RUS by Slavchansky).ttf', 57)
            # Рендарим текст
            string_rendered = font2.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 230
            text_coord += intro_rect.height
            text_coord += 15
        elif line == '1':
            # Выставляем шрифт
            font4 = pygame.font.Font('data/font/MultiroundPro.otf', 59)
            # Рендарим текст
            string_rendered = font4.render(f'Ваш результат {score}.', 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 130
            text_coord += intro_rect.height
            text_coord += 15
        elif line != '1' and line != 'Dino 2.0':
            font3 = pygame.font.Font('data/font/DolomanPavljenko.otf', 45)
            # Рендарим текст
            string_rendered = font3.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
        # Рисуем наш текст
        screen.blit(string_rendered, intro_rect)


game_active = False
dinos = pygame.sprite.GroupSingle()
dinos.add(dino())
start_screen()
fon_music.stop()
fon2_music.play(loops=-1)
runn = True
while runn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runn = False
        if game_active:
            pass
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    screen.fill((0, 0, 0))
    if game_active:
        screen.fill((0, 0, 0))
        screen.blit(sky, (0, 0))
        screen.blit(land, (0, 260))
        score = display_score()
        dinos.draw(screen)
        dinos.update()

    else:
        lose_screen()

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
