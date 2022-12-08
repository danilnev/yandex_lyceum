num = int(input())
bottles = [int(input()) for i in range(num)]
minn = int(input())
maxx = int(input())
print('\n'.join([str(bottle) for bottle in bottles if minn <= bottle <= maxx]))
