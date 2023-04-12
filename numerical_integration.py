import math
import matrix_solution


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


def gauss_method():
    print("вычисления для метода Гаусса")
    matrix = [
        [1 / 3, 1 / 2, 1, -1 / 4],
        [1 / 4, 1 / 3, 1 / 2, -1 / 5],
        [1 / 5, 1 / 4, 1 / 3, -1 / 6]
    ]
    a0, a1, a2 = matrix_solution.gauss_method(matrix)  # пользуемся методом Гаусса из лабораторной №3))
    print("a0 = {}, a1 = {}, a2 = {}".format(a0, a1, a2))

    x0 = round((1 - math.sqrt(0.6)) / 2, 6)
    x1 = 1 / 2
    x2 = round((1 + math.sqrt(0.6)) / 2, 6)

    matrix2 = [
        [1, 1, 1, 1],
        [x0, x1, x2, 0.5],
        [pow(x0, 2), pow(x1, 2), pow(x2, 2), 1 / 3]
    ]
    a, b, c = matrix_solution.gauss_method(matrix2)
    print("a = {}, b = {}, c = {}".format(a, b, c))

    gauss_result = a * f(x0) + b * f(x1) + c * f(x2)
    print("I = {}".format(gauss_result))


if __name__ == '__main__':
    print("метод средних прямоугольников")
    print("шаг    результат            погрешность по Рунге")
    print("0.1    {:}  {:.18f}".format(middle_rectangles(0.1),
                                       runge_error_middle_rectangles(0.1, 0.1 * 2)))
    print("0.05   {:}  {:.18f}".format(middle_rectangles(0.5),
                                       runge_error_middle_rectangles(0.5, 0.5 * 2)))
    print("0.025  {:}  {:.18f}".format(middle_rectangles(0.025),
                                       runge_error_middle_rectangles(0.025, 0.025 * 2)))

    print("")
    print("метод 3/8")
    print("шаг    результат            погрешность по Рунге")
    print("0.1    {:}  {:.18f}".format(three_eights_method(0.1), runge_error_three_eights_method(0.1, 0.1 * 2)))
    print("0.05   {:}  {:.18f}".format(three_eights_method(0.05), runge_error_three_eights_method(0.05, 0.05 * 2)))
    print("0.025  {:}  {:.18f}".format(three_eights_method(0.025), runge_error_three_eights_method(0.025, 0.025 * 2)))

    print("")
    gauss_method()
