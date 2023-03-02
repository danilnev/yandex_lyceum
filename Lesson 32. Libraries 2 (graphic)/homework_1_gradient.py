from PIL import Image, ImageDraw


def gradient(color):
    img = Image.new('RGB', (512, 200))
    draw = ImageDraw.Draw(img)
    count = 0
    if color.upper() == 'R':
        for i in range(0, 512, 2):
            draw.line(((i, 0), (i, 200)), (count, 0, 0))
            draw.line(((i + 1, 0), (i + 1, 200)), (count, 0, 0))
            count += 1
    if color.upper() == 'G':
        for i in range(0, 512, 2):
            draw.line(((i, 0), (i, 200)), (0, count, 0))
            draw.line(((i + 1, 0), (i + 1, 200)), (0, count, 0))
            count += 1
    if color.upper() == 'B':
        for i in range(0, 512, 2):
            draw.line(((i, 0), (i, 200)), (0, 0, count))
            draw.line(((i + 1, 0), (i + 1, 200)), (0, 0, count))
            count += 1
    img.save('res.png')


gradient('g')
