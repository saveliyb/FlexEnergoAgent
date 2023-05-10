from sympy.polys.fields import field


class Holy_Grail:
    def __init__(self, pow) -> None:
        # self.y_values, self.x_values = y_values, x_values
        self.pow = pow

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

    def main(self, y_values, x_values, d, x_values1, y_values1, d1):
        from sympy import sqrt, diff, simplify, Symbol
        poly, derivative_mas, derivative_second = [], [], []
        x = Symbol('x')
        for i in range(0, d - 4, 2):
            poly.append(simplify(self.interpolate_lagrange(x, x_values[i:i + 5], y_values[i:i + 5])))
            derivative_mas.append(diff((poly[i // 2] + poly[max(0, i // 2 - 1)]) / 2))
            derivative_second.append(diff(derivative_mas[len(derivative_mas) - 1]))

        mid, delta, _time_ = 0, 0, 0

        poly.append(simplify(self.interpolate_lagrange(x, x_values[d - 5:d], y_values[d - 5:d])))

        a = None
        mass,  mass1, mass2, mass3 = [], [], [], []

        while delta <= d - 1:
            past = delta
            mid = ((poly[min(max((delta // 2), 0), len(poly) - 1)] + poly[
                min(max((delta // 2) - 1, 0), len(poly) - 1)]) / 2).evalf(subs={x: delta})
            delta += min(max(3 / 10, abs(1.5 / sqrt(
                abs((derivative_mas[min((delta // 2), len(derivative_mas) - 1)].evalf(subs={x: delta})))))), 2)
            mid += ((poly[min(max((delta // 2), 0), len(poly) - 1)] + poly[
                min(max((delta // 2) - 1, 0), len(poly) - 1)]) / 2).evalf(subs={x: delta})
            mid /= 2
            npow = mid * (delta - past) * 100 / 1.2
            how = 0

            if (self.pow + npow) >= 100:
                while (self.pow + npow) > 100:
                    self.pow -= 1
                    how += 1
                mass1.append(['Продажа', how, '%', 'От', past, 'До', delta, 'Время', delta - past])
                _time_ += delta - past
                from Market import MarketHolyGrail
                a = MarketHolyGrail(past, delta).main(x_values=x_values1, y_values=y_values1, d=d1)
                mass.append(a)
                mass2.append([mid, delta - past])
            elif (self.pow + npow) < 30:
                while (self.pow + npow) < 30:
                    self.pow += 1
                    how += 1
                mass1.append(['Покупка', how, '%', 'От', past, 'До', delta, 'Время', delta - past])
                _time_ += delta - past
                from Market import MarketHolyGrail
                a = MarketHolyGrail(past, delta).main(x_values=x_values1, y_values=y_values1, d=d1)
                mass.append(a)
                mass2.append([mid, delta - past])
            elif _time_ != 0:
                mass3.append([sqrt(abs(mass[i] / min(mass) * 1.607 * mass2[i][0] * 2.4 * (mass2[i][1]))) / 0.3 for i in
                              range(len(mass))])
                mass2 = []
                mass = []
                _time_ = 0
            self.pow += npow
            if delta > d - 1:
                break
            print(mass1, mass2, mass3, sep="\n\t")
        # mass1.append([mass[i] / min(mass) * 1.607 * mass2[i][0] * (-2.4) * (mass2[i][1]) / 0.3 for i in range(len(mass))])
        return mass1, mass3

