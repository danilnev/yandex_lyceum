class Num:
    def __init__(self, value):
        self.v = value

    def make_negative(self):
        if self.v > 0:
            self.v = -self.v
        return self

    def square(self):
        self.v = self.v ** 2
        return self

    def strange_command(self):
        if self.v % 5 == 0:
            self.v += 1
        return self

    def __str__(self):
        return str(self.v)


numbers = input().split()
numbers = list(map(lambda x: Num(int(x)), numbers))
num_cmds = int(input())
for i in range(num_cmds):
    command = input()
    if command == 'make_negative':
        numbers = list(map(lambda x: x.make_negative(), numbers))
    elif command == 'square':
        numbers = list(map(lambda x: x.square(), numbers))
    elif command == 'strange_command':
        numbers = list(map(lambda x: x.strange_command(), numbers))
print(*numbers)
