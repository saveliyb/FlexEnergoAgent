from nerandom import get_values
import asyncio
import aiohttp
from classes import Bet


class Agent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.url = "http://127.0.0.1:8000"
        self.d_time = 20
        self.get_graph()

    def get_graph(self):
        self.graph = get_values(self.agent_id)

    async def req(self, action: str, bet: dict):
        if action in ["buy", "sell"]:
            async with aiohttp.ClientSession() as session:
                print(f"\n\n{bet}\n\n")
                response = await session.post(f"{self.url}/add_bet_{action}/", json=bet)
                return response.status
        else:
            raise ValueError
            # print(response)

    def get_bet(self, stake: float, lot: float) -> Bet:
        return Bet(user_id=self.agent_id, stake=stake, lot=lot)

    async def loop(self):
        averange_cost = 2.23

        for i, energy in enumerate(self.graph[1]):
            print(energy, "\n", i, end=" ")
            bet = None
            action = ""
            if energy > 0.5:
                bet = self.get_bet(lot=round(energy - 0.5, 3),
                                   stake=round(round(energy - 0.5, 3) * averange_cost, 2)).to_dict()
                action = "buy"
                print(f"sell в размере {bet['bet']} по стоимости: {bet['lot']}")

            else:
                bet = self.get_bet(lot=round(0.5 - energy, 3),
                                   stake=round(round(0.5 - energy, 3) * averange_cost, 2)).to_dict()
                action = "sell"
                print(f"buy в размере {bet['bet']} по стоимости: {bet['lot']}")
            if bet and action:
                await self.req(action, bet)

            await asyncio.sleep(self.d_time)
        return


if __name__ == '__main__':
    import os

    if os.name == 'nt':
        """crutch for windows"""
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    agent = Agent("123")
    asyncio.run(agent.loop())

