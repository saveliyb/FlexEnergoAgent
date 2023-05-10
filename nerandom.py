import matplotlib.pyplot as plt

from random_consumption import get_graph_values as consumption_get_graph_values
from random_gen_diesel import get_graph_values as disel_get_graph_values
from random_gen_wind import get_graph_values as wind_get_graph_values
from random_gen_sun import get_graph_values as sun_get_graph_values


def get_values(agent_id: str = "") -> tuple:
    d = 51
    x, y_cons = consumption_get_graph_values(d)
    x, y_disel = disel_get_graph_values(d)
    x, y_wind = wind_get_graph_values(d)
    x, y_sun = sun_get_graph_values(d)

    y_result = [sum((y_disel[i], y_wind[i], y_sun[i], -y_cons[i])) for i in range(d)]

    plt.plot(x, y_cons, '-r', alpha=0.7, label="потребление", lw=2)
    plt.plot(x, y_disel, '-g', alpha=0.7, label="дизель", lw=3)
    plt.plot(x, y_wind, '-b', alpha=0.7, label="ветер", lw=3)
    plt.plot(x, y_sun, '-y', alpha=0.7, label="солнце", lw=3)
    plt.plot(x, y_result, "-k", label="итог", lw=5)
    plt.xlabel("time\nкаждые 28,8 минуты", fontsize=14, fontweight="bold")
    plt.ylabel("КВ*ч\n", fontsize=14, fontweight="bold")
    plt.xticks([i for i in range(51)])
    plt.yticks([i for i in range(int(min(y_result)) - 1, 15)])
    # plt.grid = True
    plt.grid(color="k", linestyle='-', linewidth=1)
    plt.legend(loc='upper left')
    plt.savefig(f"foo{agent_id}.png")

    return x, y_result


if __name__ == '__main__':
    d = 51
    x, y_cons = consumption_get_graph_values(d)
    x, y_disel = disel_get_graph_values(d)
    x, y_wind = wind_get_graph_values(d)
    x, y_sun = sun_get_graph_values(d)

    y_result = [sum((y_disel[i], y_wind[i], y_sun[i], -y_cons[i])) for i in range(d)]

    plt.plot(x, y_cons, '-r', alpha=0.7, label="потребление", lw=2)
    plt.plot(x, y_disel, '-g', alpha=0.7, label="дизель", lw=3)
    plt.plot(x, y_wind, '-b', alpha=0.7, label="ветер", lw=3)
    plt.plot(x, y_sun, '-y', alpha=0.7, label="солнце", lw=3)
    plt.plot(x, y_result, "-k", label="итог", lw=5)
    plt.xlabel("time\nкаждые 28,8 минуты", fontsize=14, fontweight="bold")
    plt.ylabel("КВ*ч\n", fontsize=14, fontweight="bold")
    plt.xticks([i for i in range(51)])
    plt.yticks([i for i in range(int(min(y_result)) - 1, 15)])
    # plt.grid = True
    plt.grid(color="k", linestyle='-', linewidth=1)
    plt.legend(loc='upper left')
    plt.show()

