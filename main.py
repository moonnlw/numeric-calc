import math

# обозначения:
# x_n - следующее значение
# x_p - предыдущее
# x - текущее

EPSILON = 0.5 * 10e-5


def f(x):
    return math.sin(x) - 4 * x + 0.5


def df(x):
    return math.cos(x) - 4


def d2f(x):
    return -math.sin(x)


def phi(x):
    return (math.sin(x) + 0.5) / 4


def dphi(x):
    return math.cos(x) / 4


def select_point(a, b):
    if f(a) * d2f(a) > 0:
        return a
    elif f(b) * d2f(b) > 0:
        return b
    else:
        raise Exception("Something went wrong")


def dihotomia_method(a, b):
    counter = 0

    while abs(b - a) > EPSILON:
        counter += 1
        c = (a + b) / 2

        if f(b) * f(c) < 0:
            a = c
        else:
            b = c
    res = (a + b) / 2
    print(f"dihotomia: x = {res}, iterations: {counter}")


def newtone_method(a, b):
    counter = 0

    x = select_point(a, b)
    x_n = a if x == b else b

    while abs(x - x_n) > EPSILON:
        counter += 1

        x = x_n
        x_n = x - f(x) / df(x)

    print(f"newtone: x = {x_n}. iterations: {counter}")


def newtone_method_mod(a, b):
    counter = 0

    x = select_point(a, b)

    deriv_x0 = df(x)  # фиксируем производную
    x_n = a if x == b else b

    while abs(x - x_n) > EPSILON:
        counter += 1

        x = x_n
        x_n = x - f(x) / deriv_x0

    print(f"newtone_mod: x = {x_n}. iterations: {counter}")


def chord_method(a, b):
    counter = 0

    x0 = select_point(a, b)  # фиксируем x0
    fx0 = f(x0)  # фиксируем значение функции в x0

    x = x0
    x_n = a if x == b else b

    while abs(x - x_n) > EPSILON:
        counter += 1

        x = x_n
        x_n = x - (f(x) * (x - x0)) / (f(x) - fx0)

    print(f"chord: x = {x_n}. iterations: {counter}")


def movable_chord_method(a, b):
    counter = 0

    x = select_point(a, b)
    x_n = a if x == b else b

    while abs(x - x_n) > EPSILON:
        counter += 1

        x_p = x
        x = x_n
        x_n = x - (f(x) * (x - x_p)) / (f(x) - f(x_p))

    print(f"movable_chord: x = {x_n}. iterations: {counter}")


def simple_iter_method(a, b):
    counter = 0

    x = a
    x_n = phi(a)

    while abs(x - x_n) > EPSILON:
        counter += 1

        x = x_n
        x_n = phi(x_n)

    print(f"simple iteration: x = {x_n}, iterations: {counter}")


def start(a, b):
    dihotomia_method(a, b)
    newtone_method(a, b)
    newtone_method_mod(a, b)
    chord_method(a, b)
    movable_chord_method(a, b)
    simple_iter_method(a, b)


if __name__ == '__main__':
    start(-1/8, 3/8)
