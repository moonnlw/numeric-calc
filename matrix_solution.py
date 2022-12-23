import math

EPSILON = 0.5e-4

matrix = [
    [0.2, 1.21, -0.2, 1.41],
    [-0.1, -0.1, 1.15, 1.9],
    [-0.5, -0.3, 0.17, -1.43]
]


def diagonal_dominance(matr):
    new_matrix = [[]] * 3
    max_elems = []
    for i in range(3):
        row_a = matr[i][:-1]
        max_elem = [0] * 3
        for j in range(3):
            val = row_a[j]
            if abs(val) >= abs(max_elem[0]):
                max_elem = [val, j]
        max_elem.append(i)
        max_elems.append(max_elem)
    for elem in max_elems:
        i = elem[1]
        j = elem[2]
        new_matrix[i] = matr[j]
    return new_matrix


def prep(matr):
    new_matr = diagonal_dominance(matr)

    for i in range(3):
        diag = new_matr[i][i]
        new_row = [math.inf] * 4

        for j in range(4):
            elem = new_matr[i][j]
            if j == 3:
                new_row[j] = (elem / diag)
            else:
                if elem != diag:
                    new_row[j] = - (elem / diag)
        new_matr[i] = new_row

    return new_matr


def check(xn, xnm1, eps):
    for i in range(len(xn)):
        if abs(xn[i] - xnm1[i]) > eps:
            return False
        return True


def to_triangle_view(matr):
    n_matr = matr.copy()

    for i in range(2):
        for k in range(i + 1, 3):
            d = - n_matr[k][i] / n_matr[i][i]
            for j in range(4):
                n_matr[k][j] += n_matr[i][j] * d

    return n_matr


def jacoby_method(matr):
    eq = prep(matr)

    x = []
    for row in eq:
        x.append(row[-1])
    counter = 0

    while True:
        x_next = [0, 0, 0]

        for i in range(3):
            for j in range(4):
                if j == 3:
                    x_next[i] = x_next[i] + eq[i][j]
                else:
                    if eq[i][j] != math.inf:
                        x_next[i] = x_next[i] + eq[i][j] * x[j]
        counter += 1

        if check(x, x_next, EPSILON):
            break
        x = x_next.copy()

    return x, counter


def seidel_method(matr):
    eq = prep(matr)

    x = []
    for row in eq:
        x.append(row[-1])

    x_updated = x.copy()
    counter = 0

    while True:
        x_next = [0, 0, 0]

        for i in range(3):
            for j in range(4):
                if j == 3:
                    x_next[i] = x_next[i] + eq[i][j]
                else:
                    if eq[i][j] != math.inf:
                        x_next[i] = x_next[i] + eq[i][j] * x_updated[j]

            x_updated[i] = x_next[i]

        counter += 1

        if check(x, x_next, EPSILON):
            break

        x = x_next.copy()

    return x, counter


def gauss_method(matr):
    new_matr = to_triangle_view(matr)

    for i in reversed(range(3)):
        n, j = (0, 2)
        while j > i:
            n = n + new_matr[j][3] * new_matr[i][j]
            j -= 1

        new_matr[i][3] = (new_matr[i][3] - n) / new_matr[i][i]

    result = []
    for i in range(3):
        result.append(new_matr[i][3])
    return result


if __name__ == '__main__':
    jacoby = jacoby_method(matrix)
    seidel = seidel_method(matrix)
    gauss = gauss_method(matrix)
    print(f"Метод Якоби: {jacoby[0]}, итераций: {jacoby[1]}")
    print(f"Метод Гауса-Зейделя: {seidel[0]}, итераций: {seidel[1]}")
    print(f"Метод Гауса: {gauss[0]}")

