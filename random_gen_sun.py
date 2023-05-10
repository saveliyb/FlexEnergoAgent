from random import uniform
# from typing import List, Union


def night():
    return 0


def day_evening():
    return uniform(-0.2, 1)


def y_zero():
    return 0


def get_graph_values(n: int) -> tuple:
    x = [0]
    y = [0]
    sun_const = 0.3 + uniform(0.001, 0.01)

    for _ in range((n - 3) // 6):
        x.append(x[-1] + 1)
        y.append(night())

    for _ in range((n - 3 - (n-3) // 6 * 2) // 2):
        x.append(x[-1] + 1)
        y.append(max(sun_const, y[-1] + day_evening()))

    for _ in range((n - 3 - (n-3) // 6 * 2) // 2):
        x.append(x[-1] + 1)
        y.append(max(sun_const, y[-1] - day_evening()))

    x.append(x[-1] + 1)
    y.append(y[-1] / 2)

    for _ in range((n - 3) // 6):
        x.append(x[-1] + 1)
        y.append(night())

    x.append(x[-1] + 1)
    y.append(y[0])

    return x, y


def get_graph_value(all_cut, time, previous_y: float = None):
    x = [0]
    if 0 <= time <= ((all_cut - 3) // 6) or previous_y == None:
        """night"""
        y = night()
    elif ((all_cut - 3) // 6) < time <= ((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6):
        """morning"""
        y = max(y_zero(), previous_y + day_evening())
    elif ((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6) < time <= \
            (((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6) +
             (all_cut - 3 - (all_cut-3) // 6 * 2) // 2):
        """evening"""
        y = max(y_zero(), previous_y - day_evening())
    elif time == (((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6) +
             (all_cut - 3 - (all_cut-3) // 6 * 2) // 2 + 1):
        """day"""
        y = previous_y / 2
    elif (((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6) +
             (all_cut - 3 - (all_cut-3) // 6 * 2) // 2 + 1) < time <= (((all_cut - 3 - (all_cut-3) // 6 * 2) // 2) + ((all_cut - 3) // 6) +
             (all_cut - 3 - (all_cut-3) // 6 * 2) // 2 + 1 + (all_cut - 3) // 6):
        y = night()
    else:
        y = y_zero()
    # print(y)
    return x, y


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # x, y = get_graph_values(51)
    # print(len(x))
    # print(x, y, sep="\n")
    x = [i for i in range(51)]
    y = list()
    y.append(y_zero())
    for i in range(1, 51):
        y.append(get_graph_value(51, i, y[-1])[1])
    plt.plot(x, y, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
    plt.show()