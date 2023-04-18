class MailClient:
    def __init__(self, server, username):
        self.server, self.username = server, username

    def get_name(self):
        return self.username

    def get_server(self):
        return self.server

    def receive_mail(self):
        mail = self.server.get_mail(search_user(self.username))
        print(' ' * 10)
        if mail is None:
            return 'Для вас нет новых писем!'
        return '\n.....................\n'.join(list(map(lambda x: f'Письмо от {x[0]}:\n{x[1]}', mail)))

    def send_mail(self, server1, username1, message):
        server1.send_mail(self.username, search_user(username1), message)
        print('Ваше письмо успешно отправлено!')


class Server:
    def __init__(self, server_name):
        self.name = server_name
        self.mail = dict()

    def get_name(self):
        return self.name

    def send_mail(self, from_user, to_user, message):
        if to_user not in self.mail:
            self.mail[to_user] = []
        self.mail[to_user].append((from_user, message))

    def get_mail(self, username):
        if username not in self.mail or not self.mail[username]:
            return None
        result = self.mail[username]
        del self.mail[username]
        return result


def search_server(name):
    global servers
    for server in servers:
        if server.get_name() == name:
            return server
    return None


def search_user(name):
    global users
    for user in users:
        if user.get_name() == name:
            return user
    return None


def help():
    print('Комманды почты:', 'help - вызвать список комманд', 'send - отправить письмо', 'reg - регистрация клиента',
          'my mail - получить список моих писем', 'servers - список серверов', 'exit - выход', sep='\n')


def main():
    global users, servers
    servers = [Server('yandex'), Server('google'), Server('opera')]
    users = []
    print('Добро пожаловать в сервис по управлению почтой!')
    help()
    while True:
        command = input('Введите комманду: ')
        if command == 'help':
            help()
        elif command == 'reg':
            name = input('Введите ваше имя: ')
            while name == '':
                print('Имя не может быть пустым!')
                name = input('Введите ваше имя: ')
            print('Список серверов:', '\t'.join(list(map(lambda x: x.get_name(), servers))))
            server = input('Введите название сервера: ')
            while server not in list(map(lambda x: x.get_name(), servers)):
                print('Некорректное имя сервера!')
                server = input('Введите название сервера: ')
            users.append(MailClient(search_server(server), name))
            print('Клиент успешно зарегистрирован!')
        elif command == 'send':
            from_user = input('Введите ваше имя: ')
            if search_user(from_user) is None:
                print('Нет такого зарегистрированного пользователя!')
                from_user = input('Введите ваше имя: ')
            to_user = input('Введите имя получателя: ')
            if search_user(to_user) is None:
                print('Нет такого зарегистрированного пользователя!')
                to_user = input('Введите ваше имя: ')
            message = input('Введите сообщение (для переноса строки ставьте "\\n"):\n')
            search_user(from_user).send_mail(search_user(to_user).get_server(), to_user, message)
            print('Письмо успешно отправлено!')
        elif command == 'my mail':
            username = input('Введите ваше имя: ')
            while search_user(username) is None:
                print('Пользователя с таким именем не существует!')
                username = input('Введите ваше имя: ')
            user = search_user(username)
            print(user.receive_mail())
        elif command == 'servers':
            print('\n'.join(list(map(lambda x: f'- {x.get_name}', servers))))
        elif command == 'exit':
            print('Спасибо за пользование нашим сервисом, удачи!')
            break
        else:
            print('Нет такой команды, введите корректное имя или вызовите помощник командой "help"')
        print(' ' * 10)


if __name__ == '__main__':
    main()
