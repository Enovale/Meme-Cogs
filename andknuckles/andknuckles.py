import discord
from discord.ext import commands
import os
from cogs.utils.dataIO import dataIO
import random

WINDOWS_OS = os.name == 'nt'

class andknuckles:
    """Exterminates thots"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def andknuckles(self, ctx, length):
        """Makes an & Knuckles meme of a given length."""
        
        prefixes = ["New ", "Super ", "Deluxe "]
        suffixes = ["DLC", "Zombie flavoured", "DD ", "HD "]

        #Your code will go here
        random.shuffle(prefixes)
        random.shuffle(suffixes)
        length = int(length)
        del prefixes[length:]
        del suffixes[length:]
        prefstr = ''.join(prefixes)
        suffstr = ''.join(suffixes)
        await self.bot.say("" + prefstr + suffstr)

def setup(bot):
    bot.add_cog(andknuckles(bot))
