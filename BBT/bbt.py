from twitchio.ext import commands


class Bot(commands.bot):

    def __init__(self):
        super().__init__(token='ACCESS_TOKEN', prefix='?', initial_channels=['...'])


bot = Bot()
bot.run()
