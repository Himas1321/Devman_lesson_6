def get_long_or_short_password(password):
    return len(password) >= 12

def get_whether_there_are_numbers_or_not(password):
    return any(letter.isdigit() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password)

def has_lower_letters(password):
    return any(letter.islower() for letter in password)

def has_symbols(password):
    return any(not letter.isalpha() and not letter.isdigit() for letter in
               password)

checks = [
    get_long_or_short_password,
    get_whether_there_are_numbers_or_not,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]

def password_rating(password):
    score = 0
    for check in checks:
        if check(password):
            score += 2
    return (score)

if __name__ == '__main__':
    user_input = input('ведите пароль:')
    print('Рейтинг пароля:', password_rating(user_input))
