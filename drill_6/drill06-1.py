from pico2d import *

open_canvas()

grass = load_image('grass.png')
# 객체를 생성
character = load_image('character.png')

x = 0
y = 90
while (x < 750):
    clear_canvas_now()
    grass.draw_now(400, 30)
    # 객체를 2d로 보여줌
    character.draw_now(x,90)
    x = x + 2
    delay(0.01)
    
while (y < 550):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(750,y)
    y = y + 2
    delay(0.01)
    
while (x >50):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,550)
    x = x - 2
    delay(0.01)

while (y >90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(50,y)
    y = y - 2
    delay(0.01)

while( x < 400):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.01)

import math
import matplotlib.pyplot as plt
circle_center = (400, 340)    # 원의 중심
circle_radius = 20       # 원의 반지름
x = 270
y = 270
while cos(x) < 1 and sin(y) < 0 :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    cos(x) == cos(x) + 0.1
    sin(y) == sin(y) + 0.1
    delay(0.01)
close_canvas()

