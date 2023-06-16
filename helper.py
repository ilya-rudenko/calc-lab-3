from methods import compute_rectangles_center, compute_trapezoid, compute_simpson
from functions import Equation

# c = [[0, 0, 0, 0, 0, 0, 0] for i in range(7)]
#
# c[0][5] = 19
# c[1][5] = 75
#
# c[2][5] = 50
# c[3][5] = 50
# c[4][5] = 75
# c[5][5] = 19
#
# x = [3, 3.4, 3.8, 4.2, 4.6, 5]
#
def f(x):
    return 2*x**3 -3*x**2+4*x-22
#
# sum = 0
#
# for j in range(1, 6):
#     for i in range(0, 6):
#         sum += c[i][5]*f(x[i])
#
# print(sum*(4/2880))

print(compute_trapezoid(Equation("",f),3,5,10))