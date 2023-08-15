import pygame
from queue import Queue

pygame.init()

# color used
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

# global variables
screen_width = 800
screen_height = 800
WIDTH = 30
HEIGHT = 30
MARGIN = 1
text_size = 15
row_box = 25
col_box = 25
grid = []
dis = []
INF = 1000000
direction = [[1,0],[-1,0],[0,1],[0,-1]]
fps = 60
path = []

# screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Multisource BFS")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,text_size)

def create_board():
    for row in range(row_box):
        grid.append([])
        dis.append([])
        for column in range(col_box):
            grid[row].append(0)
            dis[row].append(INF)

def draw_grid():
    for row in range(row_box):
        for column in range(col_box):
            color = BLACK
            if grid[row][column] == 1:
                color = RED
            if grid[row][column] == 2:
                color = GREEN
            if grid[row][column] == 3:
                color = BLUE
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

def color_grid():
    done = False

    curr = 1
    global max_depth
    for row,column in path:
        screen.fill(WHITE)
        color = BLACK
        if grid[row][column] == 2:
            color = GREEN
        if grid[row][column] == 3:
            color = BLUE
        color = RED
        draw_grid()
        grid[row][column] = 1;
        pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        pygame.time.delay(50)
        pygame.display.update()

def isValid(x,y):
    if x < 0 or y < 0 or x >= row_box or y >= col_box:
        return False
    if grid[x][y] == 2:
        return False
    return (dis[x][y] == INF)

def bfs():
    q = Queue(0)

    for row in range(row_box):
        for column in range(col_box):
            if grid[row][column] == 1:
                q.put([row,column])
                path.append([row,column])
                dis[row][column] = 0

    while not q.empty():
        [x,y] = q.get()
        for dx,dy in direction:
            X = x + dx
            Y = y + dy
            if isValid(X,Y):
                dis[X][Y] = 1 + dis[x][y]
                q.put([X,Y])
                path.append([X,Y])

def gameloop():

    # local varible
    done = False

    create_board()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                grid[row][column] = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                done = True

        screen.fill(WHITE)
        draw_grid()
        pygame.display.update()
        clock.tick(fps)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                grid[row][column] = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                done = True

        screen.fill(WHITE)
        draw_grid()
        pygame.display.update()
        clock.tick(fps)

gameloop()
bfs()
color_grid()
pygame.quit()
quit()