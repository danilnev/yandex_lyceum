from PIL import Image, ImageFilter


def motion_blur(n):
    img1 = Image.open('4_rotate_with_blur/image.jpg')
    img1 = img1.transpose(Image.ROTATE_270)
    img1 = img1.filter(ImageFilter.GaussianBlur(radius=n))
    img1.save('res.jpg')


motion_blur(10)
