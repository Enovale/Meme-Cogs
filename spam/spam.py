import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	async def spam(self, ctx, user=None, number: int=None, spam_text: str):
		"""Spam The User hehe"""
		
		if len(ctx.message.mentions):
			user = ctx.message.mentions[0]
		if type(user) == discord.User or type(user) == discord.Member:
			notneeded = True
		if ctx.message.author.member.id == "234014949888884736":
			await self.bot.say("no")
			return
		for i in range(number):
			await self.bot.send_message(user, spam_text)
			
def setup(bot):
	bot.add_cog(Spam(bot))
