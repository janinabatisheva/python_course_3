# 4. Начните работу над проектом «Склад оргтехники»...

class CapacityErr(Exception):
    def __init__(self, free, need):
        self.free = free
        self.need = need

    def __str__(self):
        return f"No enough space, free space is {self.free}, need {self.need}"


class LackErr(Exception):
    def __init__(self, itms):
        self.itms = itms

    def __str__(self):
        return f"There are only {self.itms['printers']} printers, {self.itms['scanners']} scanners, {self.itms['xeroxes']} xeroxes in the storage!"


class Storage:
    def __init__(self, capacity=100):
        self.max_count = capacity
        self.items = {'printers': 0, 'scanners': 0, 'xeroxes': 0}

    def store(self, items):
        need = sum([items[key] for key in items])
        free = self.max_count - sum([self.items[key] for key in self.items])
        if need > free:
            raise CapacityErr(free, need)

        else:
            self.items = {key: self.items[key] + items[key] for key in self.items}

    def to_use(self, items):
        check = [self.items[key] >= items[key] for key in self.items]
        if False in check:
            raise LackErr(self.items)

        else:
            self.items = {key: self.items[key] - items[key] for key in self.items}

    def show(self):
        print(f"There are {self.items['printers']} printers, "
              f"{self.items['scanners']} scanners, "
              f"{self.items['xeroxes']} xeroxes in the storage, "
              f"occupancy is {sum([self.items[key] for key in self.items])}, "
              f"free space is {self.max_count - sum([self.items[key] for key in self.items])}.")


class OfficeEquipment:
    name = 'device'

    @staticmethod
    def items_dict():
        while True:
            try:
                p = int(input('Input number of printers: '))
                s = int(input('Input number of scanners: '))
                x = int(input('Input number of xeroxes: '))
                break
            except ValueError:
                print('Error: data is incorrect!')
        return {'printers': p, 'scanners': s, 'xeroxes': x}


class Printer(OfficeEquipment):
    name = 'printer'

    def __init__(self, islaser=True):
        self.islaser = islaser


class Scanner(OfficeEquipment):
    name = 'scanner'

    def __init__(self, size='A4'):
        self.size = size


class Xerox(OfficeEquipment):
    name = 'xerox'

    def __init__(self, iscolor=False):
        self.iscolor = iscolor


s = Storage(50)
s.show()

while True:
    try:
        print('Equipment taking to the storage...')
        d = OfficeEquipment.items_dict()
        s.store(d)
        s.show()
        break
    except CapacityErr as err:
        print(err)

while True:
    try:
        print('Transfer of equipment for use...')
        d = OfficeEquipment.items_dict()
        s.to_use(d)
        s.show()
        break
    except LackErr as err:
        print(err)
