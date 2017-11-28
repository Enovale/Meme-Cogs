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
import requests
from io import BytesIO

WINDOWS_OS = os.name == 'nt'

class DeepFry:
    """Deep fries images"""

    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists("data/deepfry"):
            os.makedirs("data/deepfry")
        self.path = os.path.join("data", "deepfry")

        
    @commands.command(pass_context=True)
    async def deepfry(self, ctx, link):
        """Will deep fry any image link given. (Adds absurd saturation, etc)"""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        

       	    contrast = ImageEnhance.Contrast( image )
       	    brightness = ImageEnhance.Brightness( image )
       	    sharpness = ImageEnhance.Sharpness( image )
       	    saturation = ImageEnhance.Color( image )
       	    image = sharpness.enhance(5.0)
       	    image = brightness.enhance( 1.5 )
       	    image = contrast.enhance( 8.0 )
       	    image = saturation.enhance( 15.0 )
       	    image = image.filter(ImageFilter.GaussianBlur(1))
       	    image = image.convert("RGB")
            image.save(self.path + "/" + id + ".jpg", quality=8)
       		await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
       		os.remove(self.path + "/" + id + ".jpg")
		else:
			await self.bot.say("Sorry, but this image format is not supported.")
        
    @commands.command(pass_context=True)
    async def customfry(self, ctx, link, contrast, saturation, sharpness, brightness, blur):
        """Will deep fry any image link given. with custom filters"""

        id = ctx.message.author.id
        channel = ctx.message.channel
        response = requests.get(link)
        image = Image.open (BytesIO(response.content))
        

        contrastenhance = ImageEnhance.Contrast( image )
        brightnessenhance = ImageEnhance.Brightness( image )
        sharpnessenhance = ImageEnhance.Sharpness( image )
        saturationenhance = ImageEnhance.Color( image )
        if "." not in contrast:
            contrast = contrast + ".0"
        if "." not in saturation:
            saturation = saturation + ".0"
        if "." not in sharpness:
            sharpness = sharpness + ".0"
        if "." not in brightness:
            brightness = brightness + ".0"
        image = sharpnessenhance.enhance(float(sharpness))
        image = brightnessenhance.enhance( float(brightness) )
        image = contrastenhance.enhance( float(contrast) )
        image = saturationenhance.enhance( float(saturation) )
        image = image.filter(ImageFilter.GaussianBlur(int(blur)))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=8)
        await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
        os.remove(self.path + "/" + id + ".jpg")
        
    @commands.command(pass_context=True)
    async def destroy(self, ctx, link):
        """Will deep fry any image link given, but to such an extreme degree that its no longer recognizable"""
    
        id = ctx.message.author.id
        channel = ctx.message.channel
        response = requests.get(link)
        image = Image.open (BytesIO(response.content))
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(2))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
        os.remove(self.path + "/" + id + ".jpg")

def setup(bot):
    bot.add_cog(DeepFry(bot))
