import numpy as np
import matplotlib.pyplot as plt


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def print_error(s):
    print(bcolors.FAIL + s + bcolors.ENDC)


def ask(question, answers=None, is_numeric=False, is_positive=False):
    if answers is None:
        answers = []
    print(question)

    if is_numeric:
        print(">>", end=" ")
        answ = input()

        while (not is_number(answ)) or (is_positive and float(answ) < 0):
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return float(answ)

    else:
        print(">>", end=" ")
        answ = input()

        while answ not in answers:
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return answ


def draw_plot(func, left, right):
    x = np.linspace(left - 2, right + 2, 100)

    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")

    plt.xticks(np.arange(left - 2, right + 2, 1))

    plt.plot(x, func.calculate(x), color="r")

    x_stroke = np.linspace(left, right, 20)

    for i in x_stroke:
        plt.plot(np.ones(2) * i, np.linspace(0, func.calculate(i), 2), color="b")

    plt.show()
