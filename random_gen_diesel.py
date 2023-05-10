from random import uniform

def get_graph_values(n: int) -> tuple:
    disel_const = 1
    x = [0]
    y = [disel_const + uniform(0.001, 0.01)]

    for _ in range(n-1):
        x.append(x[-1] + 1)
        y.append(y[0] + uniform(-0.1, 0.1))

    return x, y


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    x, y = get_graph_values(51)
    print(len(x))
    # print(x, y, sep="\n")
    plt.plot(x, y, '*-b', label="second", mec='r', lw=2, mew=2, ms=12)
    plt.show()