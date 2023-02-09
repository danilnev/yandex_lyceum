import sys


data = sys.stdin.readlines()
if len(data) == 0:
    print(-1)
else:
    heights = list(map(lambda x: int(x.rstrip('\n')), data))
    print(sum(heights) / len(heights))
