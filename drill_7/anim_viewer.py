from pico2d import *

open_canvas()

grass = load_image('mapleback.png')
character = load_image('raccoon_villion.png')
num = 0
x = 800
frame = 0

while (x >= 400):
    clear_canvas()
    grass.draw(400,300)
    character.clip_draw(frame * 85, 1080, 80, 78, x, 95)
    # 캔버스에서 원점은 왼쪽 밑 점이기에 첫 캐릭터의 왼쪽 밑이 원점
    # left 는 x좌표,bottom은 y좌표
    update_canvas()
    frame = (frame + 1) % 10
    # 일정 범위내에서 숫자를 돌려서 계속 증가시키는 방식 (0~7까지만 나오게함)
    x -= 5
    delay(0.06)
    get_events()
    # 넣어줘야 내부적으로 프로세스가 안막힌다고 함

for num in range(0,40,1):
    clear_canvas()
    grass.draw(400,300)
    character.clip_draw(frame * 93, 964, 80, 110, 400, 95)
    # 캔버스에서 원점은 왼쪽 밑 점이기에 첫 캐릭터의 왼쪽 밑이 원점
    # left 는 x좌표,bottom은 y좌표
    update_canvas()
    frame = (frame + 1) % 7
    # 일정 범위내에서 숫자를 돌려서 계속 증가시키는 방식 (0~7까지만 나오게함)
    delay(0.06)
    get_events()
    
while (x >= 100):
    clear_canvas()
    grass.draw(400,300)
    character.clip_draw(frame * 86, 771, 83, 100, x, 90)
    # 캔버스에서 원점은 왼쪽 밑 점이기에 첫 캐릭터의 왼쪽 밑이 원점
    # left 는 x좌표,bottom은 y좌표
    update_canvas()
    frame = (frame + 1) % 4
    # 일정 범위내에서 숫자를 돌려서 계속 증가시키는 방식 (0~7까지만 나오게함)
    x -= 5
    delay(0.06)
    get_events()



for num in range(0, 5, 1):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw(frame * 87, 183, 80, 88, 100, 95)
        # 캔버스에서 원점은 왼쪽 밑 점이기에 첫 캐릭터의 왼쪽 밑이 원점
        # left 는 x좌표,bottom은 y좌표
        update_canvas()
        frame = (frame + 1) % 5
        # 일정 범위내에서 숫자를 돌려서 계속 증가시키는 방식 (0~7까지만 나오게함)
        delay(0.30)
        get_events()

for num in range(0, 2, 1):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw((frame * 168) + 528, 173, 200, 200, 100, 135)
        # 캔버스에서 원점은 왼쪽 밑 점이기에 첫 캐릭터의 왼쪽 밑이 원점
        # left 는 x좌표,bottom은 y좌표
        update_canvas()
        frame = (frame + 1) % 2
        # 일정 범위내에서 숫자를 돌려서 계속 증가시키는 방식 (0~7까지만 나오게함)
        delay(0.20)
        get_events()
close_canvas()

