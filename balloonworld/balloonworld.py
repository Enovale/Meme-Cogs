import discord
import asyncio
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
from discord.ext import commands
import os
import re
import time

gameStarted = False
balloonHid = False
timedOut = False
balloonText = ""
    
class BalloonWorld:

    def __init__(self, bot):
        self.bot = bot
        
    async def shouldStop(self, mode):
        if mode == "hide":
            timeout = time.time() + 30
        if mode == "seek":
            timeout = time.time() + 40
        while True:
            if balloonHid == True:
                timedOut = False
                return True
            if time.time() > timeout:
                return True
                timedOut = True
                
    async def startHideSequence(self):
        global gameStarted
        global timedOut
        if gameStarted == False:
            return
        await self.shouldStop("hide")
        if timedOut == True:
            await self.bot.send_message(gameChannel, "You ran out of time, Bro! I'll stop the game for you.")
        if timedOut == False:
            await self.bot.send_message(gameChannel, "Balloon hid.")
            
    @commands.command(pass_context=True)
    async def findit(self, ctx):
        global balloonText
        if balloonText == "":
            await self.bot.say("Sorry Bro! Noone's hid any balloons!")
            return
        gameChannel = ctx.message.channel
        await self.bot.send_message(gameChannel, "Hey Bro! Wanna play some Balloon World?")
        msg = await self.bot.wait_for_message(content='yes')
        await self.bot.send_message(gameChannel, "Nice on! A'ight, seeking in: 3")
        time.sleep(1)
        await self.bot.send_message(gameChannel, "2")
        time.sleep(1)
        await self.bot.send_message(gameChannel, "1")
        time.sleep(1)
        await self.bot.send_message(gameChannel, "GO")
        msg = await self.bot.wait_for_message(timeout=40, author=ctx.message.author)
        if msg == None:
            await self.bot.send_message(gameChannel, "You ran out of time, Bro! Ill stop the game.")
            return
        if msg.content == balloonText:
            await self.bot.send_message(gameChannel, "WOAH YOU DID IT XD")
        else:
            await self.bot.send_message(gameChannel, "Wrong.")
    
    @commands.command(pass_context=True)
    async def hideit(self, ctx):
        global balloonHid
        balloonHid = False
        emoji = "🎈"
        channel = ctx.message.channel
        global gameChannel
        global gameStarted
        gameStarted = False
        gameChannel = ctx.message.channel
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
        gameStarted = True
        await self.startHideSequence()
        
    @commands.command()    
    async def cheat(self):
        global balloonText
        global balloonHid
        await self.bot.say(balloonText + " " + str(balloonHid))
  
    async def on_reaction_add(self, reaction, user):
        server = reaction.message.server
        msg = reaction.message
        global gameStarted
        if gameStarted == False:
            return
        if "🎈" in str(reaction.emoji):
            global balloonHid
            balloonHid = True
            global balloonText
            balloonText = reaction.message.content
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
