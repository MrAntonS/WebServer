import pygame
import requests
import sys
import os
from map import get_map
 
response = None
try:
    x = [30, 50, 8, "map.png"]#input().split()
    map_file = get_map(x[0],x[1],x[2],x[3])
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)
 
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
# Рисуем картинку, загружаемую из только что созданного файла.

screen.blit(pygame.image.load(x[3]), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
running = True
x[2] = int(x[2])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            print("///")
            print(x[0])
            print(x[1])
            if event.key == 280: 
                if x[2] != 20:
                    x[2] += 1
            if event.key == 281:
                if x[2] != 0:
                    x[2] -= 1
            if event.key == 273:
                if x[1] != 73:
                    x[1] += 1
            if event.key == 274:
                if x[1] != 0:
                    x[1] -= 1
            if event.key == 275:
                if x[0] != 180:
                    x[0] += 1
            if event.key == 276:
                if x[0] != -140:
                    x[0] -= 1
    x[2] = abs(x[2])
    map_file = get_map(x[0],x[1],x[2],x[3])
    screen.blit(pygame.image.load(x[3]), (0, 0))
    pygame.display.flip()
    pass
pygame.quit()
 
# Удаляем за собой файл с изображением.
os.remove(x[3])