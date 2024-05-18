import getters
from validators import check_users_email_password
import json


def app():
    result = False
    while not result:
        user_mail = getters.get_mail()
        if user_mail == 'exit':
            print('Goodbye')
            quit()
        user_password = getters.get_password()
        with open('users_data.json', 'r') as json_file:
            users_data = json.load(json_file)
        result = check_users_email_password(user_mail, user_password, users_data)


app()
