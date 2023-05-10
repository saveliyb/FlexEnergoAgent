from pprint import pprint

from sympy.polys.fields import field

# график цен (формирование)


class MarketHolyGrail:
    def __init__(self, past, delta) -> None:
        self.past, self.delta = past, delta

    def interpolate_lagrange(self, x, x_values, y_values):
        def _basis(j):
            from operator import mul
            from functools import reduce
            p = [(x - x_values[m]) / (x_values[j] - x_values[m]) for m in range(k) if m != j]
            return reduce(mul, p)

        assert len(x_values) != 0 and (
                    len(x_values) == len(y_values))  # x and y cannot be empty and must have the same length
        k = len(x_values)
        return sum(_basis(j) * y_values[j] for j in range(k))

    def main(self, x_values, y_values, d):
        # import numpy as np
        # from random import uniform
        from sympy import sqrt, diff, simplify, Symbol
        poly, derivative_mas, derivative_second = [], [], []
        # derivative_mas = []
        # derivative_second = []
        x = Symbol('x')
        # d = 51
        # y_values = np.array([uniform(0, 7) for i in range(d)], dtype=float)
        # x_values = np.array([i for i in range(d)], dtype=float)

        for i in range(0, d - 4, 2):
            poly.append(simplify(self.interpolate_lagrange(x, x_values[i:i + 5], y_values[i:i + 5])))
            derivative_mas.append(diff((poly[i // 2] + poly[max(0, i // 2 - 1)]) / 2))
            derivative_second.append(diff(derivative_mas[len(derivative_mas) - 1]))

        # mid, delta = 0, 0
        # delta = 0
        poly.append(simplify(self.interpolate_lagrange(x, x_values[d - 5:d], y_values[d - 5:d])))
        # print("poly:")
        # print(poly)
        a = ((poly[min(max((self.past // 2), 0), len(poly) - 1)] + poly[
            min(max((self.past // 2) - 1, 0), len(poly) - 1)]) / 2).evalf(subs={x: self.past})
        a += ((poly[min(max((self.delta // 2), 0), len(poly) - 1)] + poly[
            min(max((self.delta // 2) - 1, 0), len(poly) - 1)]) / 2).evalf(subs={x: self.delta})
        a /= 2
        print(a)
        return a

# возвращает среднее между двумя точками