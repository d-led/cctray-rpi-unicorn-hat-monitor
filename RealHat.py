#!/usr/bin/env python
import unicornhat as hat

class RealHat:
    WIDTH = 8
    HEIGHT = 8
    AREA = 8 * 8

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

