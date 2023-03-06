from PIL import Image


def transparency(filename1, filename2):
    img1 = Image.open(filename1)
    img2 = Image.open(filename2)
    pxls1 = img1.load()
    pxls2 = img2.load()
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r = int(pxls1[i, j][0] * 0.5 + pxls2[i, j][0] * 0.5)
            g = int(pxls1[i, j][1] * 0.5 + pxls2[i, j][1] * 0.5)
            b = int(pxls1[i, j][2] * 0.5 + pxls2[i, j][2] * 0.5)
            pxls2[i, j] = (r, g, b)
    img2.save('res.jpg')


transparency('img1.jpg', 'img2.jpg')
