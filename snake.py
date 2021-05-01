import pygame
import random
import time

pygame.init()

#Cores
blue = (50, 100, 213)
orange = (205, 102, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)
red = (255,40,0)

#Dimensões
dimensions = (600,600)

#Valores Iniciais
x = 300
y = 300
d = 20
list_snake = [ [x, y] ] 
dx = 0
dy = 0
snake_alive = True

x_eat = round(random.randrange(0, 600 - d) / 20) * 20
y_eat = round(random.randrange(0, 600 - d) / 20) * 20

font = pygame.font.SysFont('hack', 35)
font2 = pygame.font.SysFont('hack', 70)

screen = pygame.display.set_mode((dimensions))
pygame.display.set_caption('Snake da Kenzie')

screen.fill(blue)


clock = pygame.time.Clock()

def draw_snake(list_snake):
    screen.fill(blue)
    for unidade in list_snake:
        pygame.draw.rect(screen, orange, [unidade[0], unidade[1], d, d])

def move_snake(dx, dy, list_snake): 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    
    x_novo = list_snake[-1][0] + dx
    y_novo = list_snake[-1][1] + dy
    list_snake.append([x_novo, y_novo])
    del list_snake[0]

    return dx, dy, list_snake

def check_comida(dx, dy, x_eat, y_eat, list_snake):
    head = list_snake[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_eat and head[1] == y_eat:
        list_snake.append([x_novo, y_novo])
        x_eat = round(random.randrange(0, 600 - d) / 20) * 20
        y_eat = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(screen, green, [x_eat, y_eat, d, d])

    return x_eat, y_eat, list_snake

def game_over():
    screen.fill(blue)
    game_over = font2.render('GAME OVER', True, red)
    reset = font.render('Reinicie o jogo', True, yellow)
    screen.blit(game_over, [150,250])
    screen.blit(reset, [210,320])
    pygame.display.update()
    time.sleep(1)

def check_wall(list_snake):
    head = list_snake[-1]
    x = head[0]
    y = head[1]
    if x not in range(600) or y not in range(600):
        game_over()
        return False
    return True

def check_crash(list_snake):
    head = list_snake[-1]
    body = list_snake.copy()
    del body[-1]
    for x,y in body:
        if x == head[0] and y == head[1]:
            game_over()
            return False
    return True
    
def update_points(list_snake):
    pts = str(len(list_snake))
    score = font.render('Pontuação: ' + pts, True, yellow)
    screen.blit(score, [0,0])

def update_speed(lista_snake):
    pts = len(list_snake)
    if pts > 5:
        return pts * 2.5
    else:
        return pts * 3

while snake_alive:
    pygame.display.update()
    draw_snake(list_snake)
    dx, dy, list_snake = move_snake(dx, dy, list_snake)
    x_eat, y_eat, list_snake = check_comida(dx, dy, x_eat, y_eat, list_snake)
    #print(list_snake)
    snake_alive = check_wall(list_snake)
    snake_alive = check_crash(list_snake)
    update_points(list_snake)
    speed_snake = update_speed(list_snake)
    clock.tick(speed_snake)