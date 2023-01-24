def get_transactions(t):
    global transactions
    if t == 'print_it':
        for trans in transactions:
            print(transactions[trans][0], trans, transactions[trans][1])
    else:
        transaction, money = t.split('-')[1].split(':')
        if transaction not in transactions:
            transactions[transaction] = [1, int(money)]
        else:
            transactions[transaction][0] += 1
            transactions[transaction][1] += int(money)


transactions = dict()
# get_transactions('880005553535-перевод:100')
# get_transactions('111111111-перевод:1000')
# get_transactions('880005553535-оплата_жкх:10000')
# get_transactions('89065664312-перевод:50000000')
# get_transactions('print_it')
