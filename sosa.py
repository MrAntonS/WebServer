import pygame
import requests
import sys
import os
import test
from map import get_map
 
 
response = None
MYEVENTTYPE = 30
#Частота обновлениея ~20 секунд
#Сделано для того чтобы не нагружать систему

pygame.time.set_timer(MYEVENTTYPE, 20000)
slovar = test.test()[1][:-1]
slovar1 = test.test()[0]
try:
    x = [30, 50, 8, "map.png"]#input().split()
    print(test.test()[1])
    map_file = get_map(x[0],x[1],x[2],x[3], test.test()[1][:-1])
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
        #Обновление положения самолетов 
        if event.type == MYEVENTTYPE:
            print("Мое событие сработало")
            slovar = test.test()[1][:-1]
            slovar1 = test.test()[0]
            
        if event.type == pygame.KEYUP:
            #Сделано для проверки координат
            #Масштаб
            if event.key == 280: 
                if x[2] != 20:
                    x[2] += 1
                    
            if event.key == 281:
                if x[2] != 0:
                    x[2] -= 1
            #Перемещение камеры    
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
            if event.key == 105:
                xstat = input("Какой самолет вам нужен?")
                if xstat.isdigit():
                    print("Готово")
                    print("ICAO24:", str(slovar1[int(xstat)][0]), "Callsign:", str(slovar1[int(xstat)][1]), "Speed:", str(slovar1[int(xstat)][5]) + "m/s", "On Ground?", str("No" if slovar1[int(xstat)][8] == False else "Yes"))
                    
    #Создаем новую карту
    x[2] = abs(x[2])
    map_file = get_map(x[0],x[1],x[2],x[3], slovar)
    screen.blit(pygame.image.load(x[3]), (0, 0))
    pygame.display.flip()
    pass
pygame.quit()
 
# Удаляем за собой файл с изображением.
os.remove(x[3])