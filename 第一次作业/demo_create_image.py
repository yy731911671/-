import pygame
import random
import numpy

XMAX, YMAX = 20, 20
pygame.init()
screen = pygame.display.set_mode([XMAX*30,YMAX*30])
screen.fill([255,255,255])

pngWall1 = "wall1.png"
pngWall2 = "wall2.png"
pngPoint = "point.png"

imgWall1 = pygame.image.load(pngWall1)
imgWall2 = pygame.image.load(pngWall2)
imgPoint = pygame.image.load(pngPoint)
def create_grid_string(dots, xx, yy):
    """
    Creates a grid of size (xx, yy)
    with the given positions of dots
    """
    grid = ""
    for y in range(yy):
        for x in range(xx):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid


def get_all_dots_positions(xsize, ysize):
    """Returns a list of (x, y) tuples covering all positions in a grid"""
    return [(x, y) for x in range(1, xsize - 1) for y in range(1, ysize - 1)]


def get_neighbors(x, y):
    """Returns a list with the 8 neighbor positions of (x, y)"""
    return[
        (x, y - 1), (x + 1, y), (x - 1, y), (x - 1, y - 1),
        (x, y + 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)
    ]


def generate_dot_positions(xsize, ysize):
    """Creates positions of dots for a random maze"""
    positions = get_all_dots_positions(xsize, ysize)
    dots = set()
    while positions != []:
        (x, y) = random.choice(positions)
        neighbors = get_neighbors(x, y)
        free = [nb in dots for nb in neighbors]
        if free.count(True) < 5: # 等于5时，第二行和倒数第二行无#
            dots.add((x, y))
        positions.remove((x, y))
    return dots


def create_maze(xsize, ysize):
    """Returns a xsize*ysize maze as a string"""
    dots = generate_dot_positions(xsize, ysize)
    maze = create_grid_string(dots, xsize, ysize)
    return maze





maze = create_maze(XMAX, YMAX)
print(maze)
"""
create a maze picture
"""
list = maze.split("\n")
for x in range(XMAX):
    for y in range(YMAX):
        if x == 0 or y == 0 or x == XMAX - 1 or y == YMAX - 1:
            screen.blit(imgWall1,[y * 30, x * 30])
        elif list[x][y] == ".":
            screen.blit(imgPoint,[y * 30, x * 30])
        else:
            screen.blit(imgWall2,[y * 30, x * 30])



pygame.display.flip()
#LOOP:mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
pygame.quit()
