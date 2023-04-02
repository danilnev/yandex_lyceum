class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.prote = proteins
        self.fats = fats
        self.cd = carbohydrates

    def get_proteins(self):
        return self.prote

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.cd

    def get_kcalories(self):
        return 4 * self.prote + 9 * self.fats + 4 * self.cd

    def __add__(self, other):
        return FoodInfo(self.prote + other.prote, self.fats + other.fats, self.cd + other.cd)
