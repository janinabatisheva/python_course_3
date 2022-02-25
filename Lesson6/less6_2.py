# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, depth=1):
        mass = round(self._length * self._width * 25 * depth / 1000)
        return mass


while True:
    try:
        ln = int(input('Введите длину дороги в метрах: '))
        wd = int(input('Введите ширину дороги в метрах: '))
        break
    except ValueError:
        continue

r = Road(ln, wd)
print(f'Масса асфальта: {r.asphalt_mass()} т')
