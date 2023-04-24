class Transformations:
    def __init__(self, name, objects):
        self.name, self.objects = name, list(objects)

    def append(self, string):
        self.objects.append(string)

    def __sub__(self, other):
        name = self.name[:5] + other.name[-3:]
        objects = sorted(list(set(self.objects) - set(other.objects)))
        return Transformations(name, objects)

    def __itruediv__(self, other):
        self.objects = self.objects[:other]
        return self

    def __call__(self, number):
        return tuple(filter(lambda x: len(x) <= number, self.objects))

    def __str__(self):
        return f'Transformations by name {self.name}: {", ".join(self.objects)}'

    def __eq__(self, other):
        return self.name == other.name and self.objects == other.objects

    def __ne__(self, other):
        return not (self.name == other.name and self.objects == other.objects)

    def __gt__(self, other):
        if len(self.objects) > len(other.objects):
            return True
        elif len(self.objects) == len(other.objects):
            if self.objects > other.objects:
                return True
            elif self.objects == other.objects:
                if self.name > other.name:
                    return True
        return False

    def __ge__(self, other):
        if len(self.objects) > len(other.objects):
            return True
        elif len(self.objects) == len(other.objects):
            if self.objects > other.objects:
                return True
            elif self.objects == other.objects:
                if self.name >= other.name:
                    return True
        return False

    def __lt__(self, other):
        if len(self.objects) < len(other.objects):
            return True
        elif len(self.objects) == len(other.objects):
            if self.objects < other.objects:
                return True
            elif self.objects == other.objects:
                if self.name < other.name:
                    return True
        return False

    def __le__(self, other):
        if len(self.objects) < len(other.objects):
            return True
        elif len(self.objects) == len(other.objects):
            if self.objects < other.objects:
                return True
            elif self.objects == other.objects:
                if self.name <= other.name:
                    return True
        return False


tr = Transformations('Illmarrannen', ('snake', 'lizard'))
tr1 = Transformations('Rual', ('rabbit', 'owl'))
print(tr, tr1, sep='\n')
print(tr > tr1, tr <= tr1, tr != tr1)
tr.append('owl')
tr1.append('lizard')
tr2 = tr - tr1
print(tr, tr1, tr2, sep='\n')
print(tr < tr2, tr2 >= tr1, tr2 == tr1)
print('hell0'[-3:])