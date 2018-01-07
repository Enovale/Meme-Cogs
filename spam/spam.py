import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	async def spam(self, ctx, user=None, number: int=None, spam_text: str=None):
		"""Spam The User hehe"""
		
		elif len(ctx.message.mentions):
			user = ctx.message.mentions[0]
		if type(user) == discord.User or type(user) == discord.Member:
			notneeded = True
		elif user == "@everyone":
			user = "@everyone"
		if spam_text == None:
			await self.bot.say('Wait What Dude Want To Spam Sombody Nothing Wew')
			return
		for i in range(number):
			await self.bot.send_message(user, spam_text)
			
def setup(bot):
	bot.add_cog(Spam(bot))
