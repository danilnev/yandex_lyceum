def add_item(item_name, item_cost):
    global shopping
    shopping.append((item_name, item_cost))


def print_receipt():
    global shopping, check_count
    if len(shopping) > 0:
        print(f'Чек {check_count}. Всего предметов: {len(shopping)}')
        summ = 0
        for product in shopping:
            print(product[0], '-', product[1])
            summ += product[1]
        print('Итого:', summ)
        print('-----')
        shopping.clear()
        check_count += 1


shopping = []
check_count = 1

# add_item('Блокнот', 100)
# print_receipt()
#
# add_item('Ручка', 70)
# print_receipt()
# print_receipt()
#
# add_item('Булочка', 15)
# add_item('Булочка', 15)
# add_item('Чай', 5)
# print_receipt()
#
# add_item('Булочка', 15)
# add_item('Булочка', 15)
