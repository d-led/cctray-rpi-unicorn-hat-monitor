#!/usr/bin/env python
import unittest
import sys

class FakeHat:
    WIDTH = 8
    HEIGHT = 8
    AREA = 8 * 8
    pixels = {}

    def brightness(self,_):
        pass

    def clear():
        pass

    def set_pixel(self, x, y, r, g, b):
        self.pixels[(x,y)]=(r,g,b)

    def get_pixel(self, x, y):
        return self.pixels.get((x,y))

    def show(self):
        pass

    def dump(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                col = self.get_pixel(x,y)
                if col == (0,0,0):
                        sys.stdout.write('x')
                else:
                        sys.stdout.write('o')
            print('')


class TestFakeHat(unittest.TestCase):

  def test_setting_pixels(self):
    hat = FakeHat()

    hat.set_pixel(4,3,1,2,3)
    self.assertEqual((1,2,3),hat.get_pixel(4,3))

    self.assertEqual(None,hat.get_pixel(0,0))

if __name__ == "__main__":
    unittest.main()
