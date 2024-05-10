"""1.1Написать функцию, которая принимает список пользователей
(имеющуюся структуру данных [ {}, {}, .. ]) и
печатает имена этих пользователей и возраст в консоль.

1.2Написать функцию, которая принимает список пользователей
 (имеющуюся структуру данных [ {}, {}, .. ]) и
 печатает имя и возраст в консоль тех пользователей,
 возраст которых больше либо равен 18 лет.
1.2* Изменить функцию, так,
что бы функция принимала вторым параметром возраст для проверки.

1.3 Написать функцию,
которая принимает список пользователей
(имеющуюся структуру данных [ {}, {}, .. ]) и
печатает в консоль словарь,
где ключ имя пользователя а значение - список с гражданствами пользователя

1.4 Написать функцию,
которая принимает список пользователей
(имеющуюся структуру данных [ {}, {}, .. ])
и добавляет пользователю данные статуса. Значение статуса устанавливать
в suspicious, если пользователь младше 18 и работает или старше 18 и не работает..
в not_suspicious, если пользователь младше 18 и не работает или старше 18 и работает.
Функция должна возвращать обновленный список с пользователями.
"""


users = [
    {
        'name': 'Victor',
        'age': 24,
        'is_working': False,
        'citizenship': ['Russian', 'England']
    },
    {
        'name': 'Anastasia',
        'age': 32,
        'is_working': True,
        'citizenship': ['Czech']
    },
    {
        'name': 'Bobbi',
        'age': 12,
        'is_working': False,
        'citizenship': ['American']
    },
    {
        'name': 'Tomas',
        'age': 48,
        'is_working': True,
        'citizenship': ['Greek', 'Spanish']
    }
]


def publish_name_age(users_pull=None):
    """We get a list of dictionaries with user data.
    We display Name and Age in the terminal"""
    if users_pull is None:
        users_pull = users
    for user_data in users_pull:
        user_data = list(user_data.items())
        name = user_data[0][1]
        age = user_data[1][1]
        print('name : ', name)
        print('age : ', age)


def age_verification(age_verific=None, users_pull=None):
    """Get a list of dictionaries with user data.
    Get age verification.
    Display in the console the names and ages
    of those users who have passed verification"""
    if users_pull is None:
        users_pull = users
    if age_verific is None:
        age_verific = 18
    for user_data in users_pull:
        user_data = list(user_data.items())
        name = user_data[0][1]
        age = user_data[1][1]
        if age_verific <= age:
            print('name : ', name)
            print('age : ', age)


def name_citizenship(users_pull=None):
    """Get a list of dictionaries with user data.
    Displays Name and Citizenship to the console"""
    if users_pull is None:
        users_pull = users
    name_citiz = {}
    for user_data in users_pull:
        name_citiz[user_data['name']] = user_data['citizenship']
    print(name_citiz)


def status_users(users_pull=None):
    """Get a list of dictionaries with user data.
    adds status to user:
     suspicious
     not_suspicious,"""
    if users_pull is None:
        users_pull = users
    for user_data in users_pull:
        print(user_data)
        if (18 > int(user_data['age']) and user_data['is_working'] == True) or\
            (18 <= int(user_data['age']) and user_data['is_working'] == False):
            user_data['status'] = 'suspicious'
        else:
            user_data['status'] = 'not_suspicious'
    return users


status_users()
print(users)
