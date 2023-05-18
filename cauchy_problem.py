import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 1
x0 = 0
y0 = 2


def f(x, y):
    return -8 * x / y


def df(x, y):
    return -8 / y - (64 * x ** 2 / y ** 3)


def d2f(x, y):
    return - 64 * x / y ** 3 - 1536 * x ** 3 / y ** 5


def d3f(x, y):
    return -64 / y ** 3 - 6144 * x ** 2 / y ** 5 - 61440 * x ** 4 / y ** 7


def result(x):
    return np.sqrt(4 - 8 * x ** 2)


def euler_with_recalculation(n):
    h = (b - a) / n
    x, y = x0, y0
    points = []
    for i in range(0, n):
        next_x = x + h
        if next_x <= 0.7:
            next_y = y + h / 2 * (f(x, y) + f(next_x, y + f(x, y) * h))
            points.append((next_x, next_y))
            x = next_x
            y = next_y
    return points


def euler_implicit(n):
    h = (b - a) / n
    x, y = x0, y0
    points = []
    for i in range(0, n):
        next_x = x + h
        sqrt = y ** 2 - 32 * h * next_x
        if sqrt > 0:
            next_y = (y + math.sqrt(sqrt)) / 2
            points.append((next_x, next_y))
            x = next_x
            y = next_y
    return points


def taylor_4th_order(n):
    h = (b - a) / n
    x, y = x0, y0
    points = []
    for i in range(0, n):
        next_x = x + h
        if next_x < 1 / math.sqrt(2):
            next_y = y + h * f(x, y) + h * h * df(x, y) / 2 + math.pow(h, 3) * d2f(x, y) / 6 + math.pow(h, 4) * d3f(x,
                                                                                                                    y) / 24
            points.append((next_x, next_y))
            x = next_x
            y = next_y
    return points


if __name__ == '__main__':
    values_euler = list(zip(*euler_with_recalculation(30)))
    values_euler_implicit = list(zip(*euler_implicit(30)))
    values_taylor = list(zip(*taylor_4th_order(30)))

    plt.grid()
    plt.plot(values_taylor[0], values_taylor[1], '-bo', color='r', label='taylor')
    plt.plot(values_euler[0], values_euler[1], '-bo', color='b', label='euler recalculate')
    plt.plot(values_euler_implicit[0], values_euler_implicit[1], '-bo', color='g', label='euler implicit')

    xp = np.arange(0, 0.7, 0.00001)
    plt.plot(xp, result(xp), color='black', label='exact solution')
    plt.legend()
    plt.show()
