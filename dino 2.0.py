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
        # Ведём переменую i
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

    # ------------------------------------------------------------
    # Функция key_down
    # ------------------------------------------------------------

    def key_down(self):
        # Получаем все клавиши которые нажаты
        key = pygame.key.get_pressed()
        # Если нажат пробел и динозаврик на земле
        if key[pygame.K_SPACE] and self.rect.bottom >= 260:
            # То dino_gravity = -20
            self.dino_gravity = -20
            # И проигрываем звук прыжка
            self.jump_music.play()

    # ------------------------------------------------------------
    # Функция dino_animation
    # ------------------------------------------------------------
    def dino_animation(self):
        # Если динозаврик подпрыгнул
        if self.rect.bottom < 260:
            # Cтавим изображение прыгающего динозаврика
            self.image = self.dino_jump
        # Если не прыгает
        else:
            # Отсчитываем dino_walk_index
            self.dino_walk_index += 0.1
            # Если dino_walk_index больше длины dino_walk
            if self.dino_walk_index >= len(self.dino_walk):
                # Обнуляем dino_walk_index
                self.dino_walk_index = 0
            # Cтавим изображение динозаврика
            self.image = self.dino_walk[int(self.dino_walk_index)]

    # ------------------------------------------------------------
    # Функция dino_gravityx
    # ------------------------------------------------------------

    def dino_gravityx(self):
        # Медленно возвращаем его обратно
        self.dino_gravity += 1
        # Медленно возвращаем его обратно
        self.rect.y += self.dino_gravity
        # Если он на земле
        if self.rect.bottom >= 260:
            # Останавливаем его
            self.rect.bottom = 260

    # ------------------------------------------------------------
    # Функция update
    # ------------------------------------------------------------

    def update(self):
        # Вызываем key_down
        self.key_down()
        # Вызываем dino_animation
        self.dino_animation()
        # Вызываем dino_gravityx
        self.dino_gravityx()


# ----------------------------------------------------------------
# Функция spider
# ----------------------------------------------------------------
class Spider(pygame.sprite.Sprite):
    #
    def __init__(self):
        super().__init__()
        # ----------------------------------------------------------------
        # Добавляем паучка в нашу игру
        # ----------------------------------------------------------------
        #  Добавляем 1 изображение
        self.spider_frame_1 = pygame.image.load('data/spider/паук для игры 1.png').convert_alpha()
        # Добавляем 2 изображение
        self.spider_frame_2 = pygame.image.load('data/spider/паук для игры 2.png').convert_alpha()
        # Объединяем изображения
        self.spider_frames = [self.spider_frame_1, self.spider_frame_2]
        # Добавляем значение анимации
        self.spider_frame_index = 0
        # Добавляем анимацию
        spider_surf = self.spider_frames[self.spider_frame_index]
        # Выставляем позицию
        self.pos_land = 260
        # Выставляем изображение
        self.image = self.spider_frames[self.spider_frame_index]
        #
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.pos_land))

    # ------------------------------------------------------------
    # Функция crash
    # ------------------------------------------------------------

    def crash(self):
        #
        if self.rect.x <= -80:
            #
            self.kill()

    # ------------------------------------------------------------
    # Функция spider_animation
    # ------------------------------------------------------------
    def spider_animation(self):
        # Отсчитываем spider_walk_index
        self.spider_frame_index += 0.1
        # Если spider_walk_index больше длины spider_walk
        if self.spider_frame_index >= len(self.spider_frames):
            # Обнуляем spider_walk_index
            self.spider_frame_index = 0
        # Cтавим изображение динозаврика
        self.image = self.spider_frames[int(self.spider_frame_index)]

    # ------------------------------------------------------------
    # Функция update
    # ------------------------------------------------------------

    def update(self):
        # Вызываем spider_animation
        self.spider_animation()
        # Делаем чтоб наша стрекоза литела
        self.rect.x -= 6
        # Вызываем функцию crash
        self.crash()


# ----------------------------------------------------------------
# Функция spider
# ----------------------------------------------------------------
class Dragonfly(pygame.sprite.Sprite):
    #
    def __init__(self):
        super().__init__()
        # ----------------------------------------------------------------
        # Добавляем стрекозу в нашу игру
        # ----------------------------------------------------------------
        #  Добавляем 1 изображение
        self.dragonfly_frame1 = pygame.image.load('data/dragonfly/стрекоза для игры 1.png').convert_alpha()
        # Добавляем 2 изображение
        self.dragonfly_frame2 = pygame.image.load('data/dragonfly/стрекоза для игры 2.png').convert_alpha()
        # Объединяем изображения
        self.dragonfly_frames = [self.dragonfly_frame1, self.dragonfly_frame2]
        # Добавляем значение анимации
        self.dragonfly_frame_index = 0
        # Добавляем анимацию
        dragonfly_surf = self.dragonfly_frames[self.dragonfly_frame_index]
        # Выставляем позицию стрекозы
        self.pos_land = randint(160, 190)
        # Ставим изображение
        self.image = self.dragonfly_frames[self.dragonfly_frame_index]
        # выставляем нашей стрекозе позицию
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.pos_land))

    # ------------------------------------------------------------
    # Функция crash
    # ------------------------------------------------------------

    def crash(self):
        # если стрекоза ушла с экрана
        if self.rect.x <= -80:
            # Уничтожим её
            self.kill()

    # ------------------------------------------------------------
    # Функция dragonfly_animation
    # ------------------------------------------------------------
    def dragonfly_animation(self):
        # Отсчитываем dragonfly_walk_index
        self.dragonfly_frame_index += 0.1
        # Если dragonfly_walk_index больше длины dragonfly_walk
        if self.dragonfly_frame_index >= len(self.dragonfly_frames):
            # Обнуляем dragonfly_walk_index
            self.dragonfly_frame_index = 0
        # Cтавим изображение стрекозы
        self.image = self.dragonfly_frames[int(self.dragonfly_frame_index)]

    # ------------------------------------------------------------
    # Функция update
    # ------------------------------------------------------------

    def update(self):
        # Вызываем dragonfly_animation
        self.dragonfly_animation()
        # Делаем чтоб наша стрекоза летела на право
        self.rect.x -= 5
        # Вызываем функцию crash
        self.crash()


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


# ----------------------------------------------------------------------------
# Функция lose_screen
# ----------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------
# Функция collision_crasheck
# ----------------------------------------------------------------------------
def collision_crasheck():
    # Проверяем есть ли столкновение динозаврика
    if pygame.sprite.spritecollide(dinos.sprite, group, False):
        # Очищаем нашу группу с объектами
        group.empty()
        # Возращаем False
        return False
    # Возращаем True
    return True


# ----------------------------------------------------------------------------
# Таймер спавна стрекоз и пауков
# ----------------------------------------------------------------------------
# Отсчитываем время
timer_spawn = pygame.USEREVENT + 1
# Выставляем таймер
pygame.time.set_timer(timer_spawn, 1900)
# Добавляем переменную game_active
game_active = False
# Создаем спрайт dinos
dinos = pygame.sprite.GroupSingle()
# Добавляем в dinos класс dino
dinos.add(dino())
# Вызываем функцию start_screen
start_screen()
# Останавливаем стартовую музыку
fon_music.stop()
# Начинаем бесконечно проигрывать новую фоновую музыку
fon2_music.play(loops=-1)
# Выставляем ей громкость
fon2_music.set_volume(0.2)
# Прописываем множество наших животных
animals = ['spider', 'spider', 'spider', 'dragonfly']
# Создаем группу с наши животными
group = pygame.sprite.Group()
# Добавляем переменую glavnai_run
glavnai_run = True
# Запускаем главный цикл
while glavnai_run:
    # Перебераем все события
    for event in pygame.event.get():
        # Если приложение закрывается
        if event.type == pygame.QUIT:
            # Закрывам приложение
            glavnai_run = False
        # Ести game_active = True
        if game_active:
            # Если таймер подошел для спавна
            if event.type == timer_spawn:
                # Выбираем рандомно персонажа
                type = choice(animals)
                # Если это паук
                if type == 'spider':
                    # Добавляем паука в группу для преграды
                    group.add(Spider())
                # Если это стрекоза
                elif type == 'dragonfly':
                    # Добавляем стрекозу в группу для преграды
                    group.add(Dragonfly())
        # Если нет
        else:
            # Если нажата клавиша и это клавиша пробел
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # делаем игру активной
                game_active = True
                # И заменяем стартовое время на время смерти
                start_time = int(pygame.time.get_ticks() / 1000)
    # Если игра активна
    if game_active:
        # Рисуем небо
        screen.blit(sky, (0, 0))
        # Рисуем землю
        screen.blit(land, (0, 260))
        # Вычисляем счет
        score = display_score()
        # Рисуем динозаврика
        dinos.draw(screen)
        # Обновляем спрайт динос
        dinos.update()
        # Отрисоваваем группу с препятствиями
        group.draw(screen)
        # Обновляем препятствия
        group.update()
        # Проверяем столкновения
        game_active = collision_crasheck()
    # Если игра остановлена
    else:
        # Показываем экран проигрыша
        lose_screen()
    # Ставим скорость отображения
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
