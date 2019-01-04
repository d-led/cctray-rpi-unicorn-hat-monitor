#!/usr/bin/env python
import unicornhathd as hat

class RealHatHD:
    WIDTH = 16
    HEIGHT = 16
    AREA = 16 * 16

    def brightness(self,b):
        hat.brightness(b)

    def clear():
        hat.clear()

    def set_pixel(self, x, y, r, g, b):
        hat.set_pixel(x,y,r,g,b)

    def get_pixel(self, x, y):
        return hat.get_pixel(x,y)

    def show(self):
        hat.show()

    def dump(self):
        pass

