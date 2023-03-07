from PIL import Image
# import itertools


def mirror():
    img = Image.open('image.jpg')
    # pxls = img.load()
    # for i, j in itertools.product(range(img.size[0] // 2 + 1), range(img.size[1])):
    #     pxls[i, j], pxls[img.size[0] - i - 1, j] = pxls[img.size[0] - i - 1, j], pxls[i, j]
    # for i, j in itertools.product(range(img.size[0]), range(img.size[1] // 2 + 1)):
    #     pxls[i, j], pxls[i, img.size[1] - j - 1] = pxls[i, img.size[1] - j - 1], pxls[i, j]
    img = img.transpose(Image.ROTATE_270).transpose(Image.FLIP_TOP_BOTTOM)
    img.save('res.jpg')


mirror()
