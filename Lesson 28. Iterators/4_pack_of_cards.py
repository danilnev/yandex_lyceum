import itertools


suits = ['пик', 'треф', 'бубен', 'червей']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
without_suit = input()
suits.remove(without_suit)
print('\n'.join(list(map(lambda x: ' '.join(x), itertools.product(numbers, suits)))))
