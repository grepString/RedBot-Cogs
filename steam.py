import discord
from discord.ext import commands
import json
import requests

class Steam:

    """Steam Connect Protocol"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def connect(self, ip : str):
        """Creates a URL to connect
        to a Steam game server.
        Example: !connect 12.34.56.78:27015"""

        url = "steam://connect/"+ip
        await self.bot.say(url)

    @commands.command()
    async def browser(self):
        """Opens your Steam server browser
        """

        url = "steam://open/servers"
        await self.bot.say(url)

def setup(bot):
    bot.add_cog(Steam(bot))
