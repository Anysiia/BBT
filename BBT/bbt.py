from twitchio.ext import commands
from config_bbt import twitchio_config as config


class BetterBotTwitchException(Exception):
    """Exception specific to the bot"""


class WrongConfigException(BetterBotTwitchException):
    """Exception for missing configuration"""


class BetterBotTwitch(commands.Bot):

    def __init__(self):
        if "OAUTH_TOKEN" not in config or "CHANNEL_NAME" not in config:
            raise WrongConfigException
        super().__init__(token=config["OAUTH_TOKEN"],
                         prefix='?',
                         initial_channels=config["CHANNEL_NAME"])

    async def event_ready(self):
        message = config["START_MESSAGE"] if "START_MESSAGE" in config else "Hello"
        await self.connected_channels[0].send(message)
