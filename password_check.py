min_password_length = 4


def main():
    password = get_password(min_password_length)
    print_stars(password)


def get_password(min_length):
    password = input(f"Enter password of at least {min_length} characters: ")
    while len(password) < min_length:
        print("Password is too short")
        password = input(f"Enter password of at least {min_length} characters: ")
    return password


def print_stars(valid):

    print('*' * len(valid))


main()
