class ReversedList:
    def __init__(self, array):
        self.array = [array[i] for i in range(len(array) - 1, -1, -1)]

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[len(self)]
