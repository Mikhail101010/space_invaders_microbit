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
game_start_time = 0
while run:
    if stoped:
        amogus()
        game_running = False
        stoped = False
    if not game_running:
        if input.button_is_pressed(Button.A):
            game_start_time = input.running_time()
            game_running = True
            clear()
    else:
        if input.button_is_pressed(Button.B):
            stoped = True
        else:
            basic.show_number(int((input.running_time() - game_start_time) / 1000))