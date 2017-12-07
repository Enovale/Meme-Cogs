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
        lines = textwrap.wrap(text, width=int(imageSize[1]/15))
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
    async def ascii(self, ctx, *, text:str):
        """Convert text into ASCII"""
        asciitext = figlet_format(text, font='starwars')
        await self.bot.say("```" + asciitext + "```")
        
    @commands.command(pass_context=True)
    async def red(self, ctx, user=None):
        """Adds a red filter to image/user"""
        
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
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
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
        mask = Image.open(self.path + "/" + 'red.png')
        mask = mask.convert("RGBA")
        mask = mask.resize ((width, height))
        image = image.convert("RGBA")
        image = Image.alpha_composite(image, mask)
        image.save(self.path + "/" + id + "red" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "red" + ".png")
        os.remove(self.path + "/" + id + "red" + ".png")
        
     
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5)
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
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
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
