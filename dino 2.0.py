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
size_shrift = 50
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
# Добавим звук прыжка
jump_music = pygame.mixer.Sound('data/music/cartoon-spring-boing-03 (mp3cut.net)(jump).mp3')
# ----------------------------------------------------------------
# Дообавляем фон нашей игры
# ----------------------------------------------------------------
# Добалем фоновое изображение для старта игры
start_screen = pygame.image.load('data/start_screen/210420200620119050.jpg')
# Добавляем небо
sky = pygame.image.load("data/sky/sky.png")
# Добавлем землю
land = pygame.image.load("/data/land/land.png")
# ----------------------------------------------------------------
# Дообавляем динозаврика в нашу игру
# ----------------------------------------------------------------
#  Добавляем 1 изображение динозаврика
dino_walk_1 = pygame.image.load('/data/dino/dino_walk_1.png').convert_alpha()
# Добавляем 2 изображение динозаврика
dino_walk_2 = pygame.image.load('/data/dino/dino_walk_2.png').convert_alpha()
# Объединяем изображения динозаврика
dino_walk = [dino_walk_1, dino_walk_2]
# Добавляем значение бега динозаврика
dino_walk_index = 0
# Добавляем изображение прыжка динозаврика
dino_jump = pygame.image.load('data/dino/jump.png').convert_alpha()
# Добавляем анимацию
dino_surf = dino_walk[dino_walk_index]
# Добавлем к динозаврику квадрат
dino_rect = dino_surf.get_rect(midbottom=(80, 300))
# Добавлем гравитацию динозаврику
dino_gravity = 0
# ----------------------------------------------------------------
# Добавляем паучка в нашу игру
# ----------------------------------------------------------------
#  Добавляем 1 изображение
spider_frame_1 = pygame.image.load('data/spider/spider1.png').convert_alpha()
# Добавляем 2 изображение
spider_frame_2 = pygame.image.load('data/spider/spider2.png').convert_alpha()
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
dragonfly_frame1 = pygame.image.load('data/dragonfly/dragonfly1.png').convert_alpha()
# Добавляем 2 изображение
dragonfly_frame2 = pygame.image.load('data/dragonfly/dragonfly2.png').convert_alpha()
# Объединяем изображения
dragonfly_frames = [dragonfly_frame1, dragonfly_frame2]
# Добавляем значение анимации
dragonfly_frame_index = 0
# Добавляем анимацию
dragonfly_surf = dragonfly_frames[dragonfly_frame_index]


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Dino 2.0", "",
                  "Правила игры",
                  "В игре есть много прикольных персонажей,",
                  "каждый очень опасен,"
                  'буде осторожны!']

    fon = pygame.transform.scale(start_screen, (800, 400))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(shrift, size_shrift)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)
