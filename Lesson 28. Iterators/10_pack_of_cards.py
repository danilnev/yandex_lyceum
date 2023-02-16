import itertools


def suit_and_num(cards):
    global great
    if 'червей' in itertools.chain(*cards) and (cards[0][0] in great or cards[1][0] in great or cards[2][0] in great):
        return True
    else:
        return False


suits = sorted(['пик', 'треф', 'бубен', 'червей'])
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
great = ['валет', 'дама', 'король', 'туз']
cards = list(itertools.product(numbers, suits))
cards = list(itertools.permutations(cards, 3))
cards = list(map(lambda x: sorted(x), sorted(cards)))
cards = list(filter(suit_and_num, cards))
print('\n'.join(map(lambda x: ', '.join([' '.join(y) for y in x]), cards[200:300])))
