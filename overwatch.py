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

        # Stat Variables
        level = int(url.json()["overall_stats"]["level"])
        wins = int(url.json()["overall_stats"]["wins"])
        losses = int(url.json()["overall_stats"]["losses"])
        prestige = int(url.json()["overall_stats"]["prestige"])
        mostDamage = int(url.json()["game_stats"]["damage_done_most_in_game"])
        mostHealing = int(url.json()["game_stats"]["healing_done_most_in_game"])
        mostElims = int(url.json()["game_stats"]["eliminations_most_in_game"])
        mostobjTime = float(url.json()["game_stats"]["objective_time_most_in_game"])
        mostobjKills = int(url.json()["game_stats"]["objective_kills_most_in_game"])
        mostFire = float(url.json()["game_stats"]["time_spent_on_fire_most_in_game"])
        totalDamage = int(url.json()["game_stats"]["damage_done"])
        totalHealing = int(url.json()["game_stats"]["healing_done"])
        totalElims = int(url.json()["game_stats"]["eliminations"])
        totalobjTime = float(url.json()["game_stats"]["objective_time"])
        totalobjKills = int(url.json()["game_stats"]["objective_kills"])
        totalFire = float(url.json()["game_stats"]["time_spent_on_fire"])
        goldMedals = int(url.json()["game_stats"]["medals_gold"])
        silverMedals = int(url.json()["game_stats"]["medals_silver"])
        bronzeMedals = int(url.json()["game_stats"]["medals_bronze"])
        timePlayed = float(url.json()["game_stats"]["time_played"])

        # Competitive Variable
        compRank = int(url.json()["overall_stats"]["comprank"])

        if gamemode == "casual":
            data = "```diff\n"
            data += "!==========[Overwatch Casual Stats]==========!\n"
            data += "+ Level: {}\n".format(level)
            data += "+ Prestige: {}\n".format(prestige)
            data += "+ Wins: {}\n".format(wins)
            data += "+ Losses: {}\n".format(losses)
            data += "+ Most Damage in 1 Game: {0:.0f}\n".format(mostDamage)
            data += "+ Most Healing in 1 Game: {0:.0f}\n".format(mostHealing)
            data += "+ Most Elims in 1 Game: {0:.0f}\n".format(mostElims)
            data += "+ Most Objective Time in 1 Game: {0:.2f} hrs\n".format(mostobjTime)
            data += "+ Most Objective Kills in 1 Game: {0:.0f}\n".format(mostobjKills)
            data += "+ Most Time on Fire in 1 Game: {0:.2f} hrs\n".format(mostFire)
            data += "+ Total Damage: {0:.0f}\n".format(totalDamage)
            data += "+ Total Healing: {0:.0f}\n".format(totalHealing)
            data += "+ Total Eliminations: {0:.0f}\n".format(totalElims)
            data += "+ Total Objective Time: {0:.2f} hrs\n".format(totalobjTime)
            data += "+ Total Objective Kills: {0:.0f}\n".format(totalobjKills)
            data += "+ Total Time on Fire: {0:.2f} hrs\n".format(totalFire)
            data += "+ Gold Medals: {0:.0f}\n".format(goldMedals)
            data += "+ Silver Medals: {0:.0f}\n".format(silverMedals)
            data += "+ Bronze Medals: {0:.0f}\n".format(bronzeMedals)
            data += "+ Time Played: {0:.2f} hrs\n".format(timePlayed)
            data += "!============================================!\n"
            data += "```"
            await self.bot.say(data)

        if gamemode == "competitive":
            data = "```diff\n"
            data += "!========[Overwatch Competitive Stats]========!\n"
            data += "+ Level: {}\n".format(level)
            data += "+ Prestige: {}\n".format(prestige)
            data += "+ Rank: {}\n".format(compRank)
            data += "+ Wins: {}\n".format(wins)
            data += "+ Losses: {0:.0f}\n".format(losses)
            data += "+ Most Damage in 1 Game: {0:.0f}\n".format(mostDamage)
            data += "+ Most Healing in 1 Game: {0:.0f}\n".format(mostHealing)
            data += "+ Most Elims in 1 Game: {0:.0f}\n".format(mostElims)
            data += "+ Most Objective Time in 1 Game: {0:.2f} hrs\n".format(mostobjTime)
            data += "+ Most Objective Kills in 1 Game: {0:.0f}\n".format(mostobjKills)
            data += "+ Most Time on Fire in 1 Game: {0:.2f} hrs\n".format(mostFire)
            data += "+ Total Damage: {0:.0f}\n".format(totalDamage)
            data += "+ Total Healing: {0:.0f}\n".format(totalHealing)
            data += "+ Total Eliminations: {0:.0f}\n".format(totalElims)
            data += "+ Total Objective Time: {0:.2f} hrs\n".format(totalobjTime)
            data += "+ Total Objective Kills: {0:.0f}\n".format(totalobjKills)
            data += "+ Total Time on Fire: {0:.2f} hrs\n".format(totalFire)
            data += "+ Gold Medals: {0:.0f}\n".format(goldMedals)
            data += "+ Silver Medals: {0:.0f}\n".format(silverMedals)
            data += "+ Bronze Medals: {0:.0f}\n".format(bronzeMedals)
            data += "+ Time Played: {0:.2f} hrs\n".format(timePlayed)
            data += "!=============================================!\n"
            data += "```"
            await self.bot.say(data)

def setup(bot):
    bot.add_cog(Overwatch(bot))
