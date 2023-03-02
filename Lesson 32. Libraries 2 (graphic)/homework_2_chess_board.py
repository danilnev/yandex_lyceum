from PIL import Image, ImageDraw


def board(num, size):
    img = Image.new('RGB', (num * size, num * size))
    draw = ImageDraw.Draw(img)
    for i in range(0, num * size, size):
        if i % (size * 2) == 0:
            for j in range(0, num * size, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        ((i, j), (i + size, j + size)), (0, 0, 0)
                    )
                else:
                    draw.rectangle(
                        ((i, j), (i + size, j + size)), (255, 255, 255)
                    )
        else:
            for j in range(0, num * size, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        ((i, j), (i + size, j + size)), (255, 255, 255)
                    )
                else:
                    draw.rectangle(
                        ((i, j), (i + size, j + size)), (0, 0, 0)
                    )
    img.save('res.png')


board(5, 30)
