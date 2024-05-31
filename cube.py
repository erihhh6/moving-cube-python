import pygame as pg
from math import *
import numpy as np

clock = pg.time.Clock()
size = (1000,1000)
speed = 0.05
pg.init()
screen = pg.display.set_mode(size)

projection_matrix = [
    [1,0,0],
    [0,1,0],
    [0,0,0]
]


cube_points = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]

angle_x=angle_y=angle_z=0
def multip_matrix(a,b):
    return np.matmul(a,b)
def controls():
    global angle_x, angle_y, angle_z
    keys = pg.key.get_pressed()
    angle_y+=keys[pg.K_a] * speed
    angle_y-=keys[pg.K_d] * speed
    angle_x+=keys[pg.K_w] * speed
    angle_x-=keys[pg.K_s] * speed
    angle_z-=keys[pg.K_q] * speed
    angle_y+=keys[pg.K_e] * speed

def draw_lines(i,j,lista):
    pg.draw.line(screen,'red',(lista[i][0],lista[i][1]),(lista[j][0],lista[j][1]),1)


offset = 250
while True:
    screen.fill('black')
    controls()
    rotation_x = [
        [1,0,0],
        [0,cos(angle_x),-sin(angle_x)],
        [0,sin(angle_x),cos(angle_x)]
    ]
    rotation_y = [
        [cos(angle_y),0,sin(angle_y)],
        [0,1,0],
        [-sin(angle_y),0,cos(angle_y)]
    ]
    rotation_z = [
        [cos(angle_z),-sin(angle_z),0],
        [sin(angle_z),cos(angle_z),0],
        [0,0,1]
    ] 
    
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()
    lista = [0 for n in range(len(cube_points))]
    i = 0
    for points in cube_points:
        rotate_x = multip_matrix(points,rotation_x)
        rotate_y = multip_matrix(rotate_x,rotation_y)
        rotate_z = multip_matrix(rotate_y,rotation_z)
        points2d = multip_matrix(rotate_z,projection_matrix)
        x = (points2d[0] * offset) + 450
        y = (points2d[1] * offset) + 450
        lista[i] = (x,y)
        i+=1
        pg.draw.circle(screen,'red',(x,y),5)
    """
    angle_x+=0.01
    angle_y+=0.01
    angle_z+=0.01
    """
    draw_lines(0,1,lista)
    draw_lines(0,4,lista)
    draw_lines(0,2,lista)
    draw_lines(1,3,lista)
    draw_lines(1,5,lista)
    draw_lines(2,3,lista)
    draw_lines(2,6,lista)
    draw_lines(3,7,lista)
    draw_lines(4,6,lista)
    draw_lines(4,5,lista)
    draw_lines(5,7,lista)
    draw_lines(6,7,lista)








    pg.display.flip()