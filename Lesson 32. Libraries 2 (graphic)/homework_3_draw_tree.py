from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color=(117, 187, 253), snow_color=(255, 250, 250),
            trunk_color=(164, 90, 82), needls_color=(1, 121, 111), sun_color=(255, 219, 0)):
    img = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse(((width * 0.8, -height * 0.2), (width * 1.2, height * 0.2)), sun_color)
    draw.rectangle(((0, height * 0.8), (width, height)), snow_color)
    draw.rectangle(((width * 0.45, height * 0.7), (width * 0.55, height * 0.9)), trunk_color)
    draw.polygon(
        (
            (width * 0.3, height * 0.7),
            (width * 0.40, height * 0.5),
            (width * 0.35, height * 0.5),
            (width * 0.45, height * 0.3),
            (width * 0.40, height * 0.3),
            (width * 0.50, height * 0.1),
            (width * 0.6, height * 0.3),
            (width * 0.55, height * 0.3),
            (width * 0.65, height * 0.5),
            (width * 0.6, height * 0.5),
            (width * 0.7, height * 0.7)
        ),
        needls_color
    )
    img.save(file_name)


picture('res.bmp', 1000, 800)
