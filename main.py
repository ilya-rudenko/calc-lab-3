from utils import ask, print_error, draw_plot
from functions import f_1, f_2, f_3, f_4
from methods import rectangles_left, rectangles_right, rectangles_center, trapezoid, simpson

func_answ = ask(
    "Выберите уравнение:\n"
    "   1. " + f_1.string_view + "\n"
                                 "   2. " + f_2.string_view + "\n"
                                                              "   3. " + f_3.string_view + "\n"
                                                                                           "   4. " + f_4.string_view,
    answers=["1", "2", "3", "4"]
)

if func_answ == "1":
    func = f_1
elif func_answ == "2":
    func = f_2
elif func_answ == "3":
    func = f_3
else:
    func = f_4

left = ask("Введите левую границу интегрирования: ", is_numeric=True)
right = ask("Введите правую границу интегрирования: ", is_numeric=True)

while left >= right:
    print_error("Левая граница должна быть меньше правой границы!")

    left = ask("Введите левую границу интегрирования: ", is_numeric=True)
    right = ask("Введите правую границу интегрирования: ", is_numeric=True)

draw_plot(func, left, right)

print(func.string_view)

method_answ = ask(
    "Каким методом хотите решать уравнение:\n"
    "   1. Метод прямоугольников (левые) \n"
    "   2. Метод прямоугольников (средние) \n"
    "   3. Метод прямоугольников (правые) \n"
    "   4. Метод трапеций \n"
    "   5. Метод Симпсона",
    answers=["1", "2", "3", "4", "5"]
)

print(method_answ)

eps = ask("Введите точность: ", is_numeric=True, is_positive=True)
while eps <= 0:
    print_error("Точность должна быть строго больше нуля!")

    n = ask("Введите количество точек в разбиение (n): ", is_numeric=True, is_positive=True)

if method_answ == "1":
    print("Левые прямоугольники")
    rectangles_left(func, left, right, eps)
elif method_answ == "2":
    print("Центральные прямоугольники")
    rectangles_center(func, left, right, eps)
elif method_answ == "3":
    print("Правые прямоугольники")
    rectangles_right(func, left, right, eps)
elif method_answ == "4":
    print("Трапеция")
    trapezoid(func, left, right, eps)
else:
    print("Симпсон")
    simpson(func, left, right, eps)
