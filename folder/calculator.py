# zadanie
# napisz klase Calculator
# 2 atrybuty ( okreslane przy inicjacji) a i b
# 4 metody do obliczen - (ktore zwracaja wynik odpowiednio mnozenia, dzielenia, dodawania i odejmowania)

from Utils import Calculator

while True:
    dzialanie = input('Jakie dzialnie wykonac?')

    if dzialanie == 'liczba':
        print(f'Liczba wszystkich dzialan: {Calculator.total_number_of_calculations}')
        print(f'Liczba wszystkich dodawan: {Calculator.total_number_of_dodawanie}')
        print(f'Liczba wszystkich odejmowan: {Calculator.total_number_of_odejmowanie}')
        print(f'Liczba wszystkich mnozenie: {Calculator.total_number_of_mnozenie}')
        print(f'Liczba wszystkich dzielenie: {Calculator.total_number_of_dzielenie}')
        continue

    a = float(input('a:'))
    b = float(input('b:'))
    calc = Calculator(a, b)

    if dzialanie == 'dodawanie':
        print(calc.dodawanie())
    elif dzialanie == 'odejmowanie':
        kalkulacja = Calculator(a, b)
        print(calc.odejmowanie())
    elif dzialanie == 'mnozenie':
        print(calc.mnozenie())
    elif dzialanie == 'dzielenie':
        print(calc.dzielenie())
    else:
        print('Nieznane dzialenie')






