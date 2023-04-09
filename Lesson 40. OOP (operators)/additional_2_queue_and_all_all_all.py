class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def append(self, *values):
        self.queue += values

    def copy(self):
        return Queue(*self.queue.copy())

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def extend(self, queue):
        self.queue += queue.queue

    def next(self):
        return Queue(*self.queue[1:])

    def __add__(self, other):
        return Queue(*(self.queue + other.queue))

    def __iadd__(self, other):
        self.queue += other.queue
        return self

    def __eq__(self, other):
        return self.queue == other.queue

    def __rshift__(self, n):
        if n >= len(self.queue):
            return Queue()
        else:
            return Queue(*self.queue[n:])

    def __str__(self):
        return '[' + ' -> '.join(list(map(str, self.queue))) + ']'

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
