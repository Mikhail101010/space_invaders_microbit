def draw_rect(x, y, x2, y2):
    for x_axis in range(x - 1, x2):
        for y_axis in range(y - 1, y2):
            led.plot(x_axis, y_axis)
def clear():
    for x_axis in range(0, 5):
            for y_axis in range(0, 5):
                led.unplot(x_axis, y_axis)
def amogus():
    draw_rect(2, 1, 3, 1)
    draw_rect(1, 2, 1, 5)
    draw_rect(2, 4, 4, 5)
    draw_rect(3, 2, 5, 3)

run = True
stoped = True
game_running = False
while run:
    