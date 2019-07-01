# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:59:38 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image
img=Image.open('test.jpg')
#img.show()
img_gray=img.convert('LA')
img_gray.show()
img_gray.save("test_gray.png")

img_rotate= img.transpose(Image.ROTATE_90)
img_rotate.save("test_rotate.jpg")
#img_rotate.show()

width, height = img_rotate.size
hw = width/2
hh = height/2
img_crop = img.crop((hw-80,hh-102,hw+80,hh+102))
img_crop.save('crop_test.jpg')

img.thumbnail((75,75))
print(img.width, img.height)
img.save("test_thumb.jpg")

