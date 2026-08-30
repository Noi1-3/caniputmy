class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        r = (self.real * other.real + self.imag * other.imag) / denominator
        i = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(r, i)

num1 = Complex(2, 3)
num2 = Complex(1, 4)
res_add = num1 + num2
res_mul = num1 * num2
print("сложение:", res_add.real, "+", res_add.imag, "i")
print("умножение:", res_mul.real, "+", res_mul.imag, "i")