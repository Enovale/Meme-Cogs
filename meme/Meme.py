import asyncio, aiohttp, discord
#import aalib
import os, sys, linecache, traceback, glob
import re, json, random, math, html
import wand, wand.color, wand.drawing
import PIL, PIL.Image, PIL.ImageFont, PIL.ImageOps, PIL.ImageDraw
import numpy as np
import cairosvg, jpglitch, urbandict
import pixelsort.sorter, pixelsort.sorting, pixelsort.util, pixelsort.interval
import hashlib, base64
from vw import macintoshplus
from urllib.parse import parse_qs
from lxml import etree
from imgurpython import ImgurClient
from io import BytesIO, StringIO
from discord.ext import commands
from utils import checks
from pyfiglet import figlet_format
from string import ascii_lowercase as alphabet
from urllib.parse import quote
from mods.cog import Cog
from concurrent.futures._base import CancelledError

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
