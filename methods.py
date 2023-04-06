import numpy as np


def compute_rectangles_right(func, left, right, n):
    dots = np.linspace(left, right, n)

    sum_of_areas = 0

    for i in range(n - 1):
        sum_of_areas += func.calculate(dots[i]) * (right - left) / n

    return sum_of_areas


def rectangles_right(func, left, right, eps):
    n1 = 4
    n2 = 8

    i1 = compute_rectangles_right(func, left, right, n1)
    i2 = compute_rectangles_right(func, left, right, n2)

    while abs(i2 - i1) > eps:
        n1 *= 2
        n2 *= 2
        i1 = compute_rectangles_right(func, left, right, n1)
        i2 = compute_rectangles_right(func, left, right, n2)

    print(
        f"Значение интеграла: {round(i2, len(str(eps)) - 1)}\n"
        f"Погрешность измерения: {round(abs(i2 - i1), len(str(eps)))}\n"
        f"Число разбиений: {n2}"
    )


def compute_rectangles_left(func, left, right, n):
    dots = np.linspace(left, right, n)

    sum_of_areas = 0

    for i in range(1, n):
        sum_of_areas += func.calculate(dots[i]) * (right - left) / n

    return sum_of_areas


def rectangles_left(func, left, right, eps):
    n1 = 4
    n2 = 8

    i1 = compute_rectangles_left(func, left, right, n1)
    i2 = compute_rectangles_left(func, left, right, n2)

    while abs(i2 - i1) > eps:
        n1 *= 2
        n2 *= 2
        i1 = compute_rectangles_left(func, left, right, n1)
        i2 = compute_rectangles_left(func, left, right, n2)

    print(
        f"Значение интеграла: {round(i2, len(str(eps)) - 1)}\n"
        f"Погрешность измерения: {round(abs(i2 - i1), len(str(eps)))}\n"
        f"Число разбиений: {n2}"
    )


def compute_rectangles_center(func, left, right, n):
    dots = np.linspace(left, right, n)

    sum_of_areas = 0

    i_prev = 0

    for i in range(1, n):
        sum_of_areas += func.calculate((dots[i] + dots[i_prev]) / 2) * (right - left) / n

        i_prev = i

    return sum_of_areas


def rectangles_center(func, left, right, eps):
    n1 = 4
    n2 = 8

    i1 = compute_rectangles_center(func, left, right, n1)
    i2 = compute_rectangles_center(func, left, right, n2)

    while abs(i2 - i1) > eps:
        n1 *= 2
        n2 *= 2
        i1 = compute_rectangles_center(func, left, right, n1)
        i2 = compute_rectangles_center(func, left, right, n2)

    print(
        f"Значение интеграла: {round(i2, len(str(eps)) - 1)}\n"
        f"Погрешность измерения: {round(abs(i2 - i1), len(str(eps)))}\n"
        f"Число разбиений: {n2}"
    )


def compute_trapezoid(func, left, right, n):
    dots = np.linspace(left, right, n)

    sum_of_areas = 0

    i_prev = 0

    for i in range(1, n):
        sum_of_areas += ((func.calculate(dots[i]) + func.calculate(dots[i_prev])) / 2) * (right - left) / n

        i_prev = i

    return sum_of_areas


def trapezoid(func, left, right, eps):
    n1 = 4
    n2 = 8

    i1 = compute_trapezoid(func, left, right, n1)
    i2 = compute_trapezoid(func, left, right, n2)

    while abs(i2 - i1) > eps:
        n1 *= 2
        n2 *= 2
        i1 = compute_trapezoid(func, left, right, n1)
        i2 = compute_trapezoid(func, left, right, n2)

    print(
        f"Значение интеграла: {round(i2, len(str(eps)) - 1)}\n"
        f"Погрешность измерения: {round(abs(i2 - i1), len(str(eps)))}\n"
        f"Число разбиений: {n2}"
    )


def compute_simpson(func, left, right, n):
    dots = np.linspace(left, right, n)

    h = (right - left) / n

    sum_of_y = func.calculate(dots[0]) + func.calculate(dots[n - 1])

    for i in range(1, n - 1):
        sum_of_y += 4 * func.calculate(dots[i]) if i % 2 == 1 else 2 * func.calculate(dots[i])

    return sum_of_y * h / 3


def simpson(func, left, right, eps):
    n1 = 4
    n2 = 8

    i1 = compute_simpson(func, left, right, n1)
    i2 = compute_simpson(func, left, right, n2)

    while abs(i2 - i1) > eps:
        n1 *= 2
        n2 *= 2
        i1 = compute_simpson(func, left, right, n1)
        i2 = compute_simpson(func, left, right, n2)

    print(
        f"Значение интеграла: {round(i2, len(str(eps)) - 1)}\n"
        f"Погрешность измерения: {round(abs(i2 - i1), len(str(eps)))}\n"
        f"Число разбиений: {n2}"
    )
