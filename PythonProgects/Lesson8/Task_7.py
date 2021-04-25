class ComplexNumber:
    def __init__(self, a, b):
        """
        Complex Number
        :param a: real number
        :param b: imaginary number
        """
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + other.a * self.b
        return ComplexNumber(a, b)

    def __str__(self):
        return f"{self.a}+{self.b}j"


complex_number_1 = ComplexNumber(3, 2)
complex_number_2 = ComplexNumber(1, 4)
print(f"a + b = {complex_number_2 + complex_number_1}")
print(f"a * b = {complex_number_2 * complex_number_1}")
