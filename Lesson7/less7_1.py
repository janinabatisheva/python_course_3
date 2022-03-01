# Сложение матриц по правилам линейной алгебры

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        li = [' '.join(line) for line in self.matrix_list]
        return '\n'.join(li)

    def __add__(self, other):
        ml1 = self.matrix_list[:]
        ml2 = other.matrix_list[:]
        try:
            for i in range(max(len(ml1), len(ml2))):
                for j in range(max(len(ml1[i]), len(ml2[i]))):
                    ml1[i][j] = str(int(ml1[i][j]) + int(ml2[i][j]))
            return Matrix(ml1)
        except IndexError:
            print('Ошибка! Суммировать можно только матрицы с однинаковым числом строк и числом столбцов.')


m1 = Matrix([['1', '2', '3'], ['3', '4', '5']])
m2 = Matrix([['1', '1', '1'], ['1', '1', '1']])

print('Первое слагаемое:')
print(m1)

print('Второе слагаемое:')
print(m2)

print('Сумма:')
print(m1 + m2)
