import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks

__author__ = "MasterKnight"
class rainbow:
    """Rainbows the selected role"""

    def __init__(self, bot):
        self.bot = bot
        loop = asyncio.get_event_loop()
	
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def arainbow(self, ctx, interval:float, *, role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
        else:
            await self.bot.say("Enabled Rainbow-age for that role")
        while True:
            try:
                colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
                colour = int(colour, 16)
                await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
                await asyncio.sleep(interval)
            except Exception as e:
                await self.bot.say(e)
                await self.bot.say("This error may be caused by insufficient permissions. Make sure the role your trying to rainbow is ***below*** the role im in and the role im in has manage role permissions.")


    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def rainbow(self, ctx, *, role: discord.Role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
        else:
            await self.bot.say("Enabled Rainbow-age for that role")
        
        while True:
            try:
                colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
                colour = int(colour, 16)
                await self.bot.edit_role(ctx.message.server, role, colour=discord.Colour(value=colour))
                await asyncio.sleep(200.0)
            except Exception as e:
                await self.bot.say(e)
                await self.bot.say("This error may be caused by insufficient permissions. Make sure the role your trying to rainbow is ***below*** the role im in and the role im in has manage role permissions.")

	

	
	
	
def setup(bot):
    n = rainbow(bot)
    bot.add_cog(n)
