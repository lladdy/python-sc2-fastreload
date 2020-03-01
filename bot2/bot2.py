import sc2


class Bot2(sc2.BotAI):

    async def on_start(self):
        print('on_start')

        # worker rush
        for worker in self.workers:
            self.do(worker.attack(self.enemy_start_locations[0]))

    async def on_step(self, iteration: int):
        pass

    async def on_end(self, game_result: sc2.Result):
        print('on_end')
