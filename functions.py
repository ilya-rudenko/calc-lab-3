class Equation:
    def __init__(self, string_view, calculate):
        self.string_view = string_view
        self.calculate = calculate


f_1 = Equation(
    "2*x^3 - 3*x^2 + 5*x - 9",
    lambda x: 2 * x * x * x - 3 * x * x + 5 * x - 9
)

f_2 = Equation(
    "3*x^3 + 5*x^2 + 3*x - 6",
    lambda x: 3 * x * x * x + 5 * x * x + 3 * x - 6
)

f_3 = Equation(
    "3*x^3 - 4*x^2 + 7*x - 17",
    lambda x: 3 * x * x * x - 4 * x * x + 7 * x - 17
)

f_4 = Equation(
    "- x^3 - 2*x^2 + 3*x + 23",
    lambda x: -1 * x * x * x - 2 * x * x + 3 * x + 23
)
