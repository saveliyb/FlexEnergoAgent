from random import uniform

import matplotlib.pyplot as plt

from random_consumption import get_graph_value as consumption_get_graph_value
from random_gen_wind import get_graph_value as wind_get_graph_value
from random_gen_sun import get_graph_value as sun_get_graph_value


class generator:
    def __init__(self, agent_id: str = "", save_flag: bool = True):
        self.agent_id = agent_id
        self.x, self.y_cons, self.y_wind, self.y_sun, self.y_disel, self.deals = list(), list(), list(), \
                                                                                    list(), list(), list()
        self.all_cut = 51
        self.time_now = 0
        self.save_flag = save_flag

    def generate(self, name: str = None):
        if not self.y_cons:
            self.y_cons.append(self.generate_consumention(self.time_now))
            self.y_wind.append(self.generate_wind())
            self.y_sun.append(self.generate_sun(self.time_now))
            self.y_disel.append(self.generate_disel_zero())
            self.deals.append(self.generate_deals_zero())

        elif len(self.y_cons) >= self.all_cut:
            self.y_cons.pop(0)
            self.y_wind.pop(0)
            self.y_sun.pop(0)
            self.y_disel.pop(0)
            self.deals.pop(0)
            self.y_cons.append(self.generate_consumention(self.time_now, self.y_cons[-1]))
            self.y_wind.append(self.generate_wind())
            self.y_sun.append(self.generate_sun(self.time_now, self.y_sun[-1]))
            self.y_disel.append(self.generate_disel_zero())
            self.deals.append(self.generate_deals_zero())
        else:
            self.y_cons.append(self.generate_consumention(self.time_now, self.y_cons[-1]))
            self.y_wind.append(self.generate_wind())
            self.y_sun.append(self.generate_sun(self.time_now, self.y_sun[-1]))
            self.y_disel.append(self.generate_disel_zero())
            self.deals.append(self.generate_deals_zero())

        self.time_now = (self.time_now + 1) % self.all_cut
        self.show(name)
        return

    def generate_consumention(self, time_now, previous_y=None):
        y_cons = consumption_get_graph_value(self.all_cut, time_now, previous_y)[1]
        return y_cons

    def generate_wind(self):
        y_wind = wind_get_graph_value()[1]
        return y_wind

    def generate_sun(self, time_now, previous_y=None):
        y_sun = sun_get_graph_value(self.all_cut, time_now, previous_y)[1]
        return y_sun

    def generate_disel(self, name: str = None):
        y_disel = abs(self.y_sun[-1] + self.y_wind[-1] + self.deals[-1] - self.y_cons[-1]) \
            if (self.y_sun[-1] + self.y_wind[-1] + self.deals[-1] - self.y_cons[-1]) < 0 else 0
        if not self.y_disel:
            self.y_disel.append(y_disel)
        else:
            self.y_disel.pop()
            self.y_disel.append(y_disel)
        self.generate_disel()
        if name:
            self.show(name)
        return y_disel

    def generate_disel_zero(self):
        return 0

    def generate_deals(self, deal, name: str = None):
        if not self.deals:
            self.deals.append(deal)
        else:
            self.deals.pop()
            self.deals.append(deal)
        self.show(name)
        return deal

    def generate_deals_zero(self):
        return 0

    def get_result_now(self):
        return self.y_wind[-1] + self.y_sun[-1] - self.y_cons[-1]

    def show(self, name: str):
        x = [i for i in range(len(self.y_sun))]
        y_result = [sum((self.y_wind[i], self.y_sun[i], self.deals[i], -self.y_cons[i]))
                    for i in range(len(self.y_sun))]
        plt.plot(x, self.y_cons, '-r', alpha=0.7, label="потребление", lw=2)
        plt.plot(x, self.y_disel, '-g', alpha=0.7, label="дизель", lw=3)
        plt.plot(x, self.y_wind, '-b', alpha=0.7, label="ветер", lw=3)
        plt.plot(x, self.y_sun, '-y', alpha=0.7, label="солнце", lw=3)
        plt.plot(x, y_result, "-k", label="итог", lw=5)
        plt.xlabel("time\nкаждые 28,8 минуты", fontsize=14, fontweight="bold")
        plt.ylabel("КВ*ч\n", fontsize=14, fontweight="bold")
        plt.xticks([i for i in range(51)])
        plt.yticks([i for i in range(int(min(y_result)) - 1, 15)])
        plt.grid(color="k", linestyle='-', linewidth=1)
        plt.legend(loc='upper left')
        if self.save_flag:
            if name:
                plt.savefig(f"{name}_{self.agent_id}.png")
            else:
                plt.savefig(f"example_agent_{self.agent_id}.png")
            plt.close()

        # print(len(self.y_cons))


if __name__ == '__main__':
    a = generator("01")
    for i in range(100):
        a.generate(name=f"images/example_agent_{i}")
        how_buy = uniform(0, 5)
        print(f"{i+1}\nhow buy: {how_buy}")
        a.generate_deals(uniform(0, 5),name=f"images/example_agent_{i}")
        a.generate_disel(name=f"images/example_agent_{i}")

        # input()
