from PIL import Image
import itertools


def mirror():
    img = Image.open('image.jpg')
    pxls = img.load()
    for i, j in itertools.product(range(img.size[0] // 2), range(img.size[1])):
        pxls[i, j], pxls[img.size[0] - i - 1, j] = pxls[img.size[0] - i - 1, j], pxls[i, j]
    img.save('res.jpg')
