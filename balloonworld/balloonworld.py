import discord
import asyncio
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
from discord.ext import commands
import os
import re
import time
import pickle
import threading

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
        
    async def loadObj(self):
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
        
    def check(self, message):
        global rejected
        if message == "yes" or message == "Yes" or message == "Yeah" or message == "yeah":
            print("Test Yes")
            return True
        if message == "no" or message == "No" or message == "Nah" or message == "nah":
            rejected = True
            return False
        else:
            return False
        
    async def setTimedOut(self):
        global timedOut
        timedOut = True
        
    def shouldStop(self, mode):
        if mode == "hide":
            t = threading.Timer(30.0,self.setTimedOut)
        if mode == "seek":
            t = threading.Timer(40.0,self.setTimedOut)
        global timedOut
        global balloonHid
        if (balloonHid == True):
            t.cancel()
            timedOut = False
                
    async def startHideSequence(self):
        global gameStarted
        global timedOut
        self.shouldStop("hide")
        if timedOut == True:
            await self.bot.send_message(gameChannel, "You ran out of time, Bro! I'll stop the game for you.")
        if timedOut == False:
            await self.bot.send_message(gameChannel, "Balloon hid.")
            
    @commands.command(pass_context=True)
    async def findit(self, ctx, user: discord.Member):
        database = await self.loadObj()
        if ctx.message.channel.name != database[user.id]['channel']:
            if ctx.message.server.id != database[user.id]['server']:
                await self.bot.say("Sorry Bro! That user hasn't hidden a balloon in this channel!")
            if ctx.message.server.id == database[user.id]['server']:
                await self.bot.say("Sorry Bro! That user hasn't hidden a balloon in this channel! Try finding it in #" + database[user.id]['channel'])
            return
        global balloonText
        global gameChannel
        gameChannel = ctx.message.channel
        await self.bot.send_message(gameChannel, "Hey Bro! Wanna play some Balloon World?")
        msg = await self.bot.wait_for_message(author=ctx.message.author, content='yes')
        global rejected
        if rejected == True:
            await self.bot.send_message(gameChannel, "Play again some time!")
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
            await self.bot.send_message(gameChannel, "You ran out of time, Bro! Tough luck!")
            return
        if msg.content == database[user.id]['text']:
            await self.bot.send_message(gameChannel, "You got it right, Bro! Play again sometime.")
        else:
            await self.bot.send_message(gameChannel, "Tough luck Bro. Play again sometime.")
    
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
        print("Test")
        global rejected
        if rejected == True:
            print("Rejected")
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
    async def viewsave(self):
        testdict = await self.loadObj()
        await self.bot.say(str(testdict))
        
    @commands.command()
    async def testsave(self):
        testdict = {"test": "test"}
        await self.saveObj(testdict)
        
    @commands.command()
    async def clearsave(self):
        testdict = {}
        await self.saveObj(testdict)
  
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
            database = await self.loadObj()
            database.update({user.id: {'server': server, 'channel': channel.name, 'text': balloonText}})
            await self.saveObj(database)
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
