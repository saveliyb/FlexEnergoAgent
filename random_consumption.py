from random import uniform
# from typing import List, Union


def night() -> float:
    return uniform(-0.5, 1)


def day_evening() -> float:
    return uniform(-2, 2)


def y_zero() -> float:
    return 0.2 + uniform(0.001, 0.01)


def get_graph_values(n: int) -> tuple:
    day_const_min = 3
    day_const_max = 5
    x = [0]
    y = [0.2 + uniform(0.001, 0.01)]

    for _ in range((n - 3) // 4):
        x.append(x[-1] + 1)
        y.append(min(max(y[-1] + night(), y[0]), day_const_min))

    for _ in range(n - 3 - (n-3) // 4 * 2):
        x.append(x[-1] + 1)
        y.append(max(day_const_max, y[-1] + day_evening()))

    x.append(x[-1] + 1)
    y.append((y[-1] + uniform(y[0], day_const_min)) / 2)

    for _ in range((n - 3) // 4):
        x.append(x[-1] + 1)
        y.append(min(max(y[-1] - night(), y[0]), day_const_min))

    x.append(x[-1] + 1)
    y.append(y[0])

    return x, y


def get_graph_value(all_cut, time, previous_y: float = None):
    day_const_min = 3
    day_const_max = 5
    x = [0]
    if time == 0 or not previous_y:
        y = y_zero()
    elif 0 < time <= ((all_cut - 3) // 4):
        """night"""
        y = min(max(previous_y + night(), y_zero()), day_const_min)
    elif ((all_cut - 3) // 4) < time <= ((all_cut - 3 - (all_cut - 3) // 4 * 2) + ((all_cut - 3) // 4)):
        """morning"""
        y = max(day_const_max, previous_y + day_evening())
    elif time == ((all_cut - 3 - (all_cut - 3) // 4 * 2) + ((all_cut - 3) // 4) + 1):
        """day"""
        y = (previous_y + uniform(0.2 + uniform(0.001, 0.01), day_const_min)) / 2
    elif ((all_cut - 3 - (all_cut - 3) // 4 * 2) + ((all_cut - 3) // 4)) < time <= \
            (((all_cut - 3) // 4) + ((all_cut - 3 - (all_cut - 3) // 4 * 2) + ((all_cut - 3) // 4))):
        """evening"""
        y = min(max(previous_y - night(), y_zero()), day_const_min)
    else:
        y = y_zero()
    return x, y
    # x = [0]
    # y = [0.2 + uniform(0.001, 0.01)]
    #
    # for _ in range((all_cut - 3) // 4):
    #     x.append(x[-1] + 1)
    #     y.append(min(max(y[-1] + night(), y[0]), day_const_min))
    #
    # for _ in range(all_cut - 3 - (all_cut - 3) // 4 * 2):
    #     x.append(x[-1] + 1)
    #     y.append(max(day_const_max, y[-1] + day_evening()))
    #
    # x.append(x[-1] + 1)
    # y.append((y[-1] + uniform(y[0], day_const_min)) / 2)
    #
    # for _ in range((all_cut - 3) // 4):
    #     x.append(x[-1] + 1)
    #     y.append(min(max(y[-1] - night(), y[0]), day_const_min))
    #
    # x.append(x[-1] + 1)
    # y.append(y[0])

    # return x, y


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # x, y = get_graph_values(51)
    x = [i for i in range(51)]
    y = list()
    y.append(y_zero())
    for i in range(1, 51):
        y.append(get_graph_value(51, i, y[-1])[1])
    plt.plot(x, y, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
    plt.show()