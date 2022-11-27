num = int(input())
waves = []
for i in range(num):
    string = input()
    waves.append((int(string[-1]), string[:len(string) - 2]))
result_waves = []
for i in range(num - 1):
    if waves[i][0] < waves[i + 1][0]:
        result_waves.append((i + 1, waves[i][1]))
for wave in result_waves:
    print(wave)