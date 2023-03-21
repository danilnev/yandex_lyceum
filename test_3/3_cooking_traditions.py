from PIL import Image, ImageDraw


def culinary_tradition(filename, w, *colors):
    size = (w * 6, int(w * 3.5))
    mid, fill, bg = colors
    img = Image.new('RGB', size, bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle(
        ((w * 1.5, w * 1.75), (w * 4.5, w * 3.5)), mid
    )
    draw.ellipse(
        ((0, -(w * 2.5)), (w * 6, w * 3)), mid
    )
    draw.rectangle(
        ((0, 0), (w * 6, w * 0.5)), bg
    )
    draw.ellipse(
        ((0, 0), (w * 6, w)), fill
    )
    img.save(filename)
