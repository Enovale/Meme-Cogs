import discord
from discord.ext import commands
from cogs.utils import checks
import os
import asyncio
from cogs.utils.dataIO import dataIO
import requests

WINDOWS_OS = os.name == 'nt'

class MassRename:
    """Rename's everyone in a server to your liking (((BE CAREFUL WITH THIS)))"""

    def __init__(self, bot):
        self.bot = bot

        
    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def massrename(self, ctx, nickname=""):
        """Renames everyone in the server to what you specify"""
        
        nickname = nickname.strip();
        for member in ctx.message.server.members:
            try:
                await self.bot.change_nickname(member, nickname)
            except discord.Forbidden:
                await self.bot.say("I cannot do that, I lack the "
                                   "\"Manage Nicknames\" permission, or the user " + member.name + " has a higher role placement than I do.")

    @commands.command(no_pm=True, pass_context=True)
    async def botrename(self, ctx, nickname=""):
        """Renames the bot to what you specify"""
        
        nickname = nickname.strip();
            try:
                await self.bot.change_nickname(self.bot.user, nickname)
            
def setup(bot):
    bot.add_cog(MassRename(bot))
