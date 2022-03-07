# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return (f'{self.re}+{self.im}i')
        elif self.im == 0:
            return (f'{self.re}')
        else:
            return (f'{self.re}{self.im}i')

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return ComplexNum(re, im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNum(re, im)


num1 = ComplexNum(3, 6)
num2 = ComplexNum(2, -3)
print(f'Sum is {num1 + num2}')
print(f'Product is {num1 * num2}')

# n1 = complex(3, 6)
# n2 = complex(2, -3)
# print(n1 + n2)
# print(n1 * n2)

