def do_bet(horse_number, bet):
    global bets
    if 1 <= horse_number <= 10 and horse_number not in bets and bet > 0:
        bets[horse_number] = bet
        print(f'Ваша ставка в размере {bet} на лошадь {horse_number} принята')
    else:
        print('Что-то пошло не так, попробуйте еще раз')


bets = dict()

# do_bet(1, 10)
# do_bet(1, 100)
# do_bet(2, 0)
# do_bet(2, 200)
