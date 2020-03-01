import argparse
from importlib import reload

import sc2
from bot1 import bot1
from sc2 import Race
from sc2.player import Bot
from sc2.portconfig import Portconfig


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port_config")
    args = parser.parse_args()

    portconfig = Portconfig.from_json(args.port_config)

    player_config = [
        Bot(Race.Terran, bot1.Bot1()),
        Bot(Race.Zerg, None)
    ]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("Abyssal Reef LE"),
        player_config,
        realtime=False,
        portconfig=portconfig
    )

    while True:
        r = next(gen)
        reload(bot1)
        player_config[0].ai = bot1.Bot1()
        gen.send(player_config)


if __name__ == "__main__":
    main()
