from random import uniform

def get_graph_values(n: int) -> tuple:
    wind_const = 1
    x = [0]
    y = [1 + uniform(0.001, 0.01)]

    for _ in range((n-1)//2):
        x.append(x[-1] + 1)
        x.append(x[-1] + 1)
        num = uniform(-wind_const, wind_const)
        y.append((y[0] + num)/2)
        y.append(y[0] + num)

    for _ in range(n - 1 - (n - 1) // 2 * 2):
        x.append(x[-1] + 1)
        y.append(y[0] + uniform(-wind_const/2, wind_const/2))

    return x, y


def get_graph_value():
    wind_const = 1
    x = [0]
    y = wind_const + uniform(-wind_const, wind_const/2)
    return x, y


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # x, y = get_graph_values(51)
    # print(x, y, sep="\n")
    x = [i for i in range(51)]
    y = list()
    # y.append(y_zero())
    print(len(x))
    for i in range(51):
        y.append(get_graph_value()[1])
    plt.plot(x, y, '*-b', label="second", mec='r', lw=2, mew=2, ms=12)
    plt.show()