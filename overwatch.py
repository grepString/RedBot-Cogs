import discord
from discord.ext import commands
import json
import requests

class Overwatch:

    """Overwatch Stats"""

    def __init__(self, bot):
        self.bot = bot
        self.mode = ["casual", "competitive"]

    @commands.command()
    async def ow(self, username : str, gamemode : str):
        """Fetches your Overwatch stats.
        Accepts casual or competitive for gamemode
        Usernames are case-sensitive!
        Example: !ow Err0rist-1814 casual"""
        gamemode = gamemode.lower()
        if not gamemode in self.mode:
            await self.bot.say("Invalid gamemode. Choose casual or competitive")
            return
        url = requests.get("https://owapi.net/api/v2/u/"+username+"/stats/"+gamemode)
        output = json.loads(url.text)

        # Casual variables
        level = str(url.json()["overall_stats"]["level"])
        wins = str(url.json()["overall_stats"]["wins"])
        losses = str(url.json()["overall_stats"]["losses"])
        mostDamage = str(url.json()["game_stats"]["damage_done_most_in_game"])
        mostHealing = str(url.json()["game_stats"]["healing_done_most_in_game"])
        mostElims = str(url.json()["game_stats"]["eliminations_most_in_game"])
        mostobjTime = str(url.json()["game_stats"]["objective_time_most_in_game"])
        mostobjKills = str(url.json()["game_stats"]["objective_kills_most_in_game"])
        mostFire = str(url.json()["game_stats"]["time_spent_on_fire_most_in_game"])
        totalDamage = str(url.json()["game_stats"]["damage_done"])
        totalHealing = str(url.json()["game_stats"]["healing_done"])
        totalElims = str(url.json()["game_stats"]["eliminations"])
        totalobjTime = str(url.json()["game_stats"]["objective_time"])
        totalobjKills = str(url.json()["game_stats"]["objective_kills"])
        totalFire = str(url.json()["game_stats"]["time_spent_on_fire"])
        goldMedals = str(url.json()["game_stats"]["medals_gold"])
        silverMedals = str(url.json()["game_stats"]["medals_silver"])
        bronzeMedals = str(url.json()["game_stats"]["medals_bronze"])
        timePlayed = str(url.json()["game_stats"]["time_played"])

        # Competitive variable
        compRank = str(url.json()["overall_stats"]["comprank"])

        if gamemode == "casual":
            data = "```diff\n"
            data += "!=============[Overwatch Casual Stats]=============!\n"
            data += "+ Level: {}\n".format(level)
            data += "+ Wins: {}\n".format(wins)
            data += "+ Losses: {}\n".format(losses)
            data += "+ Most Damage in 1 Game: {}\n".format(mostDamage)
            data += "+ Most Healing in 1 Game: {}\n".format(mostHealing)
            data += "+ Most Elims in 1 Game: {}\n".format(mostElims)
            data += "+ Most Objective Time in 1 Game: {}\n".format(mostobjTime)
            data += "+ Most Objective Kills in 1 Game: {}\n".format(mostobjKills)
            data += "+ Most Time on Fire in 1 Game: {}\n".format(mostFire)
            data += "+ Total Damage: {}\n".format(totalDamage)
            data += "+ Total Healing: {}\n".format(totalHealing)
            data += "+ Total Elims: {}\n".format(totalElims)
            data += "+ Total Objective Time: {}\n".format(totalobjTime)
            data += "+ Total Objective Kills: {}\n".format(totalobjKills)
            data += "+ Total Time on Fire: {}\n".format(totalFire)
            data += "+ Gold Medals: {}\n".format(goldMedals)
            data += "+ Silver Medals: {}\n".format(silverMedals)
            data += "+ Bronze Medals: {}\n".format(bronzeMedals)
            data += "+ Time Played: {}\n".format(timePlayed)
            data += "!==================================================!\n"
            data += "```"
            await self.bot.say(data)

        if gamemode == "competitive":
            data = "```diff\n"
            data += "!===========[Overwatch Competitive Stats]===========!\n"
            data += "+ Level: {}\n".format(level)
            data += "+ Competitive Rank: {}\n".format(compRank)
            data += "+ Wins: {}\n".format(wins)
            data += "+ Losses: {}\n".format(losses)
            data += "+ Most Damage in 1 Game: {}\n".format(mostDamage)
            data += "+ Most Healing in 1 Game: {}\n".format(mostHealing)
            data += "+ Most Elims in 1 Game: {}\n".format(mostElims)
            data += "+ Most Objective Time in 1 Game: {}\n".format(mostobjTime)
            data += "+ Most Objective Kills in 1 Game: {}\n".format(mostobjKills)
            data += "+ Most Time on Fire in 1 Game: {}\n".format(mostFire)
            data += "+ Total Damage: {}\n".format(totalDamage)
            data += "+ Total Healing: {}\n".format(totalHealing)
            data += "+ Total Elims: {}\n".format(totalElims)
            data += "+ Total Objective Time: {}\n".format(totalobjTime)
            data += "+ Total Objective Kills: {}\n".format(totalobjKills)
            data += "+ Total Time on Fire: {}\n".format(totalFire)
            data += "+ Gold Medals: {}\n".format(goldMedals)
            data += "+ Silver Medals: {}\n".format(silverMedals)
            data += "+ Bronze Medals: {}\n".format(bronzeMedals)
            data += "+ Time Played: {}\n".format(timePlayed)
            data += "!===================================================!\n"
            data += "```"
            await self.bot.say(data)

def setup(bot):
    bot.add_cog(Overwatch(bot))
