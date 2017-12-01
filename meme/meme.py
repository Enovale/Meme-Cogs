import asyncio, aiohttp, discord
import os, sys, linecache, traceback, glob
import re, json, random, math, html
import PIL, PIL.Image, PIL.ImageFont, PIL.ImageOps, PIL.ImageDraw
import hashlib, base64
from vw import macintoshplus
from imgurpython import ImgurClient
from io import BytesIO, StringIO
from discord.ext import commands

class meme:
    """Various Meme Retrieving/Making commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3)
    async def badmeme(self, ctx, direct=None):
        """returns bad meme (shit api)"""
        load = await self.get_json("https://api.imgflip.com/get_memes")
        url = random.choice(load['data']['memes'])
        url = url['url']
        if direct:
                await self.bot.say(url)
        else:
                b = await self.bytes_download(url)
                await self.bot.send_file(b, filename='badmeme.png')

def setup(bot):
    bot.add_cog(meme(bot))
