from PIL import Image


def thoughts(filename, length, *crds):
    from_img = Image.open(filename)
    to_img = Image.new('RGB', (length * len(crds), length))
    for i, crd in enumerate(crds):
        image = from_img.crop((*crd, crd[0] + length, crd[1] + length))
        if i % 2 == 1:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        to_img.paste(image, (length * i, 0))
    to_img.save('dreams.png')


thoughts('way.png', 200, (0, 350), (200, 300), (600, 80), (550, 450))
