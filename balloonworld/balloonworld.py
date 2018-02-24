import discord
import asyncio
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
from discord.ext import commands
import os
import re
import time

class BalloonWorld:

    def __init__(self, bot):
        self.bot = bot
        self.gameStarted = False
        self.balloonHid = False
        self.timedOut = False
        self.balloonText = ""
        
    async def shouldStop(self, mode):
        if mode == "hide":
            timeout = time.time() + 30
        if mode == "seek":
            timeout = time.time() + 40
        while True:
            if self.balloonHid == True:
                self.timedOut = False
                return True
            if time.time() > timeout:
                return True
                self.timedOut = True
                
    async def startHideSequence(self):
        if self.gameStarted == False:
            return
        await self.shouldStop("hide")
        if self.timedOut == True:
            await self.bot.send_message(self.gameChannel, "You ran out of time, Bro! I'll stop the game for you.")
        if self.timedOut == False:
            self.bot.send_message(self.gameChannel, "Balloon hid.")
            
    @commands.command(pass_context=True)
    async def seek(self):
        await self.bot.send_message(self.gameChannel, "Alright " + "seeker" + "! Ready to seek?")
        msg = await self.bot.wait_for_message(content='yes')
        await self.bot.send_message(self.gameChannel, "Nice on! A'ight, seeking in: 3")
        time.sleep(1)
        await self.bot.send_message(self.gameChannel, "2")
        time.sleep(1)
        await self.bot.send_message(self.gameChannel, "1")
        time.sleep(1)
        await self.shouldStop("seek")
        msg = await self.bot.wait_for_message(timeout=40, author=seeker)
        if msg == None:
            await self.bot.send_message(self.gameChannel, "You ran out of time, Bro! Ill stop the game.")
            return
        if msg == self.balloonText:
            await self.bot.send_message(self.gameChannel, "WOAH YOU DID IT XD")
        if msg != self.balloonText:
            await self.bot.send_message(self.gameChannel, "Wrong.")
    
    @commands.command(pass_context=True)
    async def hide(self, ctx):
        emoji = "🎈"
        channel = ctx.message.channel
        self.gameChannel = ctx.message.channel
        if "<" in emoji and ">" in emoji:
            emoji = emoji.strip("<>")
        server = ctx.message.server
        await self.bot.say("Hey Bro! Wanna play some Balloon World?")
        msg = await self.bot.wait_for_message(author=ctx.message.author, content='yes')
        await self.bot.say("Nice! Game starting in 3")
        time.sleep(1)
        await self.bot.say("2")
        time.sleep(1)
        await self.bot.say("1")
        time.sleep(1)
        await self.bot.say("GO")
        self.gameStarted = True
        await self.startHideSequence()
  
    async def on_reaction_add(self, reaction, user):
        server = reaction.message.server
        msg = reaction.message
        if self.gameStarted == False:
            return
        if "🎈" in str(reaction.emoji):
            await self.bot.send_message(self.gameChannel, "You ballooned. Yay.")
            self.balloonHid = True
            self.balloonText = reaction.message.content
            author = reaction.message.author
            channel = reaction.message.channel
            if reaction.message.embeds != []:
                print()
            else:
                print()
        else:
            return

def check_folder():
    if not os.path.exists('data/balloonworld'):
        os.mkdir('data/balloonworld')


def setup(bot):
    check_folder()
    n = BalloonWorld(bot)
    bot.add_listener(n.on_reaction_add, 'on_emoji_reaction')
    bot.add_cog(n)
