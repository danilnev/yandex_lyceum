class SparseArray:
    def __init__(self):
        self.obj = dict()

    def __setitem__(self, key, value):
        self.obj[key] = value

    def __getitem__(self, item):
        if item in self.obj:
            return self.obj[item]
        else:
            return 0
