function draw_rect(x: number, y: number, x2: number, y2: number) {
    for (let x_axis = x - 1; x_axis < x2; x_axis++) {
        for (let y_axis = y - 1; y_axis < y2; y_axis++) {
            led.plot(x_axis, y_axis)
        }
    }
}

function clear() {
    for (let x_axis = 0; x_axis < 5; x_axis++) {
        for (let y_axis = 0; y_axis < 5; y_axis++) {
            led.unplot(x_axis, y_axis)
        }
    }
}

function amogus() {
    draw_rect(2, 1, 3, 1)
    draw_rect(1, 2, 1, 5)
    draw_rect(2, 4, 4, 5)
    draw_rect(3, 2, 5, 3)
}

let run = true
let stoped = true
let game_running = false
