import asyncio
from discord.ext import commands
import discord
import inspect
import sys
import traceback
import re

class blankhelp:
    """Custimized Help For LBB"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, hidden=True)
    async def help(self, ctx):
        """Shows This Command"""
        destination = author if self.bot.pm_help else ctx.message.channel
        await self.bot.send_message(destination, "Thank's for using Luigi's Balloon Bot! Simply use ```b!findit or b!hideit``` to play! Type ``b!howto`` to learn how to play!")

def setup(bot):
    bot.remove_command('help')
    n = blankhelp(bot)
    bot.add_cog(n)
