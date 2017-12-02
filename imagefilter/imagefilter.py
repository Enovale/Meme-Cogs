import discord
from discord.ext import commands
import os
import asyncio
from cogs.utils.dataIO import dataIO
import PIL
from PIL import Image
import glob, os
from PIL import ImageEnhance
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageOps
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
        """Inverts the given image."""

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
    @commands.cooldown(1, 5)
    async def ascii(self, ctx, *, text:str):
        """Convert text into ASCII"""
        await self.bot.say("```" + figlet_format(ctx.message.content, font='starwars') + "```")

def setup(bot):
    bot.add_cog(imagefilter(bot))
