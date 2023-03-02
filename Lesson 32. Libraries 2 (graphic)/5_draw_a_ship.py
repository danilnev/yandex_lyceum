from PIL import ImageDraw, Image


def picture(file_name, width, height, sky_color=(135, 206, 235), ocean_color=(1, 123, 146), boat_color=(135, 69, 53),
            sail_color=(255, 255, 255), sun_color=(255, 207, 64)):
    img = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse(((width * 0.8, -height * 0.2), (width * 1.2, height * 0.2)), sun_color)
    draw.rectangle(((0, height * 0.8), (width, height)), ocean_color)
    draw.polygon(
        (
            (width * 0.3, height * 0.85),
            (width * 0.25, height * 0.65),
            (width * 0.49, height * 0.65),
            (width * 0.49, height * 0.3),
            (width * 0.51, height * 0.3),
            (width * 0.51, height * 0.65),
            (width * 0.75, height * 0.65),
            (width * 0.7, height * 0.85)
        ),
        boat_color
    )
    draw.polygon(
        (
            (width * 0.51, height * 0.3),
            (width * 0.66, height * 0.45),
            (width * 0.51, height * 0.60)
        ),
        sail_color
    )
    img.save(file_name)


picture('res.bmp', 1000, 800)
