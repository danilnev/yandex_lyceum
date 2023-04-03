class BaseObject:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def get_coordinates(self):
        return self.x, self.y, self.z


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x, self.y, self.z = x, y, z


class Thing(BaseObject):
    pass
