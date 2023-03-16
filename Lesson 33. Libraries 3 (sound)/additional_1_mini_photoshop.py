from PIL import Image


def temperature(pxls, i, j, ugrade_size=100):
    '''Изменяет температуру изображения'''
    for i in range(10):
        for j in range(10):
            if ugrade_size >= 0:
                pxls[i, j] = pxls[i, j][0] + ugrade_size, pxls[i, j][1], pxls[i, j][2]
            else:
                pxls[i, j] = pxls[i, j][0], pxls[i, j][1], pxls[i, j][2] + abs(ugrade_size)
    return pxls


def saturation(pxls, i, j, upgrade_size=100):
    '''Изменяет контрастность изображения'''
    for i in range(10):
        for j in range(10):
            pxls[i, j] = pxls[i, j][0] + upgrade_size, pxls[i, j][1] + upgrade_size, pxls[i, j][2] + upgrade_size
    return pxls


# img = Image.open('image.png')
# pixels = img.load()
# pixels = saturation(pixels, 2, 3)
# img.save('image.png')
