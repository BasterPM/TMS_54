from random import randint

def enter_range():
    a = [input('Start of range: '), input('End of range: ')]
    if a[0] == 'exit' or a[1] == 'exit':
        quit()
    if a[0].isnumeric() and a[1].isnumeric() and 30 >= (int(a[1]) - int(a[0])) >= 5:
        return [int(a[0]), int(a[1])]
    else:
        print('Enter only numbers in the correct range')
        return enter_range()

def randoming_nambers(user_range_list):
    random_numbers = []
    while len(random_numbers) != 3:
        random_number = (randint(user_range_list[0], user_range_list[1] + 1))
        if random_number in random_numbers:
            continue
        else:
            random_numbers.append(random_number)
    return random_numbers

def get_number_user(user_range):
    a = [input('First number: '), input('Second number: '), input('Third number: ')]
    if a[0] == 'exit' or a[1] == 'exit' or a[2] == 'exit':
        quit()
    if a[0].isnumeric() and a[1].isnumeric() and a[2].isnumeric():
        if int(a[0]) and int(a[1]) and int(a[2]) in range(user_range[0], user_range[1] + 1):
            return [int(a[0]), int(a[1]), int(a[2])]
        else:
            print('Numbers must be in range')
            return get_number_user(user_range)
    else:
        print('Use numbers only!')
        return get_number_user(user_range)

def match_checking(numbers_random, numbers_user):
    for i in range(3):
        if numbers_user[i] in numbers_random:
            numbers_random.remove(numbers_user[i])

def ygadaika():
    print('Hello!\nEnter 2 numbers, the range of which must include a minimum of 5 and a maximum of 30 numbers.\n'
          'I\'ll guess 3 of them, and you guess!')
    user_range = enter_range()
    numbers_random = randoming_nambers(user_range)
    while len(numbers_random) != 0:
        numbers_user = get_number_user(user_range)
        match_checking(numbers_random, numbers_user)
    print('You Won!')

ygadaika()

