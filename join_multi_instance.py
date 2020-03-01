import argparse
import asyncio
from importlib import reload

from bot2 import bot2
from sc2 import Race
from sc2.client import Client
from sc2.main import _play_game
from sc2.player import Bot, Human
from sc2.portconfig import Portconfig
from sc2.protocol import ConnectionAlreadyClosed
from sc2.sc2process import SC2Process


async def _join_game_aiter(players, realtime, portconfig):
    assert players, "Can't create a game without players"

    assert any(isinstance(p, (Human, Bot)) for p in players)

    async with SC2Process() as server:
        while True:
            await server.ping()

            client = Client(server._ws)

            try:
                result = await _play_game(players[1], client, realtime, portconfig)
                await client.leave()
            except ConnectionAlreadyClosed:
                print(f"Connection was closed before the game ended")
                return

            new_players = yield result
            if new_players is not None:
                players = new_players


def _join_game_iter(*args, **kwargs):
    game = _join_game_aiter(*args, **kwargs)
    new_playerconfig = None
    while True:
        new_playerconfig = yield asyncio.get_event_loop().run_until_complete(game.asend(new_playerconfig))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port_config")
    args = parser.parse_args()

    portconfig = Portconfig.from_json(args.port_config)

    player_config = [
        Bot(Race.Terran, None),
        Bot(Race.Zerg, bot2.Bot2())
    ]

    gen = _join_game_iter(
        player_config,
        realtime=False,
        portconfig=portconfig
    )

    while True:
        r = next(gen)
        reload(bot2)
        player_config[0].ai = bot2.Bot2()
        gen.send(player_config)


if __name__ == "__main__":
    main()
