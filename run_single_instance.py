from importlib import reload

import sc2
from bot1 import bot1 as bot_ai
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer


def main():
    player_config = [
        Bot(Race.Zerg, bot_ai.Bot1()),
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
        player_config[0].ai = bot_ai.Bot1()
        gen.send(player_config)


if __name__ == "__main__":
    main()
