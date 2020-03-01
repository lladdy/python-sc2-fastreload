from importlib import reload

# import sc2
# from bot1 import bot1
# from sc2 import Race, Difficulty
# from sc2.player import Bot, Computer
# from sc2.portconfig import Portconfig
#
#
#
# def main():
#     portconfig = sc2.portconfig.Portconfig()
#     # portconfig = Portconfig.from_json('{"shared": 24469, "server": [22892, 22272], "players": [[23726, 22865], [21779, 23937]]}')
#     print(portconfig.as_json)
#
#     player_config = [
#         Bot(Race.Zerg, bot1.Bot1()),
#         Bot(Race.Zerg, None)
#     ]
#
#     for g in sc2.main._host_game_iter(
#         sc2.maps.get("Abyssal Reef LE"),
#         player_config,
#         realtime=False,
#         portconfig=portconfig
#     ):
#         print(g)
#
#
# if __name__ == "__main__":
#     main()
#


from importlib import reload

import sc2
from bot1 import bot1
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer, Human


def main():
    portconfig = sc2.portconfig.Portconfig()
    print(portconfig.as_json)

    player_config = [
        # Bot(Race.Zerg, bot_ai.Bot2()),
        # Computer(Race.Terran, Difficulty.Medium)
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
