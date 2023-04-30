from datetime import datetime, time, timedelta


def correct_date(date):
    return len(date.split(':')) == len(list(filter(lambda x: x.isdigit(), date.split(':')))) == 5


def correct_time_arrange(time_arrange):
    return len(time_arrange.split(':')) == len(list(filter(lambda x: x.isdigit(), time_arrange.split(':')))) == 2


def correct_time_report(begin_time, end_time, other_reports):
    if begin_time > end_time:
        return 'Время начала больше чем время окончания!'
    for report in other_reports:
        if report.begin < end_time and report.end > begin_time:
            return 'Время доклада пересекается с уже существующими докладами!'
    return 'Доклад добавлен в расписание конференции!)'


def report_time_in_conference(report, conference):
    return conference.begin <= report.begin


def help():
    print('Команды:', 'help - список команд', 'new conference - создать конференцию', 'new report - новый доклад',
          'full time - получить длительность конференции', 'breaks - получить список перерывов', 'exit - выход',
          'reports - список выступлений', 'confs - список конференций', sep='\n')


class Report:
    def __init__(self, theme, begin_date,
                 time_arrange):  # дата в формате 'yyyy:mm:dd:hh:mm', длительность 'hh:mm'
        self.theme = theme
        begin_date = list(map(int, begin_date.split(':')))
        self.begin = datetime(*begin_date)
        time_arrange = list(map(int, time_arrange.split(':')))
        self.time_arrange = time(*time_arrange)
        self.end = self.begin + timedelta(hours=time_arrange[0], minutes=time_arrange[1])


class Conference:
    def __init__(self, name, place, begin_date):  # дата в формате 'yyyy:mm:dd:hh:mm'
        self.name = name
        self.place = place
        begin_date = list(map(int, begin_date.split(':')))
        self.begin = datetime(*begin_date)
        self.reports = []

    def append_report(self, report):
        result = correct_time_report(report.begin, report.end, self.reports)
        if result == 'Доклад добавлен в расписание конференции!)':
            self.reports.append(report)
            self.reports.sort(key=lambda x: x.begin)
        return result

    def get_full_time(self):
        if not self.reports:
            return timedelta(0)
        result = max(self.reports, key=lambda x: x.end).end - self.begin
        return result

    def get_breaks(self):
        if not self.reports:
            return 'Нет выступлений!'
        breaks = [(self.begin, self.reports[0].begin)] if self.begin != self.reports[0].begin else []
        for i in range(len(self.reports) - 1):
            report = self.reports[i]
            breaks.append((report.end, self.reports[i + 1].begin))
        return breaks

    def get_reports(self):
        return list(map(lambda report: (report.theme, report.begin, report.end), self.reports))

    def get_num_of_reports(self):
        return len(self.reports)

    def get_num_of_breaks(self):
        return len(self.get_breaks())

    def get_place(self):
        return self.place

    def get_name(self):
        return self.name


confs = dict()
print('Добро пожаловать в сервис для планирования конференций и докладов в них!')
help()
print('-' * 20)
while True:
    command = input('Введите команду: ')
    if command == 'help':
        help()
    elif command == 'new conference':
        name = input(f'Введите название: ')
        while name in confs:
            print('Конференция с таким именем уже существует!')
            name = input(f'Введите название: ')
        begin_date = input('Введите дату начала в формате "yyyy:mm:dd:hh:mm": ')
        while not correct_date(begin_date):
            print('Дата указана в неверном формате.')
            begin_date = input('Введите дату начала в формате "yyyy:mm:dd:hh:mm": ')
        place = input('Введите место проведения: ')
        confs[name] = Conference(name, place, begin_date)
        print('Конференция спешно создана!')
    elif command == 'new report':
        conf_name = input(f'Введите название конференции в которой хотите выступить ({", ".join(confs.keys())}): ')
        while conf_name not in confs:
            print('Такой конференции не существует!')
            conf_name = input(f'Введите название конференции в которой хотите выступить ({", ".join(confs.keys())}): ')
        theme = input('Введите тему вашего выступления: ')
        begin_date = input('Введите дату начала в формате "yyyy:mm:dd:hh:mm": ')
        while not correct_date(begin_date):
            print('Дата указана в неверном формате.')
            begin_date = input('Введите дату начала в формате "yyyy:mm:dd:hh:mm": ')
        time_arrange = input('Введите продолжительность доклада в формате "hh:mm": ')
        while not correct_time_arrange(time_arrange):
            print('Длительность указана в неверном формате!')
            time_arrange = input('Введите продолжительность доклада в формате "hh:mm": ')
        report = Report(theme, begin_date, time_arrange)
        if report_time_in_conference(report, confs[conf_name]):
            print(confs[conf_name].append_report(report))
        else:
            print('Доклад начинается раньше начала конференции!')
    elif command == 'full time':
        conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        while conf_name not in confs:
            print('Такой конференции не существует!')
            conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        print(confs[conf_name].get_full_time())
    elif command == 'breaks':
        conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        while conf_name not in confs:
            print('Такой конференции не существует!')
            conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        breaks = confs[conf_name].get_breaks()
        print(*list(map(lambda x: f'{str(x[0])} - {str(x[1])}\n', breaks)) if isinstance(breaks, list) else breaks,
              sep='')
    elif command == 'reports':
        conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        while conf_name not in confs:
            print('Такой конференции не существует!')
            conf_name = input(f'Введите название конференции ({", ".join(confs.keys())}): ')
        reports = confs[conf_name].get_reports()
        print(
            *list(map(lambda x: f'Тема: {x[0]}\nДлительность: {str(x[1])} - {str(x[2])}\n\n', reports)) if reports
            else 'Нет выступлений', sep=''
        )
    elif command == 'confs':
        print(
            *list(map(lambda x: f'{confs[x].get_name()}: {confs[x].begin} - {confs[x].begin + confs[x].get_full_time()}, место: '
                                f'{confs[x].get_place()}, кол-во докладов: {len(confs[x].get_reports())}', confs)),
            sep='\n'
        )
    elif command == 'exit':
        break
    else:
        print('Данной команды не существует, для получения списка комманд - help')
    print('-' * 20)
print('Всего хо-ро-ше-го!')
