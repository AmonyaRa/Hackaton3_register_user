'''Регистрация User'''
import json


def validate_password(password):
    if len(password) < 8:
        raise Exception('Пароль слишком короткий!')
    elif not password.isalnum():
        raise Exception('Пароль должен состоять из букв и цифр!')


class FileProcessing:
    @staticmethod
    def search_file():
        try:
            with open('user.json', 'x') as file:
                data = json.dump([], file)
        except Exception:
            pass

    @staticmethod
    def get_file():
        with open('user.json') as file:
            return json.load(file)


class RegisterMixin(FileProcessing):
    def register(self, name, password):
        self.search_file()
        data = self.get_file()
        validate_password(password)
        if any(i['name'].upper() == name.upper() for i in data):
            raise Exception('Такой юзер уже существует!')
        else:
            if data:
                id = max([i['id'] for i in data]) + 1
            else:
                id = 1
            data.append({
                'id': id,
                'name': name,
                'password': password
            }
            )
            with open('user.json', 'w') as file:
                json.dump(data, file)
            return 'Successfully registered'


class LoginMixin(FileProcessing):
    def login(self, name, password):
        data = self.get_file()
        if any(i['name'] != name for i in data):
            raise Exception ('Нет такого юзера в БД!')
        elif any(i['password'] != password for i in data):
            raise Exception ('Неверный пароль!')
        return 'Вы успешно залогинились!'


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        pass


'''ChangePasswordMixin - реализуйте в нем метод 'change_password' который будет изменять пароль пользователя. Метод принимает 3 аргумента name, old_password, new_password. В первую очередь проверьте новый пароль на валидность с помощью созданной вами функцией. Далее проверьте совпадает ли переданный пароль юзера с паролем юзера из БД(user.json), если нет то сгенерируйте исключение с сообщением 'Старый пароль указан не верно!'. В ином случае измените новый пароль у юзера в БД(user.json) и возвратите сообщение 'Password changed successfully!'''


class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        pass


'''ChangeUsernameMixin - реализуйте в нем метод 'change_name' который будет изменять имя юзера. Метод принимает 2 аргумента old_name и new_name. В первую очередь проверьте существует ли такой юзер которого хотим изменить в БД(user.json), если его нет то сгенерируйте исключение с сообщением 'Нет такого зарегистрированного юзера в БД!'. Далее проверьте, не занято юзера с новым именем в БД. Если же такое имя уже существует выведите сообщение 'Пользователь с таким именем уже существует!', и попросите пользователя вводить новое имя до тех пор пока она не станет уникальным. Как только новое имя будет уникальным в рамках нашей БД, перезапишите это имя у пользователя в БД и возвратите сообщение "Username changed successfully!"'''


class CheckOwnerMixin:
    def check(self, owner):
        pass


'''CheckOwnerMixin - миксин содержит метод 'check' который принимает аргумент 'owner' и просто проверят если переданное имя 'owner' в БД(user.json). Если его нет то сгенерировать исключение с сообщением 'Нет такого пользователя!'. Иначе создаваемый объект от класса Post будет успешно создан. (Запись постов записывать в БД не надо!)'''


class User:
    pass


class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner


obj = RegisterMixin()
obj.register('Sam', '1b2jjjj34')
# obj1 = LoginMixin()
# obj1.login('john', '1b234kk')