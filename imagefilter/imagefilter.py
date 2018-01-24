import discord
from discord.ext import commands
import os
import math
import asyncio
from cogs.utils.dataIO import dataIO
import PIL
from PIL import Image
import glob, os
from PIL import ImageEnhance
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import requests
from io import BytesIO
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

WINDOWS_OS = os.name == 'nt'

class imagefilter:
    """Allows for various image filtering"""

    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists("data/imagefilter"):
            os.makedirs("data/imagefilter")
        self.path = os.path.join("data", "imagefilter")

        
    @commands.command(pass_context=True)
    async def invert(self, ctx, link):
        """Inverts the given image."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.invert(image)
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
        else:
            await self.bot.say("Sorry, but this image format is not supported.")
            
    @commands.command(pass_context=True)
    async def rotate(self, ctx, link, degrees):
        """Rotates the given image."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = image.rotate(int(degrees), expand=true)
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            
    @commands.command(pass_context=True)
    async def crop(self, ctx, link, pixels):
        """crops the given image by however many pixels you specify."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.crop(image, int(pixels))
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
            
    @commands.command(pass_context=True)
    async def expand(self, ctx, link, pixels, color):
        """expands the given image's border by however many pixels you specify."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.expand(image, border=int(pixels), fill=int(color))
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
		
    @commands.command(pass_context=True)
    async def drake(self, ctx, TopText, BottomText):
        """Makes a drake meme out of your text."""
        
        id = ctx.message.author.id
        channel = ctx.message.channel
	
        try:
            drake = PIL.Image.open(self.path + "/" + "drake.png")
            draw = ImageDraw.Draw(drake)
            font2 = ImageFont.truetype(self.path + "/Arial-Custom.ttf", 20)
            width, height = font2.getsize(TopText)
            image2 = Image.new('RGBA', (500, 400), (0, 0, 0, 0))
            draw2 = ImageDraw.Draw(image2)
            lines = textwrap.wrap(TopText, width=20)
            y_text = 0
            for line in lines:
                width, height = font2.getsize(line)
                draw2.text((0, y_text), line, font=font2, fill='black')
                y_text += height

            px, py = -40, 320
            sx, sy = image2.size
            drake.paste(image2, (px, py, px + sx, py + sy), image2)
            drake.save(self.path + "/" + id + "drake" + ".png")
            await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "drake" + ".png")
            os.remove(self.path + "/" + id + "drake" + ".png")
        except Exception as e:
            await self.bot.say(e)
            print(e)
    
    @commands.command(pass_context=True)
    async def makememe2(self, ctx, link, text:str):
        """Makes a white box above the image and puts text in it to make a meme"""
        
        response = requests.get(link)
        id = ctx.message.author.id
        channel = ctx.message.channel
        img = Image.open (BytesIO(response.content))
        width, height = img.size
        image = Image.new("RGBA", (width, height), (255,255,255))
        imageSize = image.size
        fontSize = int(imageSize[1]/15)
        font = ImageFont.truetype(self.path + "/Arial-Custom.ttf", fontSize)
        lines = textwrap.wrap(text, width=int(imageSize[1]/19))
        w,h = image.size
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            y_text += height
        image = image.resize((w, h+y_text+15))
        image.paste(img, (0, y_text+15))
        draw = ImageDraw.Draw(image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text), line, font=font, fill='black')
            y_text += height
        image.save(self.path + "/" + id + "meme2" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "meme2" + ".png")
        os.remove(self.path + "/" + id + "meme2" + ".png")
        
    @commands.command(pass_context=True)
    async def carl(self, ctx, word):
        """Makes Carl Azuz puns about the word you give it"""
        
        if word in ("train", "trolly"):
            await self.bot.say("Well, you know what they say, *train*ing makes perfect,\nbeing the best can go off the rails,\nbut sometimes you gotta be the caboose.\nThats it for CNN 10.")
        if word in ("santa", "elf", "saint"):
            await self.bot.say("One nice thing about Santa`s workshop, it`s got great elf insurance. That`s a benefit of working for a saint and the nick of time, nurses are able to North Pole off exc-elf-tional treatment and saw things up round the clock for a magical delivery back home even if it was the night before Christmas.\nI`m Carl Azuz, wishing all a good night.")
        else:
            await self.bot.say("If you don't have something punny to say, don't say it at all.")
            await self.bot.say("When your out of ideas, just pun around.")
            await self.bot.say("Thats it for CNN-10.")
        
        await self.bot.say("This is still in development. I applaud your love of Carl Azus though")
        
    @commands.command(pass_context=True)
    async def byemom(self, ctx, user=None, text=None):
        """Puts the user and text into a byemom meme"""
        
        if text == None:
            text = "Sample Text"
        url = None
        id = ctx.message.author.id
        channel = ctx.message.channel
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))
        image2 = image.copy()
        image2 = image2.resize((105,105))
        image = image.resize((60,60))
        # font = ImageFont.truetype(<font-file>, <font-size>)
        #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
        font = ImageFont.truetype(self.path + "/Arial-Custom.ttf", 20)
        width, height = font.getsize(text)
        image3 = Image.new('RGBA', (500, 100), (0, 0, 0, 0))
        draw2 = ImageDraw.Draw(image3)
        x, y = 10, 10
        draw2.text((x, y), text, font=font, fill='black')

        image3 = image3.rotate(25, expand=1)
        byemom = Image.open(self.path + "/" + "byemom.png")
        byemom = byemom.convert("RGBA")
        byemom.paste(image, (540, 25))
        byemom.paste(image2, (90, 360))
        byemom.paste(image3, (356, 365), image3)
        byemom.save(self.path + id + "byemom" + ".png")
        await self.bot.send_file(channel, self.path + id + "byemom" + ".png")
        os.remove (self.path + id + "byemom" + ".png")
        
    @commands.command(pass_context=True)
    async def nut(self, ctx, user=None, text="When you nut"):
        """Makes a white box above the image and puts text in it to make a meme"""
        
        url = None
        id = ctx.message.author.id
        channel = ctx.message.channel
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                nut = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                nut = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            nut = Image.open (BytesIO(response.content))
            
        img = Image.open (self.path + '/' + 'nut.png')
        width, height = img.size
        image = Image.new("RGBA", (width, height), (255,255,255))
        imageSize = image.size
        fontSize = int(imageSize[1]/15)
        font = ImageFont.truetype(self.path + "/Arial-Custom.ttf", 60)
        lines = textwrap.wrap(text, width=45)
        w,h = image.size
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            y_text += height
        image = image.resize((w, h+y_text+15))
        image.paste(img, (0, y_text+15))
        draw = ImageDraw.Draw(image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text), line, font=font, fill='black')
            y_text += height
        nut = nut.resize((450,450))
        image.paste(nut, (100, y_text+420))
        image.save(self.path + "/" + id + "nut" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "nut" + ".png")
        os.remove(self.path + "/" + id + "nut" + ".png")
    
    @commands.command(pass_context=True)
    async def callmeme(self, ctx, text:str):
        """Puts your text on the Tom call meme"""
        
        id = ctx.message.author.id
        channel = ctx.message.channel
        img = Image.open (self.path + '/' + 'call.png')
        width, height = img.size
        image = Image.new("RGBA", (width, height), (255,255,255))
        imageSize = image.size
        fontSize = int(imageSize[1]/15)
        font = ImageFont.truetype(self.path + "/Arial-Custom.ttf", 20)
        lines = textwrap.wrap(text, width=28)
        w,h = image.size
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            y_text += height
        image = image.resize((w, h+y_text+15))
        image.paste(img, (0, y_text+15))
        draw = ImageDraw.Draw(image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
        y_text = 10
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text), line, font=font, fill='black')
            y_text += height
        image.save(self.path + "/" + id + "callmeme" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "callmeme" + ".png")
        os.remove(self.path + "/" + id + "callmeme" + ".png")
            
    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ascii(self, ctx, *, text:str):
        """Convert text into ASCII"""
        asciitext = figlet_format(text, font='starwars')
        await self.bot.say("```" + asciitext + "```")
        
    @commands.command(pass_context=True)
    async def jackoff(self, ctx, user=None):
        
        url = None
        id = ctx.message.author.id
        channel = ctx.message.channel
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))
            
        size = 230, 230
        id = ctx.message.author.id
        channel = ctx.message.channel
        image.thumbnail(size, Image.ANTIALIAS)
        jackoff = Image.open(self.path + "/" + "jackoff.png")
        jackoff.paste(image, (120, 197))
        jackoff.save(self.path + "/" + id + "jackoff" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "jackoff" + ".png")
        os.remove(self.path + "/" + id + "jackoff" + ".png")
        
    @commands.command(pass_context=True)
    async def news(self, ctx, user=None, text=None):
        """Puts a user/image into a breaking news image."""
        
        url = None
        id = ctx.message.author.id
        channel = ctx.message.channel
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if text == None:
            await self.bot.say("Yeah you didnt provide text fam")
            return
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                image2 = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image2 = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image2 = Image.open (BytesIO(response.content))
            
        news = Image.open(self.path + '/' + 'news.png')
        width, height = news.size
        image = Image.new("RGBA", (width, height), (71,111,243))
        imageSize = image.size
        fontSize = 58
        font = ImageFont.truetype(self.path + "/EUROSTIB.ttf", fontSize)
        lines = textwrap.wrap(text, width=19)
        w,h = image.size
        y_text = 410
        for line in lines:
            width, height = font.getsize(line)
            y_text += height
        image = image.resize((w, y_text+height-50))
        image.paste(news, (0, 0))
        draw = ImageDraw.Draw(image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
        y_text = 390
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text), line, font=font, fill='yellow')
            y_text += height
        image2 = image2.resize((242, 192))
        image.paste(image2, (340, 15))
        image.save(self.path + "/" + id + "news" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "news" + ".png")
        os.remove(self.path + "/" + id + "news" + ".png")
        
    @commands.command(pass_context=True)
    async def color(self, ctx, color, user=None):
        """Adds a red filter to image/user Colors are: red, blue, yellow, green, purple, or orange'"""
        
        url = None
        id = ctx.message.author.id
        channel = ctx.message.channel
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))
        
        width, height = image.size
        if color not in ('red', 'blue', 'green', 'yellow', 'purple', 'orange'):
            await self.bot.say("My dude, thats not a color I can do. try red, blue, yellow, green, purple, or orange")
            return
        mask = Image.open(self.path + "/" + color + '.png')
        mask = mask.convert("RGBA")
        mask = mask.resize ((width, height))
        image = image.convert("RGBA")
        image = Image.alpha_composite(image, mask)
        image.save(self.path + "/" + id + "color" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "color" + ".png")
        os.remove(self.path + "/" + id + "color" + ".png")
        
    @commands.command(pass_context=True)
    async def facts(self, ctx, text:str):
        """Puts your text on the good ol' facts meme"""
        
        id = ctx.message.author.id
        channel = ctx.message.channel
	
        try:
            facts = PIL.Image.open(self.path + "/" + "facts.png")
            draw = ImageDraw.Draw(facts)
            font2 = ImageFont.truetype(self.path + "/Arial-Custom.ttf", 20)
            width, height = font2.getsize(text)
            image2 = Image.new('RGBA', (500, 400), (0, 0, 0, 0))
            draw2 = ImageDraw.Draw(image2)
            lines = textwrap.wrap(text, width=17)
            y_text = 0
            for line in lines:
                width, height = font2.getsize(line)
                draw2.text((0, y_text), line, font=font2, fill='black')
                y_text += height

            image2 = image2.rotate(-13, expand=1)

            px, py = -40, 320
            sx, sy = image2.size
            facts.paste(image2, (px, py, px + sx, py + sy), image2)
            #bean.paste(img2, (math.floor(width-100), 0))
            facts.save(self.path + "/" + id + "facts" + ".png")
            await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "facts" + ".png")
            os.remove(self.path + "/" + id + "facts" + ".png")
        except Exception as e:
            await self.bot.say(e)
            print(e)
        
     
    @commands.command(pass_context=True)
    async def makememe(self, ctx, link, TopText, BottomText):
        """Makes memes from the image and text you specify. Make sure to surround the two text areas with quotes for it to work."""
        response = requests.get(link)
        img = Image.open (BytesIO(response.content))
        imageSize = img.size

	# find biggest font size that works
        fontSize = int(imageSize[1]/5)
        font = ImageFont.truetype(self.path + "/Impact-Custom.ttf", fontSize)
        topTextSize = font.getsize(TopText)
        bottomTextSize = font.getsize(BottomText)
        while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
            fontSize = fontSize - 1
            font = ImageFont.truetype(self.path + "/Impact-Custom.ttf", fontSize)
            topTextSize = font.getsize(TopText)
            bottomTextSize = font.getsize(BottomText)

        # find top centered position for top text
        topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
        topTextPositionY = 0
        topTextPosition = (topTextPositionX, topTextPositionY)

        # find bottom centered position for bottom text
        bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
        bottomTextPositionY = imageSize[1] - bottomTextSize[1] - 8
        bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

        draw = ImageDraw.Draw(img)

	# draw outlines
	# there may be a better way
        outlineRange = int(fontSize/15)
        for x in range(-outlineRange, outlineRange+1):
            for y in range(-outlineRange, outlineRange+1):
                draw.text((topTextPosition[0]+x, topTextPosition[1]+y), TopText, (0,0,0), font=font)
                draw.text((bottomTextPosition[0]+x, bottomTextPosition[1]+y), BottomText, (0,0,0), font=font)

        draw.text(topTextPosition, TopText, (255,255,255), font=font)
        draw.text(bottomTextPosition, BottomText, (255,255,255), font=font)
        id = ctx.message.author.id

        img.save(self.path + "/" + id + "meme" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "meme" + ".png")
        os.remove(self.path + "/" + id + "meme" + ".png")
    
    @commands.command(pass_context=True)
    async def avatar(self,ctx, user=None):
        """Grabs you or someone elses avatar"""
	
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                await self.bot.say(avatar)
            else:
                avatar = user.default_avatar_url
                await self.bot.say(avatar)
        else:
            await self.bot.say("Yeah thats not a person kek")
            
    @commands.command(pass_context=True)
    async def funccify(self,ctx, link):
        """Adds a NEW FUNKY MODE to your image."""
	
        try:
            response = requests.get(link)
            response2 = requests.get("http://ejb.x10host.com/funk.png")
            base = Image.open (BytesIO(response.content))
            funk = Image.open (BytesIO(response2.content))
            
            id = ctx.message.author.id
            channel = ctx.message.channel
        
            funkx = funk.width
            funky = funk.height
            basex = base.width
            basey = base.height
            newfunkx = int(round(basex * 0.4))
            newfunky = int(round(funky * (newfunkx / oldfunkx)))
            #await self.bot.say("De:b:ug information: funkx is: " + str(funkx) + " funky is: " + str(funky) + "basex is: " + str(basex) + "basey is " + str(basey) + "newfunkx is: " + str(newfunkx) + "newfunky is: " + str(newfunky))
            funk = funk.resize((newfunkx, newfunky))
            base.paste(funk, (basex - funk.width, 0), funk)
            base.save(self.path + "/" + id + "funky" + ".png")
            await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "funky" + ".png")
            os.remove(self.path + "/" + id + "funky" + ".png")
        except Exception as e:
            await self.bot.say(e)
        
		
    @commands.command(pass_context=True)
    async def bean(self,ctx, user=None, BigText=None, MinorText=None):
        """You just got BEANED"""
	
        url = None
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://cdn.discordapp.com/avatars/' + user.id + '/' + user.avatar + '.png'
                response = requests.get(avatar)
                img = Image.open (BytesIO(response.content))
                img2 = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                img = Image.open (BytesIO(response.content))
                img2 = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            img = Image.open (BytesIO(response.content))
            img2 = Image.open (BytesIO(response.content))
	
        id = ctx.message.author.id
        channel = ctx.message.channel
	
        try:
            bean = PIL.Image.open(self.path + "/" + "bean.png")
            draw = ImageDraw.Draw(bean)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            #font = ImageFont.truetype(self.path + "/VerdanaBold.ttf", 70)
            font = ImageFont.truetype(self.path + "/Verdana-Bold-Custom.ttf", 260)
            font2 = ImageFont.truetype(self.path + "/Verdana-Custom.ttf", 190)
            if BigText == None:
                text = 'BEANED!!!'
            else:
                text = BigText
            if MinorText == None:
                MinorText = "BEAN!"
            width, height = font.getsize(text)
            image2 = Image.new('RGBA', (3000, 800), (0, 0, 0, 0))
            draw2 = ImageDraw.Draw(image2)
            x, y = 10, 10
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw2.text((x-15, y), text, font=font, fill='black')
            draw2.text((x+15, y), text, font=font, fill='black')
            draw2.text((x, y-15), text, font=font, fill='black')
            draw2.text((x, y+15), text, font=font, fill='black')

            # thicker border
            draw2.text((x-15, y-15), text, font=font, fill='black')
            draw2.text((x+15, y-15), text, font=font, fill='black')
            draw2.text((x-15, y+15), text, font=font, fill='black')
            draw2.text((x+15, y+15), text, font=font, fill='black')

            # now draw the text over it
            draw2.text((x, y), text, font=font, fill='#8ff60f')

            image2 = image2.rotate(4, expand=1)

            px, py = 250, 400
            sx, sy = image2.size
            width, height = bean.size
            width2, height2 = img.size
            img = img.resize((1320, 1500))
            bean.paste(img, (math.floor(width/5), math.floor(height/3)))
            bean.paste(image2, (px, py, px + sx, py + sy), image2)
            draw.multiline_text((80, 20),"Uh oh! You friccin\nmoron. You just got",(0,0,0),font=font2, align='center')
            draw.multiline_text((80, 2520),"Tag your friends to\ntotally " + MinorText + " them!",(0,0,0),font=font2, align='center')
            img2.putalpha(50)
            img2 = img2.resize((400, 700))
            #bean.paste(img2, (math.floor(width-100), 0))
            bean.save(self.path + "/" + id + "beaned" + ".png")
            await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "beaned" + ".png")
            os.remove(self.path + "/" + id + "beaned" + ".png")
        except Exception as e:
            await self.bot.say(e)
            print(e)

def setup(bot):
    bot.add_cog(imagefilter(bot))
