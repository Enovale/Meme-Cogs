import discord
from discord.ext import commands

class Shoot:
    """Allows you to shoot a user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def shoot(self, ctx, user : discord.Member):
        """Will shoot the user specified, (be careful with that gun!)"""
        
        #Your code will go here
        if ctx.message.author.id != user.id:
            await self.bot.say(ctx.message.author.mention + " gunned down " + user.mention + " !")
        else:
            await self.bot.say(ctx.message.author.mention + " couldn't take it and shot themselves.")

def setup(bot):
    bot.add_cog(Shoot(bot))
