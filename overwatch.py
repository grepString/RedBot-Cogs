import discord
from discord.ext import commands
import aiohttp
import json
import urllib2

class Ow:
    """Overwatch Stats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ow(self, username, general):

        #Your code will go here
        url = "https://owapi.net/api/v2/u/" + username + "/stats/" + general +#build the web adress
        data = json.load(url)
        await self.bot.say(data)

def setup(bot):
    bot.add_cog(Ow(bot))