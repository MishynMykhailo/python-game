# Импортируем библиотеку
import random
import pygame
import os
# Достаем из библиотеки нужный нам функционал
from pygame.constants import QUIT, K_DOWN, K_UP , K_RIGHT, K_LEFT
# Инициализация
pygame.init()
# UPPERCASE используется для помечения 'констант'
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200
FONT = pygame.font.SysFont('Verdana',20)

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
COLOR_GREEN = (0,255,0)
# Создаем экземпляр дисплея - наше окно, где будет игра
main_display = pygame.display.set_mode((WIDTH,HEIGHT))
# BG
bg = pygame.transform.scale(pygame.image.load('background.png'),(WIDTH,HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
# goose anim
IMAGE_PATH = "goose-anim"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)
print(PLAYER_IMAGES)
# Создаем размеры игрока
# Создаем экземпляр игрока
player = pygame.image.load('player.png').convert_alpha() # pygame.Surface(player_size)
player_size = (player.get_width(), player.get_height())

# Заливаем нашего игрока
# player.fill(COLOR_BLACK)
# Считываем координаты
player_rect = pygame.Rect(0, HEIGHT/2,*player_size)
# player_rect = player.get_rect();
# Скорость игрока
player_move_down = [0,4];
player_move_up = [0,-4];
player_move_left = [-4,0];
player_move_right = [4,0];


# Создание врага
def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_size = (enemy.get_width(),enemy.get_height())
    enemy_rect = pygame.Rect(WIDTH, random.randint(20, HEIGHT-20), *enemy_size)
    enemy_move = [random.randint(-8,-4), 0]
    return [enemy, enemy_rect, enemy_move]



def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_size = (bonus.get_width(),bonus.get_height())
    bonus_rect = pygame.Rect(random.randint(20,WIDTH-20), 0-bonus.get_height(), *bonus_size)
    bonus_move = [0,random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []
score = 0
text = "PYTHON"
image_index = 0
# Переменная для цикла
playing = True

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        # Проверка на клик по кнопке QUIT, чтобы прервать цикл и выйти
        if event.type == QUIT:
            playing = False
            # Закрашиваем поле в обычный цвет, чтобы не было белой линии
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH,PLAYER_IMAGES[image_index]))
            image_index+=1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_X1 -= bg_move
    bg_X2 -= bg_move
# Если ширина меньше нашего bg, то перерисовываем, чтобы обновить
    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
# Если ширина меньше нашего bg, то перерисовываем, чтобы обновить
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()
        # Добавляем отрисовку
    main_display.blit(bg,(bg_X1,0))
    main_display.blit(bg,(bg_X2,0))
    # Отслеживаем нажатые клавиши
    keys = pygame.key.get_pressed()
    
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)
    # Ставим ограничения, чтобы игрок не вышел за экран
   
   
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0],enemy[1])
        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0],bonus[1])
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            score +=1

    # Добавляем игрока на поле
    main_display.blit(FONT.render(str(text),True,COLOR_BLACK),(20,20))
    main_display.blit(FONT.render(str(score),True,COLOR_BLACK),(WIDTH-50,20))
    main_display.blit(player,player_rect)
    # main_display.blit(enemy,enemy_rect)
    # Для движения игрока
    # player_rect = player_rect.move(player_speed)
# Обновляем дисплей, чтобы увидеть изменения
    # print(len(enemies))
    
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))