from reverse_function import reverse_string

if __name__ == '__main__':
    print('\tВведите строку, чтобы "перевернуть" ее:')
    input_string = input()
    reversed_string = reverse_string(input_string)
    if not reversed_string:
        print('\tТы ничего не ввел :(')
    else:
        print(f'\tПеревернутая строка: {reversed_string}')
