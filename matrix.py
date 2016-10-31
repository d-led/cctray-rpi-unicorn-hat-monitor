#!/usr/bin/env python
from FakeHat import FakeHat
import unittest
import sys

class Matrix:
	hat = None

	def __init__(self, hat=None):
		if hat:
			self.hat = hat
		else:
			hat = FakeHat()
			self.hat = hat

		self.AREA = hat.AREA

	def show(self, matrix_colors):
		w = self.hat.WIDTH
		h = self.hat.HEIGHT
		area = self.AREA
		count = len(matrix_colors)
		for pos in range(self.AREA):
			x = pos % w
			y = pos // h

			if pos < count:
				color = matrix_colors[pos]
				self.hat.set_pixel(x,y,color[0],color[1],color[2])

			else:
				self.hat.set_pixel(x,y,0,0,0)

		self.hat.show()
		self.dump()

	def brightness(self,b):
		self.hat.brightness(b)

	def dump(self):
		self.hat.dump()



class TestMatrix(unittest.TestCase):

	def test_setting_some_pixels(self):
		matrix = Matrix()
		self.assertNotEqual(None,matrix.hat)

		matrix.show([(1,2,3),(4,5,6)])
		self.assertEqual((4,5,6), matrix.hat.get_pixel(1,0))
		self.assertEqual((0,0,0), matrix.hat.get_pixel(0,1))
		self.assertEqual((0,0,0), matrix.hat.get_pixel(1,1))

	def test_overflow_is_ignored(self):
		matrix = Matrix()
		col = (1,2,3)
		colors = [col] * matrix.AREA
		colors.append((42,42,42))
		matrix.show(colors)
		self.assertEqual(col, matrix.hat.get_pixel(0,0))
		self.assertEqual(col, matrix.hat.get_pixel(0,1))
		self.assertEqual(col, matrix.hat.get_pixel(1,1))
		self.assertEqual(col, matrix.hat.get_pixel(1,0))

if __name__ == "__main__":
	unittest.main()
