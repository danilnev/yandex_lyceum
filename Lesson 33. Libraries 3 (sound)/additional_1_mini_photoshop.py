from PIL import Image


def temperature(size):
    '''Изменяет температуру изображения'''
    img = Image.open('image.jpg')
    pxls = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if size >= 0:
                pxls[i, j] = pxls[i, j][0] + size, pxls[i, j][1], pxls[i, j][2]
            else:
                pxls[i, j] = pxls[i, j][0], pxls[i, j][1], pxls[i, j][2] + abs(size)
    img.save('res.jpg')


def saturation(size):
    '''Изменяет контрастность изображения'''
    img = Image.open('image.jpg')
    pxls = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pxls[i, j] = pxls[i, j][0] + size, pxls[i, j][1] + size, pxls[i, j][2] + size
    img.save('res.jpg')
