class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Dalyti iš nulio neleidžiama.")
        return a / b

    def power(self, a, b):
        return a ** b

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(3, 5))         # naudojimo pavyzdys
    print(calc.subtract(10, 4))
    print(calc.multiply(2, 3))
    print(calc.divide(8, 2))
    print(calc.power(2, 3))