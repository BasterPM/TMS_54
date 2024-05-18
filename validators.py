def check_users_email_password(user_email, user_password, users_data):
    if '@' in user_email:
        for i in users_data:
            if i.get('email') == user_email and i.get('password') == user_password:
                return user_email
            else:
                print('The email or password was entered incorrectly. Try again!')
                return False
    else:
        print('email entered incorrectly')
        return False
