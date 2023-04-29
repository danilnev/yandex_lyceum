class SqrtFun:
    def __call__(self, x):
        return x ** 0.5


class X:
    def __call__(self, x):
        return x


class Task:
    def __init__(self, arg1, sign, arg2):
        self.arg1, self.sign, self.arg2 = arg1, sign, arg2

    def __call__(self, x):
        arg1 = self.arg1(x)
        arg2 = self.arg2(x)
        if self.sign == '*':
            return arg1 * arg2
        elif self.sign == '/':
            return arg1 / arg2
        elif self.sign == '+':
            return arg1 + arg2
        return arg1 - arg2


class Value:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value


num = int(input())
funcs = {'sqrt_fun': SqrtFun(), 'x': X()}
for i in range(num):
    command = input().split()
    if command[0] == 'calculate':
        print(*list(map(funcs[command[1]], map(int, command[2:]))))
    elif command[0] == 'define':
        name = command[1]
        sign = command[3]
        if command[2].isdigit():
            arg1 = Value(int(command[2]))
        elif command[2][0] == '-' and command[2][1:].isdigit():
            arg1 = Value(int(command[2][1:]) * -1)
        else:
            arg1 = funcs[command[2]]
        if command[4].isdigit():
            arg2 = Value(int(command[4]))
        elif command[4][0] == '-' and command[4][1:].isdigit():
            arg2 = Value(int(command[4][1:]) * -1)
        else:
            arg2 = funcs[command[4]]
        funcs[name] = Task(arg1, sign, arg2)
