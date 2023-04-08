from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.colors = dict()
        self.row_size = len(draw_map)
        self.col_size = len(draw_map[0])

    def numbers(self):
        return sorted(list(set(sum(self.draw_map, []))))

    def set_color(self, number, color):
        self.colors[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        return self.col_size * self.cell_size, self.row_size * self.cell_size

    def draw(self):
        image = Image.new('RGB', self.size())
        draw = ImageDraw.Draw(image)
        x, y = 0, 0
        for row in self.draw_map:
            for col in row:
                draw.rectangle((self.cell_size * x, self.cell_size * y,
                               self.cell_size * x + self.cell_size, self.cell_size * y + self.cell_size),
                               self.colors.get(col, 'black'))
                x += 1
            y += 1
            x = 0
        return image


image = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20)
image.set_color(1, 'black')
image.set_color(2, 'red')
image.set_color(3, 'orange')
image.set_color(4, 'yellow')
image.set_color(5, 'green')
image.set_color(6, 'lightblue')
image.set_color(7, 'blue')
image.set_color(8, 'violet')
image.set_color(9, 'white')
image.draw().save('res.png')
