from PIL import Image
import itertools


image = Image.open('image.jpg')
pixels = image.load()
r, g, b = 0, 0, 0
for i, j in itertools.product(range(image.size[0]), range(image.size[1])):
    r += pixels[i, j][0]
    g += pixels[i, j][1]
    b += pixels[i, j][2]
size = image.size[0] * image.size[1]
print(r // size, g // size, b // size)
