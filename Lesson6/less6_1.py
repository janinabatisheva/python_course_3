# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time
import turtle


class TrafficLight:
    __color = None

    def running(self):
        cycle = [['red', 7], ['yellow', 2], ['green', 5], ['yellow', 2]]
        for phase in cycle:
            self.__color = phase[0]
            turtle.color(phase[0], phase[0])
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            time.sleep(phase[1])

    def stop(self):
        turtle.bye()


while True:
    try:
        num = int(input('Введите количество циклов: '))
        break
    except ValueError:
        continue

tl = TrafficLight()
print('Начало работы светофора')
for _ in range(num):
    tl.running()
tl.stop()
print('Окончание работы светофора')
