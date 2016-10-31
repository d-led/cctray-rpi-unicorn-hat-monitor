from __future__ import print_function
import sys
import unittest

class Sink:
    STATUS = {
        'NONE': (0,0,0),
        'BUILDING': (255,255,0),
        'ERROR': (255,0,0),
        'OK': (0,255,0),
        'UNKNOWN': (200,200,190),
    }
    NO_STATUS = (128,128,110)
    MAX_STATUS = 64
    matrix = None

    def __init__(self, m):
        self.matrix = m
        if m:
            self.MAX_STATUS = m.AREA
            self.matrix.brightness(0.6)

    def put(self,status):
        status = status[:self.MAX_STATUS] #trim the input
        translated = [self.STATUS.get(s,self.NO_STATUS) for s in status]
        self.notify(translated)
        return translated


    def translate_status(self,val):
        return self.STATUS[val]

    def notify(self,status_colors):
        if self.matrix:
            self.matrix.show(status_colors)
        print(status_colors,file=sys.stderr)

#################################################################################

class TestSink(unittest.TestCase):

  def test_upper(self):
    sink = Sink(None)
    def ignore(args):
        pass
    sink.notify = ignore
    self.assertEqual([(0,0,0)], sink.put(['NONE']))

if __name__ == "__main__":
    unittest.main()
