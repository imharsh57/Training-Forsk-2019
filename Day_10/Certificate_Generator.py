# -*- coding: utf-8 -*-
"""

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts

"""

from PIL import Image,ImageDraw,ImageFont

img =Image.open("E:\Forsk\Day_10\Certificate.png")

name = input("Enter Name : ")

draw = ImageDraw.Draw(img)

Font = ImageFont.truetype("Monotype Corsiva.ttf",60) 

draw.text((590,245),name,(64,0,128),font = Font) #64,0,128  --> rgb \\\  590,245-->coordinates

img.save( name+' Certificate.png', resolution=100.0)

