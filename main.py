# Импортируем библиотеку
import random
import pygame
# Достаем из библиотеки нужный нам функционал
from pygame.constants import QUIT, K_DOWN, K_UP , K_RIGHT, K_LEFT
# Инициализация
pygame.init()
# UPPERCASE используется для помечения 'констант'
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
COLOR_GREEN = (0,255,0)
# Создаем экземпляр дисплея - наше окно, где будет игра
main_display = pygame.display.set_mode((WIDTH,HEIGHT))
# Создаем размеры игрока
player_size = (20,20)
# Создаем экземпляр игрока
player = pygame.Surface(player_size)
# Заливаем нашего игрока
player.fill(COLOR_WHITE)
# Считываем координаты
player_rect = player.get_rect();
# Скорость игрока
player_move_down = [0,1];
player_move_up = [0,-1];
player_move_left = [-1,0];
player_move_right = [1,0];


# Создание врага
def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6,-1), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

def create_bonus():
    bonus_size = (30, 30)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_GREEN)
    bonus_rect = pygame.Rect(random.randint(0,WIDTH), 0, *bonus_size)
    bonus_move = [0,random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_move]

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

enemies = []
bonuses = []
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
            
    main_display.fill(COLOR_BLACK)
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


    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0],bonus[1])

# Для Enemy
    # enemy_rect = enemy_rect.move(enemy_move)
# Пример №1: того как можно сделать отбитие от стенок нашего окна
    # if player_rect.bottom >= HEIGHT:
    #     player_speed[1] = -player_speed[1]

    # if player_rect.right >= WIDTH:
    #     player_speed[0] = -player_speed[0]
        
    # if player_rect.top <= 0:
    #     player_speed[1] = -player_speed[1]

    # if player_rect.left <= 0:
    #     player_speed[0] = -player_speed[0]
 

 # Пример №2: того как можно сделать отбитие от стенок нашего окна 
    # if player_rect.bottom >= HEIGHT:
    #     player_speed = random.choice(([1,-1],[-1,-1]))

    # if player_rect.right >= WIDTH:
    #     player_speed = random.choice(([-1,1],[1,1]))
        
    # if player_rect.top <= 0:
    #     player_speed = random.choice(([-1,-1],[-1,1]))

    # if player_rect.left <= 0:
    #     player_speed = random.choice(([1,1],[1,-1]))




    # Добавляем игрока на поле
    main_display.blit(player,player_rect)
    # main_display.blit(enemy,enemy_rect)
    # Для движения игрока
    # player_rect = player_rect.move(player_speed)
# Обновляем дисплей, чтобы увидеть изменения
    # print(len(enemies))
    print(len(bonuses))
    
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))