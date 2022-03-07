class NotNumErr(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f"Error: {self.param} is not a number!"


class StopException(Exception):
    def __str__(self):
        return "Stop Exception"


class NumList():
    def __init__(self):
        self.list = []

    def add_num(self, num):
        if self.isfloat(num):
            self.list.append(float(num))
        elif num == 'stop':
            raise StopException
        else:
            raise NotNumErr(num)

    @staticmethod
    def isfloat(num):
        try:
            _ = float(num)
            return True
        except ValueError:
            return False


n = NumList()
while True:
    print('Enter one or more numbers in the space')
    n_str = input('To finish type "stop": ')
    n_list = n_str.split()
    flag = False
    for el in n_list:
        try:
            result = n.add_num(el)
        except StopException:
            flag = True
        except NotNumErr as err:
            print(err)
    if flag:
        break

print(f'The result is {n.list}')
