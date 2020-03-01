from importlib import reload

import sc2
from bot import bot as bot_ai
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

bot = Bot(Race.Terran, bot_ai.Bot())


def main():
    player_config = [
        Bot(Race.Zerg, bot_ai.Bot()),
        Computer(Race.Terran, Difficulty.Medium)
    ]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("Abyssal Reef LE"),
        player_config,
        realtime=False
    )

    while True:
        r = next(gen)
        reload(bot_ai)
        player_config[0].ai = bot_ai.Bot()
        gen.send(player_config)

if __name__ == "__main__":
    main()
