from PIL import Image, ImageDraw

x = 1600
y = 400
bg_colors = [(41, 217, 22), (70, 115, 65), (29, 117, 19), (148, 222, 140)]
img = Image.new('RGB', (x, y), bg_colors[0])
draw = ImageDraw.Draw(img)

color_count = 1
for i in range(0, x, x // 4):
    draw.rectangle(
        ((i, 0), (i + (x / 4), y)),
        bg_colors[color_count]
    )
    color_count += 1
    if color_count == 4:
        color_count = 0

d_color = (204, 37, 37)
circle_size = y // 10
els = (0, (x // 4) - circle_size)
for el in els:
    for i in range(circle_size, circle_size * 3 + 1, circle_size):
        draw.ellipse(
            ((el, y - i), (el + circle_size, y - i + circle_size)),
            d_color
        )
els = (circle_size * 3, circle_size * 6)
for el in els:
    for i in range(circle_size * 3, y + 1, circle_size):
        draw.ellipse(
            ((el, y - i), (el + circle_size, y - i + circle_size)),
            d_color
        )
d_color = (0, 0, 0)
els = (circle_size, circle_size * 4, circle_size * 7)
for el in els:
    draw.rectangle(
        ((el, y - circle_size * 3), (el + (circle_size * 2), y - circle_size * 2)),
        d_color
    )
draw.rectangle(
    ((circle_size * 4, 0), (circle_size * 6, circle_size)),
    d_color)

a_colors = [(78, 237, 176), (17, 63, 122), (292, 51, 196)]
draw.polygon(
    ((x // 4, y), (x // 4 + y // 2, 0), (x // 4 + y // 2 + y * 0.075, y * 0.075), (x // 4 + y * 0.1, y)), a_colors[0]
)
draw.polygon(
    ((x // 4 + y // 2 + y * 0.075, y * 0.075), (x // 4 * 2, y), (x // 4 * 2 -
                                                                 y * 0.05, y), (x // 4 + y * 0.5, y * 0.23)),
    a_colors[1]
)
draw.polygon(
    ((490, 300), (755, 300), (770, 330), (475, 330)), a_colors[2]
)

n_color = 232, 139, 26
draw.ellipse(
    ((880, 20), (920, 60)), n_color
)
draw.rectangle(
    ((880, 40), (920, 360)), n_color
)
draw.ellipse(
    ((880, 340), (920, 380)), n_color
)
draw.rectangle(
    ((920, 200), (1080, 230)), n_color
)
draw.ellipse(
    ((1080, 20), (1120, 60)), n_color
)
draw.rectangle(
    ((1080, 40), (1120, 360)), n_color
)
draw.ellipse(
    ((1080, 340), (1120, 380)), n_color
)

ya_colors = [(0, 255, 200)]
draw.ellipse(
    ((1560, 10), (1600, 50)), ya_colors[0]
)
draw.rectangle(
    ((1560, 30), (1600, 360)), ya_colors[0]
)
draw.ellipse(
    ((1560, 340), (1600, 380)), ya_colors[0]
)
img.save('res.jpg')
