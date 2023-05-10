from random import uniform

from nerandom1 import generator
import asyncio
import aiohttp
from classes import Bet


class Agent:
    def __init__(self, agent_id: str, name: str = ""):
        self.agent_id = agent_id
        self.url = "http://127.0.0.1:8000"
        self.d_itme = 20
        self.generator = generator(agent_id, True)
        self.name = name

    def generation(self, name: str):
        self.generator.generate(name=name)

    def get_total_energy(self):
        return self.generator.get_result_now()

    def set_disel_energy_buy(self, name: str = ""):
        """energy - сколько купили на аукционе"""
        self.generator.generate_disel(name=name)

    async def get_deals_and_remake_graph(self, name: str = ""):
        lst = await self.request_to_get_result_auc()
        sum_quantity = 0
        if not lst:
            pass
        elif lst[0] == "deals":
            print(lst[1], type(lst[1]))
            for key in lst[1].keys():
                sum_quantity += int(lst[1][key]["quantity"] * 1_000)
            print(sum_quantity / 1000)
        elif lst[0] == "not_purchased":
            sum_quantity += (lst[1]["quantity"] * 1_000)
        self.generator.generate_deals(sum_quantity / 1_000, name=name)

    async def request_to_set_lot(self, action: str, bet: dict):
        if action in ["buy", "sell"]:
            async with aiohttp.ClientSession() as session:
                print(f"\n\n{bet}\n\n")
                response = await session.post(f"{self.url}/add_bet_{action}/", json=bet)
                return response.status
        else:
            raise ValueError

    async def request_to_get_result_auc(self):
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"{self.url}/get_VCG_result_for_agent/{self.agent_id}")
            print(await response.json(), type(await response.json()))
            return await response.json()

    def get_bet(self, stake: float, lot: float) -> Bet:
        return Bet(user_id=self.agent_id, stake=stake, lot=lot)

    async def loop(self):
        # TODO
        # доделать запрос в result auction по id и получать то сколько нам удалось купить, а потом подключать дизель
        name_k = 0
        while True:
            cost = uniform(50, 100)
            name = f"{self.name}{name_k}"
            # name = f"images/example_agent_{name_k}"
            self.generation(name)

            energy = self.get_total_energy()
            """energy - какое количество жнергии у нас сейчас в result"""
            if energy > 0.5:
                bet = self.get_bet(lot=round(energy - 0.5, 3),
                                   stake=round(round(energy - 0.5, 3) * cost, 2)).to_dict()
                action = "sell"
                print(f"sell в размере {bet['bet']} по стоимости: {bet['lot']}")
            else:
                bet = self.get_bet(lot=round(0.5 - energy, 3),
                                   stake=round(round(0.5 - energy, 3) * cost, 2)).to_dict()
                action = "buy"
                print(f"buy в размере {bet['bet']} по стоимости: {bet['lot']}")
            if bet and action:
                await self.request_to_set_lot(action, bet)



            name_k += 1

            await asyncio.sleep(self.d_itme)

            # await self.request_to_get_result_auc()
            await self.get_deals_and_remake_graph(name)


if __name__ == '__main__':
    import os

    if os.name == 'nt':
        """crutch for windows"""
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    agent = Agent("123")
    asyncio.run(agent.loop())
