days = int(input())
soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
for i in range(days):
    print(soups[i % 5])