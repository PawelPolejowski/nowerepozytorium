class Calculator:
    total_number_of_calculations = 0
    total_number_of_dodawanie = 0
    total_number_of_odejmowanie = 0
    total_number_of_mnozenie = 0
    total_number_of_dzielenie = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mnozenie(self):
        Calculator.total_number_of_calculations += 1
        Calculator.total_number_of_mnozenie += 1
        return self.a * self.b
    def dzielenie(self):
        Calculator.total_number_of_calculations += 1
        Calculator.total_number_of_dzielenie += 1
        return self.a / self.b
    def dodawanie(self):
        Calculator.total_number_of_calculations += 1
        Calculator.total_number_of_dodawanie += 1
        return self.a + self.b
    def odejmowanie(self):
        Calculator.total_number_of_calculations += 1
        Calculator.total_number_of_odejmowanie += 1
        return self.a - self.b