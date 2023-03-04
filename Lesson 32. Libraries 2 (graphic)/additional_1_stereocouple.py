from PIL import Image, ImageDraw


def makeanagliph(filename, delta):
    img = Image.open(filename)
    pxls = img.load()
    img2 = img.copy()
    pxls2 = img2.load()
    print(img2.size)
    x, y = img2.size
    # for i in range(y):
    #     for j in range(x):
    #         pxls2[j, i] = pxls[j - delta, i]
    for i in range(y):
        for j in range(x):
            pxls[j, i] = (pxls2[j - delta, i][0], pxls[j, i][1], pxls[j, i][2])
    img.save('res.jpg')


makeanagliph('image.jpg', 10)
