# Импортируем библиотеку
import pygame
# Достаем из библиотеки нужный нам функционал
from pygame.constants import QUIT
# Инициализация
pygame.init()
# UPPERCASE используется для помечения 'констант'
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
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
player_speed = [1,1]
# Переменная для цикла
playing = True
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        # Проверка на клик по кнопке QUIT, чтобы прервать цикл и выйти
        if event.type == QUIT:
            playing = False
            # Закрашиваем поле в обычный цвет, чтобы не было белой линии
    main_display.fill(COLOR_BLACK)
    # Ставим ограничения, чтобы игрок не вышел за экран
    print(player_rect.top)
    

    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH:
        player_speed[0] = -player_speed[0]
        
    if player_rect.top <= 0:
        player_speed[1] = -player_speed[1]

    if player_rect.left <= 0:
        player_speed[0] = -player_speed[0]
 
    # Добавляем игрока на поле
    main_display.blit(player,player_rect)
    # Для движения игрока
    player_rect = player_rect.move(player_speed)
# Обновляем дисплей, чтобы увидеть изменения
    pygame.display.flip()