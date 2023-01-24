def setup_profile(name, vacation_date):
    global people_name, date
    people_name = name
    date = vacation_date


def print_application_for_leave():
    global people_name, date
    print(f'Заявление на отпуск в период {date}. {people_name}')


def print_holiday_money_claim(amount):
    global people_name
    print(f'Прошу выплатить {amount} отпускных денег. {people_name}')


def print_attorney_letter(to_whom):
    global people_name, date
    print(f'На время отпуска в период {date} моим заместителем назначается {to_whom}. {people_name}')


people_name = None
date = None
# setup_profile("Иван Петров", "1 июня – 20 июня")
# print_application_for_leave()
# print_application_for_leave()
# print_holiday_money_claim("15 тысяч пиастров")
# print_attorney_letter("Василий Васильев")
