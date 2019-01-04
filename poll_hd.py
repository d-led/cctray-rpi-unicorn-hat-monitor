#!/usr/bin/env python

from sink import Sink
from matrix import Matrix
from cctray_status import CCTray
import sys
import time

# USAGE: sudo python poll_hd.py <poll_wait_s> <cctray.xml_url_1> <cctray.xml_url_2> ... <cctray.xml_url_n>

if len(sys.argv) < 3:
    print("at least 2 arguments needed")
    exit(1)

from RealHatHD import RealHatHD
hat = RealHatHD()
poll_wait_s = int(sys.argv[1])
urls = sys.argv[2:]

#################################################################################

led = Matrix(hat)
sink = Sink(led)

if __name__ == "__main__":
    while True:
      status = []
      for url in urls:   
          try:
              cctray = CCTray(url, hat.AREA)
              status += cctray.fetch()
          except Exception, e:
              print e
    
      sink.put(status)
      time.sleep(poll_wait_s)
