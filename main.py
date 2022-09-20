from reverse_function import reverse_string

if __name__ == '__main__':
    print('\tВведите строку, чтобы "перевернуть" ее:')
    input_string = input()
    reversed_string = reverse_string(input_string)
    if reversed_string == -1:
        print('\tТы ничего не ввел :(')
    elif reversed_string == -2:
        print('\tТы пробелы что ли ввел там?')
    else:
        print(f'\tПеревернутая строка: {reversed_string}')
