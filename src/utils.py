import os
from PIL import ImageFont

def createfont(font, size):
    pathfreemono = 'fonts/FreeMono.ttf'
    pathfreemonobold = 'fonts/FreeMonoBold.ttf'
    pathsawasdee = 'fonts/Sawasdee-Bold.ttf'

    if font == 'freemono':
        return ImageFont.truetype(pathfreemono, size)
    if font == 'freemonobold':
        return ImageFont.truetype(pathfreemonobold, size)
    if font == 'sawasdee':
        return ImageFont.truetype(pathsawasdee, size)
    else:
        print('Font not available')
