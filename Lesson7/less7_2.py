from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, m):
        self.__model = m

    @abstractmethod
    def cloth_consumption(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if str(new_model).isdigit() and new_model > 0:
            self.__model = new_model
        else:
            print('Error!')


class Topcoat(Clothes):
    def cloth_consumption(self, v):
        return round(v / 6.5 + 0.5, 2)


class Suit(Clothes):
    def cloth_consumption(self, h):
        return round(2 * h + 0.3, 2)


t = Topcoat(1)
print(f'The topcoat model is {t.model}')
print(f'Cloth consumption per topcoat is {t.cloth_consumption(30)}')

s = Suit(2)
print(f'The suit model is {s.model}')
s.model = 3
print(f'The suit model is {s.model}')
print(f'Cloth consumption per suit is {s.cloth_consumption(1.81)}')
