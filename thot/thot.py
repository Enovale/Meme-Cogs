import discord
from discord.ext import commands
import os
from cogs.utils.dataIO import dataIO

WINDOWS_OS = os.name == 'nt'

class Thot:
    """Exterminates thots"""

    def __init__(self, bot):
        self.bot = bot
        self.path = os.path.join("data", "thot")

    @commands.command(pass_context=True)
    async def thot(self, ctx):
        """Exterminates thots"""

        #Your code will go here
        channel = ctx.message.channel
        await self.bot.say("Omae wa mou Shindeiru")
        await self.bot.say("***NANI?!??!!***")
        with open(self.path + '/thot.gif', 'rb') as f:
            await self.bot.send_file (channel, f)

def setup(bot):
    bot.add_cog(Thot(bot))
