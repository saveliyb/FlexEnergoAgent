import asyncio

from Agentv01 import Agent

if __name__ == '__main__':
    if __name__ == '__main__':
        import os

        if os.name == 'nt':
            """crutch for windows"""
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        agent = Agent("01", name="images01/example_agent_")
        asyncio.run(agent.loop())
