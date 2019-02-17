import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 500
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
size = s_width, s_height
screen = pygame.display.set_mode(size)

# SHAPE FORMATS

S = [[[0, 1, 1],
      [1, 1, 0]],
     [[1, 0],
      [1, 1],
      [0, 1]]]

Z = [[[2, 2, 0],
      [0, 2, 2]],
[[0, 2],
 [2, 2],
 [2, 0]]]

I = [[[3],
      [3],
      [3],
      [3]],
     [[3, 3, 3, 3]]]

O = [[[4, 4],
      [4, 4]]]

J = [[[5, 0, 0],
      [5, 5, 5]],
[[5, 5],
 [5, 0],
 [5, 0]],
[[5, 5, 5],
 [0, 0, 5]],
[[0, 5],
 [0, 5],
 [5, 5]]]

L = [[[0, 0, 6],
      [6, 6, 6]],
[[6, 0],
 [6, 0],
 [6, 6]],
[[6, 6, 6],
 [6, 0, 0]],
[[6, 6],
 [0, 6],
 [0, 6]]]

T = [[[0, 7, 0],
      [7, 7, 7]],
[[7, 0],
 [7, 7],
 [7, 0]],
[[7, 7, 7],
 [0, 7, 0]],
[[0, 7],
[7, 7],
[0, 7]]]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255),
                (128, 0, 128)]

#def create_grid(locked_positions={}):
    #global grid
    #grid = [[0 for _ in range(10)] for _ in range(20)]



def draw_window(surface):
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, play_width, play_height), 1)
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(screen, shape_colors[grid[i][j]], (0 + j * 30, 0 + i * 30, 30, 30), 0)
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, play_width, play_height), 1)

def create_shape():
  pass


class Shape:
    def __init__(self, x, y, type, pos):
        self.x = x
        self.y = y
        self.type = type
        self.pos = pos
        global Flag, DeTime
        if not Check_Lock(self.type, self.pos, self.x, self.y):
            for i in range(len(type[pos])):
                for j in range(len(type[pos][i])):
                    if type[pos][i][j] != 0:
                        pygame.draw.rect(screen, shape_colors[type[pos][i][j]], (x * 30 + j * 30, y * 30 + i * 30,
                                                                                 30, 30), 0)
        else:
            for i in range(len(type[pos])):
                for j in range(len(type[pos][i])):
                    if type[pos][i][j] != 0:
                        grid[i + int(y)][j + int(x)] = type[pos][i][j]
            DeTime = 100
            draw_window(screen)
            Flag = False

all
def Check_Lock(ttype, Poss, x, y):
    flag = False
    global  Game_score
    if 20 - len(ttype[Poss]) == y:
        flag = True
    else:
        for i in range(len(ttype[Poss])):
            for j in range(len(ttype[Poss][i])):
                if ((grid[i + int(y) + 1][j + int(x)] + ttype[Poss][i][j]) != ttype[Poss][i][j]) and\
                        (ttype[Poss][i][j] != 0):
                    flag = True
    if flag:
        return True
    else:
        return False


def down_line(num):
    global Game_score
    for i in range(num, 0, -1):
        grid[i] = grid[i - 1]
    Game_score += 100
    print(Game_score)


#create_grid()
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

run = True
Flag = True
cord_y = 0
cord_x = 0
counter = 0
shape_type = []
shape_pos = 0
DeTime = 10
Game_score = 0
while run:

    if counter == 0:
        shape_type = shapes[random.randint(0, 6)]

    counter += 1
    keys = pygame.key.get_pressed()
    if Flag:
        Shape(cord_x, cord_y, shape_type, shape_pos)

    if not Flag:
        for i in range(20):
            if all(grid[i]) != 0:
                down_line(i)
        draw_window(screen)
        Flag = True
        cord_y = 0
        cord_x = 0
        shape_type = shapes[random.randint(0, 6)]
        shape_pos = random.randint(0, len(shape_type) - 1)

    if keys[pygame.K_UP]:
        if shape_type[shape_pos] != shape_type[-1]:
            if not((len(shape_type[shape_pos][0]) < len(shape_type[shape_pos + 1][0])) and
                   (cord_x > (10 - len(shape_type[shape_pos + 1][0])))):
                shape_pos += 1
        elif not((len(shape_type[shape_pos][0]) < len(shape_type[0][0])) and
                    (cord_x > (10 - len(shape_type[0][0])))):
            shape_pos = 0
        draw_window(screen)
        Shape(cord_x, cord_y, shape_type, shape_pos)

    if keys[pygame.K_LEFT] and cord_x != 0:
        cord_x -= 1
        draw_window(screen)
        Shape(cord_x, cord_y, shape_type, shape_pos)

    if keys[pygame.K_RIGHT] and cord_x != (10 - len(shape_type[shape_pos][0])):
        cord_x += 1
        draw_window(screen)
        Shape(cord_x, cord_y, shape_type, shape_pos)

    if keys[pygame.K_DOWN]:
        DeTime = 1

    if Flag and ((counter % 10) == 0):
        draw_window(screen)
        cord_y += 1

    pygame.display.flip()
    pygame.time.delay(DeTime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
