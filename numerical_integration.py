import math


def f(x): return x * math.sin(math.pow(x, 4))


def middle_rectangles(h):
    a, b = 0, 1
    n = int((b - a) / h)

    integral_sum = 0
    for i in range(1, n + 1):
        xi = a + i * h
        integral_sum += f(xi - h / 2)

    return h * integral_sum


def runge_error_middle_rectangles(h, h2):
    return abs(middle_rectangles(h) - middle_rectangles(h2)) / 3


def three_eights_method(h):
    a, b = 0, 1
    n = int((b - a) / h)

    integral_sum = 0
    for i in range(1, n + 1):
        xi = a + i * h
        integral_sum += (f(xi - h) + 3 * f((xi - h + 2 * xi) / 3) + 3 * f((2 * (xi - h) + xi) / 3) + f(xi)) / 8

    return h * integral_sum


def runge_error_three_eights_method(h, h2):
    return abs(middle_rectangles(h) - middle_rectangles(h2)) / 15


if __name__ == '__main__':
    print("метод средних прямоугольников")
    print("шаг    результат            погрешность по Рунге")
    print("0.1    {0}  {1}".format(middle_rectangles(0.1),
                                   runge_error_middle_rectangles(0.1, 0.1 * 2)))
    print("0.05   {0}  {1}".format(middle_rectangles(0.5),
                                   runge_error_middle_rectangles(0.5, 0.5 * 2)))
    print("0.025  {0}  {1}".format(middle_rectangles(0.025),
                                   runge_error_middle_rectangles(0.025, 0.025 * 2)))

    print("")
    print("метод 3/8")
    print("шаг    результат            погрешность по Рунге")
    print("0.1    {0}  {1}".format(three_eights_method(0.1), runge_error_three_eights_method(0.1, 0.1 * 2)))
    print("0.05   {0}  {1}".format(three_eights_method(0.05), runge_error_three_eights_method(0.05, 0.05 * 2)))
    print("0.025  {0}  {1}".format(three_eights_method(0.025), runge_error_three_eights_method(0.025, 0.025 * 2)))