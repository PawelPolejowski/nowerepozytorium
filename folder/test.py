
import folder.Utils as utils

wynik = utils.sum_two_numbers(5,6)
print(wynik)

if __name__ == "__main__":
    print('\n')
    print('Jestem w __main__ ex 00')


def arguments_args(*args):
    print(f'Jestem w funkcji {arguments_args.__name__}')
    print('Wypisuje wartosci argumentow:')

    for arg in args:
        print(arg)

if __name__ == "__main__":
    arguments_args(1, 2, 3, 4, 5, 6)