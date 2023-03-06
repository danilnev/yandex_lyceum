from PIL import Image


def twist_image(input_file_name, output_file_name):
    img = Image.open(input_file_name)
    pxls = img.load()
    for j in range(img.size[1]):
        for i in range(img.size[0] // 2):
            pxls[i, j], pxls[i + img.size[0] // 2, j] = pxls[i + img.size[0] // 2, j], pxls[i, j]
    img.save(output_file_name)


twist_image('1_graphic_mixer/image.jpg', 'res.jpg')
