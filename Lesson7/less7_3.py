class Cell:
    def __init__(self, boxes):
        self.boxes = boxes

    def __add__(self, other):
        b = self.boxes + other.boxes
        return Cell(b)

    def __sub__(self, other):
        b = self.boxes - other.boxes
        if b > 0:
            return Cell(b)
        else:
            print('Результирующая клетка не существует!')
            return Cell(0)

    def __mul__(self, other):
        b = self.boxes * other.boxes
        return Cell(b)

    def __floordiv__(self, other):
        if other.boxes != 0 and other.boxes <= self.boxes:
            b = self.boxes // other.boxes
            return Cell(b)
        elif other.boxes > self.boxes:
            print('Результирующая клетка не существует!')
            return Cell(0)
        else:
            print('Ошибка! На ноль делить нельзя.')
            return Cell(0)

    def make_order(self, line):
        result = ('*' * line + '\n') * (self.boxes // line) + '*' * ((self.boxes % line))
        return result

c1 = Cell(12)
c2 = Cell(6)

print('Первая клетка:')
print(c1.make_order(5))

print('Вторая клетка:')
print(c2.make_order(5))

c3 = c1 + c2
print('Сумма:')
print(c3.make_order(10))

c3 = c1 - c2
print('Разность:')
print(c3.make_order(5))

c3 = c1 * c2
print('Произведение:')
print(c3.make_order(25))

c3 = c1 // c2
print('Частное:')
print(c3.make_order(5))





