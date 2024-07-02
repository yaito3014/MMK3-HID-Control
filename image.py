# -*- coding: utf-8 -*-
#
# @Project : MMK3-HID-Control
# @File	   : image.py
# @Date    : 2020-05-04 02:02:30
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0
#
# *****************************************************************************

# from PyQt5.QtGui import QImage
# from PyQt5.QtCore import QByteArray
from rgb_pixel import RGBPixel
from PIL import Image


class MaschineImage(object):
    def __init__(self, image_name):
        image = Image.open(image_name)
        image = image.resize((480, 272))

        self._image_name = image_name
        self._image = image

    @property
    def image(self):
        return self._image

    @property
    def rgb888_pixels(self):
        return list(self._get_image_pixels())

    @property
    def rgb565_bytes(self):
        return self._pixels_to_bytes()

    @staticmethod
    def _converted(pixel):
        return RGBPixel(pixel_value=pixel).byte_value

    def _pixels_to_bytes(self):
        return bytes.join(self._converted(pixel) for pixel in self.rgb888_pixels)


# image = MaschineImage('Live.jpg')
# image_bytes = image.rgb565_bytes

# print(len(image_bytes))
# print('done')
