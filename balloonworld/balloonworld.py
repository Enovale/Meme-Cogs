import discord
import asyncio
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
from discord.ext import commands
import os
import re
import time
import pickle

gameChannel = None
gameStarted = False
balloonHid = False
timedOut = False
balloonText = None
rejected = False
    
class BalloonWorld:

    def __init__(self, bot):
        self.bot = bot
        
    async def saveObj(self, obj):
        f = open('data/balloonworld/database.txt', 'wb')
        pickle.dump(obj, f)
        f.close()
        
    async def loadObj(self, obj):
        f = open('data/balloonworld/database.txt', 'rb')
        obj = pickle.load(f)
        f.close()
        return obj
    
    @commands.command()
    async def howto(self):
        await self.bot.say("How to play Luigi's Balloon World in Discord:\n\n"
                           ""
                           "=====Hiding=====\n"
                           "1. Type ``b!hideit`` and say yes\n"
                           "2. Once the game starts, react to any message you please with a balloon emoji, or ``🎈``\n"
                           "3. Your message will be recorded\n\n"
                           ""
                           "=====Finding=====\n"
                           "1. Type ``b!findit`` and say yes\n"
                           "2. Once the game starts, find the message with the balloon (or ``🎈``) reaction, and say whatever the content of the message is\n"
                           "3. If you are correct, Luigi will congratulate you")
        
    async def check(self, message):
        global rejected
        if message == "yes" or message == "Yes" or message == "Yeah":
            return True
        if message == "no" or message == "No" or message == "Nah" or message == "nah":
            await self.bot.send_message(gameChannel, "Play again some time!")
            rejected = True
            return False
        
    async def shouldStop(self, mode):
        if mode == "hide":
            timeout = time.time() + 30
            print("Currently hiding")
        if mode == "seek":
            timeout = time.time() + 40
        global timedOut
        global balloonHid
        while True:
            if balloonHid == True:
                timedOut = False
                return
            if time.time() > timeout:
                return True
                timedOut = True
            time.sleep(0.2)
                
    async def startHideSequence(self):
        global gameStarted
        global timedOut
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
            return True
        global gameChannel
        gameChannel = ctx.message.channel
        await self.bot.send_message(gameChannel, "Hey Bro! Wanna play some Balloon World?")
        msg = await self.bot.wait_for_message(author=ctx.message.author, check=self.check)
        global rejected
        if rejected == True:
            return False
        message = await self.bot.send_message(gameChannel, "Nice on! A'ight, seeking in: 3")
        time.sleep(1)
        await self.bot.edit_message(message, new_content=message.content + ", 2")
        time.sleep(1)
        await self.bot.edit_message(message, new_content=message.content + ", 2, 1")
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
        msg = await self.bot.wait_for_message(author=ctx.message.author, check=self.check)
        global rejected
        if rejected == True:
            return False
        message = await self.bot.say("Nice! Game starting in 3")
        time.sleep(0.5)
        await self.bot.edit_message(message, new_content=message.content + ", 2")
        time.sleep(0.5)
        await self.bot.edit_message(message, new_content=message.content + ", 2, 1")
        time.sleep(0.5)
        await self.bot.say("GO")
        gameStarted = True
        await self.startHideSequence()
        
    @commands.command()    
    async def cheat(self):
        global balloonText
        global balloonHid
        await self.bot.say(balloonText + " " + str(balloonHid))
        
    @commands.command()
    async def testsave(self):
        testdict = {"test": "test"}
        saveObj(testdict)
  
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
            server = channel.server.id
            loadObj(testdict)
            testdict = testdict + {author.id: {'server': server, 'channel': channel.name, 'text': balloonText}}
            await self.bot.send_message(channel, "Testdict is " + str(testdict))
            if reaction.message.embeds != []:
                print()
            else:
                print()
        else:
            return
        
def check_files():
    f = 'data/balloonworld/database.txt'
    if not os.path.exists(f):
        fileIO(f, 'save', {})

def check_folder():
    if not os.path.exists('data/balloonworld'):
        os.mkdir('data/balloonworld')


def setup(bot):
    check_folder()
    check_files()
    n = BalloonWorld(bot)
    bot.add_listener(n.on_reaction_add, 'on_emoji_reaction')
    bot.add_cog(n)
