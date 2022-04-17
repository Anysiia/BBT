from twitchio.ext import commands
import config_bbt as cfg


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=cfg.twitchio_config["OAUTH_TOKEN"],
                         prefix='?',
                         initial_channels=cfg.twitchio_config["CHANNEL_NAME"])

    async def event_ready(self):
        await self.connected_channels[0].send("Hello")

bot = Bot()
bot.run()
